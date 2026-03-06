# 🎬 Movie Recommendation System

A web-based Movie Recommendation System built using **Python, Machine Learning, and Streamlit**.
The application recommends movies similar to a selected movie using **content-based filtering and cosine similarity**.

This project was developed as part of the **GTU Internship 2026 – Domain 4: Entertainment and Media**.

---

# 📌 Features

* Interactive web interface using Streamlit
* Movie recommendation based on genres
* Content-based filtering algorithm
* Fast similarity calculation using cosine similarity
* Easy movie selection using dropdown menu

---

# 🧠 Machine Learning Approach

The system uses **Content-Based Filtering**.

Steps used in the model:

1. Load movie dataset
2. Extract movie genres
3. Convert genres into vectors using CountVectorizer
4. Compute similarity between movies using Cosine Similarity
5. Recommend the top 5 most similar movies

---

# 📂 Project Structure

```
movie_recommendation_app
│
├── app.py              # Streamlit web application
├── movies.csv          # Movie dataset
├── ratings.csv         # User rating dataset
├── requirements.txt    # Required Python libraries
└── README.md
```

---

# 📊 Dataset

Dataset used: **MovieLens Dataset**

Source:
https://grouplens.org/datasets/movielens/

The dataset contains:

* Movie titles
* Genres
* User ratings

---

# ⚙️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit
* Machine Learning
* Cosine Similarity Algorithm

---

# 🚀 How to Run the Project

1. Clone the repository

```
git clone https://github.com/yourusername/movie-recommendation-system.git
```

2. Navigate to the project folder

```
cd movie-recommendation-system
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Run the Streamlit app

```
streamlit run app.py
```

5. Open the browser and access the local URL.

---

# 🎯 Project Objective

The goal of this project is to solve the problem of **content overload in entertainment platforms** by recommending relevant movies based on user preferences.

---

# 📌 Future Improvements

* Add movie posters
* Improve recommendation accuracy
* Integrate user ratings
* Add popularity prediction
* Enhance UI design

---

# 👨‍💻 Author

**Patel Jeet Dharmeshbhai**
GTU – Institute of Technology and Research (ITR), Mehsana
Computer Engineering

---

# 📜 License

This project is for **educational and internship demonstration purposes**.
