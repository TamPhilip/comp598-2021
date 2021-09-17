# Philip Tam 260849613
from pathlib import Path
import os, sys

from pandas.core.frame import DataFrame
parentdir = Path(__file__).parents[0]
sys.path.append(parentdir)
import pandas as pd


class Result():

    def __init__(self) -> None:
        self.path = '/Users/philiptam/Projects/comp598-2021/hw1/submission_template/dataset.tsv'

    def main(self):
        df = self.create()
        self.export(df)

    def create(self):
        df = pd.read_csv(self.path, sep='\t')
        
        data = {"result" : ["frac-trump-mentions"], "value" : ['%.3f' % (len(df[df['trump_mention'] == True]) / len(df))]}
        new_df = DataFrame(data=data)

        return new_df

    def export(self, df):
        df.to_csv('results.tsv', sep = '\t', index=False)
        

if __name__ == '__main__':
    Result().main()