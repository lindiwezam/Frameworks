import pandas as pd
df = pd.read_csv('metadata.csv')
missing_values = df.isnull().sum()
print(missing_values)

df.fillna('unknown', inplace=True)

df.to_csv('metadata_cleaned.csv', index=False)

df['publication_date'] = pd.to_datetime(df['publication_date'], errors='coerce')

df['publication_year'] = df['publication_date'].dt.year

df['abstract_word_count'] = df['abstract'].apply(lambda x: len(str(x).split()))

df.to_csv('metadata_prepared.csv', index=False)