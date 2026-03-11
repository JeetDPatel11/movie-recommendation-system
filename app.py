import streamlit as st
import pandas as pd
import pickle
import requests

# -------------------------------------------------
# Page Config
# -------------------------------------------------

st.set_page_config(page_title="Movie Recommendation System", layout="wide")

st.title("🎬 Movie Recommendation System")

# -------------------------------------------------
# Fix MovieLens Titles
# -------------------------------------------------

def fix_title(title):

    articles = ["The", "A", "An", "Le", "La", "Les"]

    for article in articles:
        if f", {article}" in title:
            title = title.replace(f", {article}", "")
            title = f"{article} {title}"

    return title

# -------------------------------------------------
# Load Data
# -------------------------------------------------

movies = pd.read_csv("movies.csv")

movies["title"] = movies["title"].apply(fix_title)

@st.cache_resource
def load_similarity():
    return pickle.load(open("similarity.pkl", "rb"))

similarity = load_similarity()

# -------------------------------------------------
# OMDB API
# -------------------------------------------------

API_KEY = "99b21769"

def fetch_movie_details(title):

    clean_title = title.split("(")[0].strip()

    url = f"http://www.omdbapi.com/?t={clean_title}&apikey={API_KEY}"

    try:

        data = requests.get(url).json()

        poster = data.get("Poster")
        rating = data.get("imdbRating")
        genre = data.get("Genre")
        plot = data.get("Plot")

        if poster == "N/A" or poster is None:
            poster = "https://via.placeholder.com/300x450?text=No+Poster"

        if rating is None:
            rating = "N/A"

        if genre is None:
            genre = "N/A"

        if plot is None:
            plot = "No description available"

        return poster, rating, genre, plot

    except:

        return (
            "https://via.placeholder.com/300x450?text=No+Poster",
            "N/A",
            "N/A",
            "No description available"
        )

# -------------------------------------------------
# Recommendation Function
# -------------------------------------------------

def recommend(movie):

    movie_index = movies[movies["title"] == movie].index[0]

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

# -------------------------------------------------
# Movie Selector
# -------------------------------------------------

selected_movie = st.selectbox(
    "Search or Select a Movie",
    movies["title"].values
)

# -------------------------------------------------
# Recommend Button
# -------------------------------------------------

if st.button("Recommend"):

    with st.spinner("Finding best movies for you..."):

        names = recommend(selected_movie)

        cols = st.columns(5)

        for i in range(5):

            with cols[i]:

                poster, rating, genre, plot = fetch_movie_details(names[i])

                st.image(poster, use_container_width=True)

                st.write(names[i])
                st.write(f"⭐ IMDb: {rating}")
                st.write(f"🎭 {genre}")

                with st.expander("Plot"):
                    st.write(plot)

# -------------------------------------------------
# Footer
# -------------------------------------------------

st.markdown("---")
st.markdown("Built by **Jeet Patel** 🚀")