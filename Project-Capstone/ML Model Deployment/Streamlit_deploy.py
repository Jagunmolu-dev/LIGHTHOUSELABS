import streamlit as st
import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Set page title
st.set_page_config(page_title="Movie Recommender Engine")

# Set page header
st.write("""
# Movie Recommender Engine
""")

# loading the data from the csv file to a pandas dataframe
movies_data = pd.read_csv('movies.csv')

# selecting the relevant features for recommendation
selected_features = ['genres','keywords','tagline','cast','director']

# replacing the null values with null string
for feature in selected_features:
  movies_data[feature] = movies_data[feature].fillna('')

# combining all the 5 selected features
combined_features = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']

# converting the text data to feature vectors
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

# getting the similarity scores using cosine similarity
similarity = cosine_similarity(feature_vectors)

# Get user input
movie_name = st.text_input('Enter your favourite movie name:')

# Find close match to user input in the movie titles
list_of_all_titles = movies_data['title'].tolist()
find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
close_match = find_close_match[0]

# Get index of the movie in the dataframe
index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

# Get similarity scores for all movies
similarity_score = list(enumerate(similarity[index_of_the_movie]))

# Sort the movies by similarity score
sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)

# Display recommended movies
st.write('Movies suggested for you:')
for i, movie in enumerate(sorted_similar_movies):
  index = movie[0]
  title_from_index = movies_data[movies_data.index==index]['title'].values[0]
  if (i<30):
    st.write(f"{i+1}. {title_from_index}")