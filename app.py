import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_posters(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=276d57c4b0b78e85ac4b249dd278720f&language=en-US'.format(movie_id))
    data = response.json()
    return 'http://image.tmdb.org/t/p/w500/' + data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    movies_list = sorted(enumerate(similarity[movie_index]),reverse=True,key=lambda x: x[1])[1:6]
    recommendations = []
    posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        # Fetch Posters from API
        posters.append(fetch_posters(movie_id))
        recommendations.append(movies.iloc[i[0]].title)
    return recommendations , posters

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    "Select your favorite movie",
    movies['title'].values
)
if st.button("Recommend"):
    st.write("Recommended for you :")
    recommendations,posters = recommend(selected_movie_name)
    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        st.image(posters[0])
        st.write(recommendations[0])
    with col2:
        st.image(posters[1])
        st.write(recommendations[1])
    with col3:
        st.image(posters[2])
        st.write(recommendations[2])

    with col4:
        st.image(posters[3])
        st.write(recommendations[3])
    with col5:
        st.image(posters[4])
        st.write(recommendations[4])