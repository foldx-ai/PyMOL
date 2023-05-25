import hashlib
import pymol
import requests


ATLAS_URI = "https://api.esmatlas.com/foldSequence/v1/pdb/"
FOLDXAI_URI = 'https://api.foldx.ai/fb'
valid = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
foldx_seq = ""
foldx_name = ""
foldx_pdb = ""

def thumbsup() -> None:
    data = {
        'name': foldx_name,
        'sequence': foldx_seq,
        'original_pdb': foldx_pdb,
        'approved': True,
        'revised_pdb': pymol.cmd.get_pdbstr('all'),
    }
    response = requests.post(FOLDXAI_URI, json=data)
    if response.status_code > 299:
        print('error:' + response.text)
    else:
        print("submitted")

def thumbsdown() -> None:
    data = {
        'name': foldx_name,
        'sequence': foldx_seq,
        'original_pdb': foldx_pdb,
        'approved': False,
        'revised_pdb': pymol.cmd.get_pdbstr('all'),
    }
    response = requests.post(FOLDXAI_URI, json=data)
    if response.status_code > 299:
        print('error:' + response.text)
    else:
        print("submitted")


def foldx(sequence:str, name: str=None) -> None:
    '''Given a protein sequence foldx will generate a pdb 
    file of string and load it into pymol.'''
    global foldx_name
    global foldx_pdb
    global foldx_seq
    pymol.cmd.delete('all')
    if not name:
        name = hashlib.md5(sequence.encode('utf-8')).hexdigest()[:6]
    foldx_name = name
    sequence = sequence.upper()
    for i in sequence:
        if i not in valid:
            print('ERROR: Invalid  one-letter code. ' + i + ' is invalid.')
            return
    foldx_seq = sequence
    response = requests.post(ATLAS_URI, data=sequence)
    if response.status_code > 299:
        print('error:' + response.text)
        return
    foldx_pdb = response.text
    pymol.cmd.read_pdbstr(response.text, name)

pymol.cmd.extend('foldx', foldx)
pymol.cmd.extend('thumbsup', thumbsup)
pymol.cmd.extend('thumbsdown', thumbsdown)