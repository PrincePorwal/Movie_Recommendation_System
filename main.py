import streamlit as st
import pickle
import pandas as pd
import requests
import random

# Load the necessary python pickle files
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

# recommend movies based on content
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
   
    for  i in movies_list:
       
        recommended_movies.append(movies.iloc[i[0]].title)
        

    return recommended_movies 

# List of emoji options
emoji_options = [":movie_camera:", ":popcorn:", ":clapper:", ":film_frames:", ":ticket:",":star:",":headphones:" ,":camera_with_flash:",":sunglasses:"]

#Display Title, Dropdown
st.title("Movie Recommendation System🍿")

selected_movie_name = st.selectbox('Select a movie to recommend', movies['title'].values)

# Output recommendations 
if st.button('Recommend'):
    name = recommend(selected_movie_name)
    for movie_name in name:
        random_emoji = random.choice(emoji_options)
        st.write(f"## {movie_name} {random_emoji}")








       