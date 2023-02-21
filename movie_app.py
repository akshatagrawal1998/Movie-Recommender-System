import streamlit as st
import pickle 
import pandas as pd

similarity = pickle.load(open('similarity.pkl' , 'rb'))

def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])

    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(movies_df.iloc[i[0]].title)
    return recommended_movies


movie_dict = pickle.load(open('movies_dict.pkl' , 'rb'))

movies_df = pd.DataFrame(movie_dict)
st.title("Movie Recommender System")

selected_movie_name = st.selectbox('Select a Movie', 
movies_df['title'].values)

if st.button ('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations[1:6]:
        st.write(i)