import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

# Create user-movie matrix
movie_ratings = ratings.pivot_table(index='userId', columns='movieId', values='rating')

# Fill missing values
movie_ratings = movie_ratings.fillna(0)

# Calculate similarity between movies
similarity = cosine_similarity(movie_ratings.T)

# Convert similarity matrix to DataFrame
similarity_df = pd.DataFrame(similarity, index=movie_ratings.columns, columns=movie_ratings.columns)

# Streamlit UI
st.title("Movie Recommendation System 🎬")

movie_list = movies['title'].values
selected_movie = st.selectbox("Select a movie", movie_list)

def recommend(movie_title):
    movie_id = movies[movies['title'] == movie_title]['movieId'].values[0]
    
    similar_scores = similarity_df[movie_id].sort_values(ascending=False)[1:6]
    
    recommended_movies = []
    
    for movie in similar_scores.index:
        title = movies[movies['movieId'] == movie]['title'].values[0]
        recommended_movies.append(title)
        
    return recommended_movies

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    
    st.write("Recommended Movies:")
    
    for movie in recommendations:
        st.write(movie)