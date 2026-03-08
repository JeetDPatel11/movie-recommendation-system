import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------
# Load Dataset
# -------------------------
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

# -------------------------
# Clean Movie Titles
# -------------------------
def clean_title(title):

    year = title[title.find("("):] if "(" in title else ""

    name = title.split("(")[0].strip()

    if ", The" in name:
        name = "The " + name.replace(", The", "")

    if ", A" in name:
        name = "A " + name.replace(", A", "")

    if ", An" in name:
        name = "An " + name.replace(", An", "")

    return name + " " + year

def extract_year(title):
    if "(" in title and ")" in title:
        return title.split("(")[-1].replace(")", "")
    return ""

def clean_title(title):

    # remove year
    title = title.split("(")[0].strip()

    # fix titles like "Lion King, The"
    if ", The" in title:
        title = "The " + title.replace(", The", "")

    if ", A" in title:
        title = "A " + title.replace(", A", "")

    if ", An" in title:
        title = "An " + title.replace(", An", "")

    return title


movies["clean_title"] = movies["title"].apply(clean_title)

movies["year"] = movies["title"].str.extract(r"\((\d{4})\)")
movies["display_title"] = movies["clean_title"] + " (" + movies["year"] + ")"


# -------------------------
# Create User-Movie Matrix
# -------------------------
movie_ratings = ratings.pivot_table(
    index="userId",
    columns="movieId",
    values="rating"
)

movie_ratings = movie_ratings.fillna(0)


# -------------------------
# Similarity Matrix
# -------------------------
similarity = cosine_similarity(movie_ratings.T)

similarity_df = pd.DataFrame(
    similarity,
    index=movie_ratings.columns,
    columns=movie_ratings.columns
)


# -------------------------
# Recommendation Function
# -------------------------
def recommend(movie_title):

    movie_id = movies[movies["clean_title"] == movie_title]["movieId"].values[0]

    similar_movies = similarity_df[movie_id].sort_values(ascending=False)[1:6]

    recommended_movies = []

    for movie in similar_movies.index:

        title = movies[movies["movieId"] == movie]["clean_title"].values[0]

        recommended_movies.append(title)

    return recommended_movies


# -------------------------
# Streamlit UI
# -------------------------
st.title("Movie Recommendation System 🎬")

movie_list = movies["display_title"].values

selected_display_movie = st.selectbox("Select a movie", movie_list)

selected_movie = movies[movies["display_title"] == selected_display_movie]["clean_title"].values[0]


# -------------------------
# Recommendation Button
# -------------------------
if st.button("Recommend"):

    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies")

    for movie in recommendations:

        year = movies[movies["clean_title"] == movie]["title"].values[0]
        year = extract_year(year)

        st.write(f"{movie} ({year})")