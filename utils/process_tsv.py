import pandas as pd
import re

def process_tsv(input_path, output_path):
    df = pd.read_csv(input_path, sep='\t')
    df = df[df['id'].str.startswith('ger')]
    df['text'] = df['text'].astype(str)  # Ensure 'text' is a string
    df['text'] = df['text'].str.replace(r'\*{3,}', ' Scheiße ', regex=True)
    df['text'] = df['text'].apply(lambda x: re.sub(r'@\S+', '', x))
    df['text'] = df['text'].str.replace(r'http\S+', '', regex=True)
    df['text'] = df['text'].str.replace(r'(.)\1{2,}', r'\1', regex=True)
    df['text'] = df['text'].str.strip()
    df.to_csv(output_path, sep='\t', index=False)

if __name__ == "__main__":
    input_path = "./data/test.tsv"
    output_path = "./data/processed_ger_test.tsv"
    process_tsv(input_path, output_path)
