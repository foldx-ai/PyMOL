import pymol
import requests
import hashlib

URI = "https://api.esmatlas.com/foldSequence/v1/pdb/"

def foldx(sequence:str, name: str=None) -> None:
    '''Given a protein sequence foldx will generate a pdb 
    file of string and load it into pymol.'''
    if not name:
        name = hashlib.md5(sequence.encode('utf-8')).hexdigest()[:6]
    sequence = sequence.upper()
    response =requests.post(URI, data=sequence)
    if response.status_code > 299:
        print('error:' + response.text)
        return
    pymol.cmd.read_pdbstr(response.text, name)

pymol.cmd.extend('foldx', foldx)