import pandas as pd
import streamlit as st
import pickle
import requests

st.title("Movie Recommder System")
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
def recommendations(movie):
    arr=[]
    posters=[]
    ind = movies[movies["title"] == movie].index[0]
    distances = similarity[ind]
    lis = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:5]
    for i in lis:
        a=fetch_poster(movies.iloc[i[0]].movie_id)
        posters.append(a)
        arr.append(movies.iloc[i[0]].title)
    return arr,posters

movies_list=pickle.load(open("movie_dict.pkl","rb"))
movies=pd.DataFrame(movies_list)
options=st.selectbox(
    'write the name of the movie ',
    movies["title"].values)
similarity=pickle.load(open("similarity.pkl","rb"))
if st.button('Recommend'):

    col1, col2, col3,col4,col5= st.columns(5)
    try:
        name,poster=recommendations(options)
        with col1:
            st.text(name[0])
            st.image(poster[0])

        with col2:
            st.text(name[1])
            st.image(poster[1])

        with col3:
            st.text(name[2])
            st.image(poster[2])
        with col4:
            st.text(name[3])
            st.image(poster[3])
        with col5:
            st.text(name[4])
            st.image(poster[4])
    except:
        st.text("Sorry could not fetch posters")






