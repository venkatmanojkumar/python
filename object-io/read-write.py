from itertools import islice
from msilib import sequence


def read_series(filename):
    """using with in read series"""
    with open(filename, mode='rt', encoding='utf-8') as f:
        return[int(line.strip()) for line in f]

def write_sequence(filename,num):
    with open(filename,mode='wt',encoding='utf-8') as f:
        f.writelines(f"{r}\n" for r in islice(sequence(),num + 1))
