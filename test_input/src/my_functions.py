import pandas as pd


def read_input(file):
    infile = pd.read_csv(file, sep='\t')
