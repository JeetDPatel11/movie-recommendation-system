import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Load datasets
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

# Create pivot table
movie_ratings = ratings.pivot_table(index='movieId',columns='userId',values='rating').fillna(0)

# Compute similarity
similarity = cosine_similarity(movie_ratings)

# Save similarity matrix
pickle.dump(similarity, open("similarity.pkl","wb"))

print("similarity.pkl created successfully")