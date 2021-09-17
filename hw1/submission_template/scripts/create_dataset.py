# Philip Tam 260849613
from pathlib import Path
import os, sys
parentdir = Path(__file__).parents[0]
sys.path.append(parentdir)
import pandas as pd


class Dataset():

    def __init__(self) -> None:
        self.path = '/Users/philiptam/Projects/comp598-2021/hw1/submission_template/data/IRAhandle_tweets_1.csv'

    def main(self):
        df = self.create()
        self.export(df)

    def create(self):
        df = pd.read_csv(self.path)
        # Keep only first 10,000
        df = df.head(10000)
        # Keep only english
        df = df[df['language'] == "English"]
        # Remove rows with ?
        df = df[df['content'].str.contains('\?') == False]
        # Add Trump Feature
        df['trump_mention'] = df['content'].str.contains('[^a-zA-Z0-9]Trump[^a-zA-Z0-9]|^Trump[^a-zA-Z0-9]|[^a-zA-Z0-9]Trump$')
        return df

    def export(self, df):
        df[['tweet_id', 'publish_date', 'content','trump_mention']].to_csv('dataset.tsv', sep = '\t', index=False)
        print(len(df))
        

if __name__ == '__main__':
    Dataset().main()