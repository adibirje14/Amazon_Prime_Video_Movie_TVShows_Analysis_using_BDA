# dashboard.py

import streamlit as st
import pandas as pd
from footer import display_footer
from visualization import (
    plot_movies_vs_tvshows,
    plot_distribution_of_ratings,
    plot_titles_per_year,
    plot_titles_per_decade,
    plot_top_genres,
    plot_genre_distribution,
    plot_genre_distribution_post_2000,
    plot_movie_duration_distribution,
    plot_top_countries,
    plot_top_directors,
    plot_top_actors,
    plot_tv_show_durations,
    plot_movies_by_duration_group,
    plot_word_cloud
)

# Load your dataset
data = pd.read_csv(r'amazon_prime_titles.csv')

# Set the title for the dashboard
st.title("Amazon Prime Video Insights Dashboard")

# Set a default selection to show the introduction
selection = "Introduction"

# Sidebar for navigation using buttons
st.sidebar.image(r'Prime video logo.png', width=150)
st.sidebar.header("Navigation")

options = [
    "Introduction",
    "Movies vs TV Shows",
    "Distribution of Ratings",
    "Titles Released per Year",
    "Titles Released per Decade",
    "Top Genres",
    "Genre Distribution",
    "Genre Distribution (Post 2000)",
    "Movie Duration Distribution",
    "Top Countries",
    "Top Directors",
    "Top Actors",
    "TV Show Durations",
    "Movies by Duration",
    "Word Cloud"
]

# Create buttons for each option
for option in options:
    if st.sidebar.button(option):
        selection = option

# Create a horizontal navbar for Movie Recommendation
st.markdown("---")  # Add a horizontal line for separation
if st.button("Get Recommendation"):
    # Redirect to app2
    st.query_params["app"] = "recommendation"  # Set a query parameter

# Display the Introduction by default
if selection == "Introduction":
    st.markdown("""### Project Introduction

Welcome to the **Amazon Prime Video Insights Dashboard**! This interactive dashboard provides comprehensive insights into Amazon Prime Video's extensive content library. 

Using this dashboard, you can explore various aspects of the dataset, including:
- **Distribution of Ratings:** Understand how titles are rated across the platform.
- **Titles Released Over the Years:** Track the trends in content availability over time.
- **Most Popular Genres:** Identify which genres are most prevalent and popular among viewers.

#### Technologies Used
This project is built using the following technologies:
- **Streamlit:** A powerful framework for creating interactive web applications with Python, allowing for real-time data visualization.
- **Pandas:** A library for data manipulation and analysis, which makes it easy to handle and preprocess the dataset.
- **Matplotlib & Seaborn:** Libraries for creating visually appealing plots and charts that enhance data understanding.
- **WordCloud:** A specialized library for generating word clouds from text data, providing a visual representation of keyword frequency.

#### Dataset
The dataset utilized in this project is sourced from **Kaggle**, featuring detailed information on Amazon Prime Video titles, including attributes such as ratings, genres, release years, and descriptions.

Feel free to navigate through the dashboard using the buttons on the left sidebar to uncover fascinating insights about Amazon Prime Video!
    """)

# Create an expander for guidelines
with st.expander("View Guidelines", expanded=True):
    st.markdown("""### Guidelines for Using the Navigation Buttons
- Use the buttons in the sidebar to select different visualizations.
- Each button corresponds to a specific analysis of the dataset.
- Click on any button to view the respective visualization.
- To go back, simply click another button or refresh the page.
""")

# Define a function to display the selected visualization
def display_visualization(selection):
    if selection == "Movies vs TV Shows":
        st.header("Number of Movies vs TV Shows")
        st.pyplot(plot_movies_vs_tvshows(data))
    elif selection == "Distribution of Ratings":
        st.header("Distribution of Ratings")
        st.pyplot(plot_distribution_of_ratings(data))
    elif selection == "Titles Released per Year":
        st.header("Number of Titles Released Each Year")
        st.pyplot(plot_titles_per_year(data))
    elif selection == "Titles Released per Decade":
        st.header("Number of Titles Released Each Decade")
        st.pyplot(plot_titles_per_decade(data))
    elif selection == "Top Genres":
        st.header("Top 10 Genres on Amazon Prime")
        st.pyplot(plot_top_genres(data))
    elif selection == "Genre Distribution":
        st.header("Distribution of Genres Across Release Years")
        genre_distribution = data['listed_in'].str.get_dummies(sep=', ').groupby(data['release_year']).sum()
        st.pyplot(plot_genre_distribution(genre_distribution))
    elif selection == "Genre Distribution (Post 2000)":
        st.header("Distribution of Genres Across Release Years (2000 and Onwards)")
        st.pyplot(plot_genre_distribution_post_2000(data))
    elif selection == "Movie Duration Distribution":
        st.header("Distribution of Duration for Movies")
        st.pyplot(plot_movie_duration_distribution(data))
    elif selection == "Top Countries":
        st.header("Top 10 Countries by Number of Titles on Amazon Prime")
        st.pyplot(plot_top_countries(data))
    elif selection == "Top Directors":
        st.header("Top 10 Directors by Number of Titles on Amazon Prime")
        st.pyplot(plot_top_directors(data))
    elif selection == "Top Actors":
        st.header("Top 10 Actors on Amazon Prime")
        st.pyplot(plot_top_actors(data))
    elif selection == "TV Show Durations":
        st.header("TV Show Durations")
        st.pyplot(plot_tv_show_durations(data))
    elif selection == "Movies by Duration":
        st.header("Number of Movies by Duration")
        st.pyplot(plot_movies_by_duration_group(data))
    elif selection == "Word Cloud":  # Handle Word Cloud visualization
        st.header("Word Cloud of Descriptions")
        st.pyplot(plot_word_cloud(data))

# Display the selected visualization if one was clicked
if selection != "Introduction":
    display_visualization(selection)

display_footer()

# Check if the app query parameter is set
if st.query_params.get("app") == "recommendation":
    import recommend  # Ensure that recommend.py is in the same directory
    recommend.run()  # Call the run function in recommend.py  
