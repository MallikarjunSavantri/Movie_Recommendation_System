import streamlit as st
from pathlib import Path
import pickle

BASE_DIR = Path(__file__).resolve().parent.parent

movies = pickle.load(open(BASE_DIR / "models" / "movies.pkl", "rb"))
similarity = pickle.load(open(BASE_DIR / "models" / "similarity.pkl", "rb"))

#Recommendation function
def recommend(movie):

    movie_index = movies[movies["title"]==movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(enumerate(distances), reverse=True, key=lambda x:x[1])

    recommended=[]

    for i in movies_list[1:6]:
        recommended.append(movies.iloc[i[0]].title)
    return recommended

#UI
st.title("Movie Recommendation System")

selected_movie = st.selectbox("Select a movie", movies["title"].values)

#recommendation button to select movies
if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    
    #display
    for movie in recommendations:
        st.write(movie)