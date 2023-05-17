import pymol
import requests

URI = "https://api.esmatlas.com/foldSequence/v1/pdb/"

def foldx(sequence, name=None):
    '''Given a protein sequence foldx will generate a pdb 
    file of string and load it into pymol.'''
    response =requests.post(URI, data=sequence)
    pymol.cmd.read_pdbstr(response.text, name)

pymol.cmd.extend('foldx', foldx)