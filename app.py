!pip install streamlit
import streamlit as st
import pickle

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox(
    "Choose a movie",
    movies['title'].values
)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = []
    for i in movie_list:
        recommendations.append(movies.iloc[i[0]].title)
    return recommendations

if st.button("Recommend"):
    results = recommend(selected_movie)
    for movie in results:
        st.write("🍿", movie)
