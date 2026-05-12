import pandas as pd

df = pd.read_csv("tmdb_5000_movies.csv")

df = df[['title', 'overview', 'genres', 'keywords']]
df = df.fillna('')
import ast

def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return " ".join(L)
df['genres'] = df['genres'].apply(convert)
df['keywords'] = df['keywords'].apply(convert)
df['tags'] = df['overview'] + " " + df['genres'] + " " + df['keywords']

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(stop_words='english')
vectors = tfidf.fit_transform(df['tags'])

from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vectors)

def recommend(movie):
    index = df[df['title'] == movie].index[0]
    distances = similarity[index]
    
    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:11]

    for i in movies_list:
        print(df.iloc[i[0]].title)
      
