# recommend.py

import streamlit as st
from recommend_backend import RecommendationSystem
import pandas as pd

def run():
    # Initialize the recommendation system
    csv_path = r'amazon_prime_titles.csv'
    recommender = RecommendationSystem(csv_path)

    # Set title for the recommendation page
    st.title("Movie Recommendation System")

    # Sidebar inputs
    st.sidebar.header("Select Your Preferences")

    # Dropdown for genre selection
    genre_options = ['All', 'Action', 'Comedy', 'Drama', 'Horror', 'Romance', 'Thriller', 'Sci-Fi', 'Fantasy']
    selected_genre = st.sidebar.selectbox("Select Movie Genre:", genre_options)

    # Dropdown for year range selection
    year_options = list(range(1900, 2025))
    selected_year_start = st.sidebar.selectbox("Select Starting Year:", year_options)
    selected_year_end = st.sidebar.selectbox("Select Ending Year:", year_options)

    # Dropdown for type selection
    type_options = ['All', 'Movie', 'TV Show']
    selected_type = st.sidebar.selectbox("Select Type:", type_options)

    # Duration range selection
    duration_range = st.sidebar.slider("Select Duration Range (minutes):", min_value=0, max_value=300, value=(0, 300))

    # Submit button
    if st.sidebar.button("Submit"):
        recommendations = recommender.get_recommendations(selected_genre, selected_year_start, selected_year_end, selected_type, duration_range)

        # Display recommendations
        st.header("Here are the movies closest to your description:")
        if not recommendations.empty:
            for index, row in recommendations.iterrows():
                # Display the title in a larger font
                st.subheader(row['title'])  # Use subheader to make it prominent

                # Create a DataFrame for displaying movie details
                data = {
                    "Field": ["Type", "Director", "Cast", "Country", "Release Year", "Rating", "Duration"],
                    "Value": [row['type'],
                              row['director'],
                              row['cast'],
                              row['country'],
                              row['release_year'],
                              row['rating'],
                              row['duration']]
                }
                movie_df = pd.DataFrame(data)

                # Display the movie details in a table
                st.table(movie_df)

                # Display the description below the table
                st.subheader("Description:")
                st.write(row['description'])
                st.write("---")  # Add a separator between movies
        else:
            st.write("No recommendations found based on your criteria.")

    # BACK BUTTON
    if st.button("Back"):
        # Redirect back to App 1
        st.query_params["app"] = ""  # Clear the query parameter to go back
