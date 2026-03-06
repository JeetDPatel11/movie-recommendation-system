import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Page title
st.title("🎬 Movie Recommendation System")

# Load movie dataset
movies = pd.read_csv("movies.csv")

# Clean genres column
movies["genres"] = movies["genres"].str.replace("|", " ")

# Convert text to numeric vectors
vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(movies["genres"])

# Calculate similarity between movies
similarity = cosine_similarity(genre_matrix)

# Recommendation function
def recommend(movie_name):
    movie_index = movies[movies["title"] == movie_name].index[0]
    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# Movie selection dropdown
selected_movie = st.selectbox(
    "Select a movie",
    movies["title"].values
)

# Button to trigger recommendation
if st.button("Recommend"):
    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies:")
    for movie in recommendations:
        st.write(movie)