import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

df = pd.read_csv('metadata.csv')

all_titles = ''.join(df['title'].dropna())

all_titles = all_titles.lower()

stop_words = set(stopwords.words('english'))
words = [word forword in all_titles.split() if word not in stop_words]
filtered_titles = ''.join(words)

wordcloud = WordCloud(width=800, height=400, max_words=100).generate(filtered_titles)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show