import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns
from wordcloud import WordCloud

# visualizations.py

# visualizations.py

def plot_movies_vs_tvshows(data):
    # Set figure size
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the count of Movies vs TV Shows
    sns.countplot(data=data, x='type', order=data['type'].value_counts().index, ax=ax)

    # Set the title and labels
    ax.set_title('Number of Movies vs TV Shows')
    ax.set_xlabel('Type')
    ax.set_ylabel('Count')

    # Return the figure for Streamlit
    return fig


def plot_distribution_of_ratings(data):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(data=data, x='rating', order=data['rating'].value_counts().index, ax=ax)
    ax.set_title('Distribution of Ratings')
    plt.xticks(rotation=45)
    return fig

def plot_titles_per_year(data):
    # Set figure size
    fig, ax = plt.subplots(figsize=(20, 8))

    # Plot the count of titles per year
    sns.countplot(data=data, x='release_year', order=data['release_year'].value_counts().index, ax=ax)

    # Set the title and labels
    ax.set_title('Number of Titles Released Each Year')
    ax.set_xlabel('Release Year')
    ax.set_ylabel('Count')

    # Rotate x-ticks
    plt.xticks(rotation=90, fontsize=10)

    # Return the figure for Streamlit display
    return fig

# 1. Titles Released per Decade
def plot_titles_per_decade(data):
    data['decade'] = (data['release_year'] // 10) * 10
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.countplot(data=data, x='decade', order=data['decade'].value_counts().index, ax=ax)
    ax.set_title('Number of Titles Released Each Decade')
    plt.xticks(rotation=45)
    return fig

# 2. Top 10 Genres on Amazon Prime
def plot_top_genres(data):
    all_genres = data['listed_in'].str.split(',').apply(lambda x: [genre.strip() for genre in x]).explode()
    genre_counts = Counter(all_genres)
    top_genres = genre_counts.most_common(10)
    genres, counts = zip(*top_genres)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=list(genres), y=list(counts), ax=ax)
    ax.set_title('Top 10 Genres on Amazon Prime')
    plt.xticks(rotation=45)
    return fig

# 3. Distribution of Genres Across Release Years
def plot_genre_distribution(genre_distribution):
    fig, ax = plt.subplots(figsize=(12, 6))
    genre_distribution.plot(kind='area', figsize=(12, 6), alpha=0.5, colormap='viridis', ax=ax)
    ax.set_title('Distribution of Genres Across Release Years')
    ax.set_xlabel('Release Year')
    ax.set_ylabel('Count of Genres')
    plt.xticks(rotation=45)
    plt.legend(title='Genres', bbox_to_anchor=(1.05, 1), loc='upper left')
    return fig

# 4. Distribution of Genres from 2000 Onwards
def plot_genre_distribution_post_2000(data):
    filtered_data = data[data['release_year'] >= 2000]
    genre_distribution = filtered_data['listed_in'].str.get_dummies(sep=', ').groupby(filtered_data['release_year']).sum()
    fig, ax = plt.subplots(figsize=(12, 6))
    genre_distribution.plot(kind='area', alpha=0.5, colormap='viridis', ax=ax)
    ax.set_title('Distribution of Genres Across Release Years (2000 and Onwards)')
    ax.set_xlabel('Release Year')
    ax.set_ylabel('Count of Genres')
    plt.xticks(rotation=45)
    plt.legend(title='Genres', bbox_to_anchor=(1.05, 1), loc='upper left')
    return fig

# 5. Distribution of Movie Durations
def plot_movie_duration_distribution(data):
    movies_data = data[data['type'] == 'Movie']
    movies_data['duration'] = movies_data['duration'].str.extract(r'(\d+)').astype(int)
    movies_data = movies_data[movies_data['duration'] <= 200]
    bin_edges = range(0, 220, 20)
    movies_data['duration_bins'] = pd.cut(movies_data['duration'], bins=bin_edges)
    labels = [f"{i}-{i+19}" for i in bin_edges[:-1]]
    fig, ax = plt.subplots(figsize=(12, 6))
    movies_data['duration_bins'].value_counts().sort_index().plot(kind='bar', color='skyblue', edgecolor='black', ax=ax)
    plt.xticks(ticks=range(len(labels)), labels=labels, rotation=45)
    ax.set_title('Distribution of Duration for Movies (20-Minute Intervals)')
    ax.set_xlabel('Duration (minutes)')
    ax.set_ylabel('Number of Movies')
    plt.grid(axis='y', alpha=0.75)
    return fig

# 6. Top 10 Countries by Number of Titles
def plot_top_countries(data):
    # Fill NaN values with "Unknown" and then process
    country_counts = (
        data['country']
        .fillna('Unknown')  # Fill NaN values with "Unknown"
        .str.split(',')
        .apply(lambda x: [country.strip() for country in x])  # Strip whitespace
        .explode()
        .value_counts()
    )
    
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=country_counts.index[:10], y=country_counts.values[:10], ax=ax)
    ax.set_title('Top 10 Countries by Number of Titles on Amazon Prime')
    plt.xticks(rotation=45)
    return fig

# 7. Top 10 Directors
def plot_top_directors(data):
    director_counts = data['director'].value_counts()
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=director_counts.index[:10], y=director_counts.values[:10], ax=ax)
    ax.set_title('Top 10 Directors by Number of Titles on Amazon Prime')
    plt.xticks(rotation=45)
    return fig

# 8. Top 10 Actors
def plot_top_actors(data):
    # Replace NaN values with "Unknown" and then process
    all_actors = (
        data['cast']
        .fillna('Unknown')  # Fill NaN values with "Unknown"
        .str.split(',')
        .apply(lambda x: [actor.strip() for actor in x])  # Strip whitespace
        .explode()
    )
    
    actor_counts = Counter(all_actors)
    top_actors = actor_counts.most_common(10)

    if top_actors:  # Check if there are any actors found
        actors, counts = zip(*top_actors)
    else:
        actors, counts = [], []

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=list(actors), y=list(counts), ax=ax)
    ax.set_title('Top 10 Actors on Amazon Prime')
    plt.xticks(rotation=45)
    return fig

# 9. TV Show Durations
def plot_tv_show_durations(data):
    tv_shows = data[data['type'] == 'TV Show']
    tv_shows_no_nan = tv_shows.dropna(subset=['duration'])
    duration_counts = tv_shows_no_nan['duration'].value_counts()
    fig, ax = plt.subplots(figsize=(10, 6))
    duration_counts.plot(kind='bar', color='blue', ax=ax)
    ax.set_title('TV Show Durations')
    ax.set_xlabel('Duration')
    ax.set_ylabel('Number of TV Shows')
    plt.xticks(rotation=90)
    return fig

# 10. Movies by Duration
def plot_movies_by_duration_group(data):
    movies = data[data['type'] == 'Movie'].copy()
    movies = movies.dropna(subset=['duration'])
    movies['duration_minutes'] = movies['duration'].str.extract(r'(\d+)').astype(float)
    bins = [0, 60, 90, 120, 150, 180, 210, 240, 300]
    labels = ['0-60 min', '61-90 min', '91-120 min', '121-150 min', '151-180 min', '181-210 min', '211-240 min', '240+ min']
    movies['duration_group'] = pd.cut(movies['duration_minutes'], bins=bins, labels=labels, right=False)
    duration_group_counts = movies['duration_group'].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(duration_group_counts.index, duration_group_counts.values, color='blue', width=0.7)
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 5, int(yval), ha='center', va='bottom')
    ax.set_xlabel('Duration')
    ax.set_ylabel('Number of Movies')
    ax.set_title('Number of Movies by Duration')
    plt.xticks(rotation=90)
    plt.tight_layout()
    return fig

def plot_word_cloud(data):
    # Combine all descriptions into a single string
    text = ' '.join(data['description'].dropna())

    # Create a word cloud object
    wordcloud = WordCloud(width=800, height=400, background_color='white', max_words=200, colormap='viridis').generate(text)

    # Plot the word cloud
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')  # No axis labels
    plt.title('Word Cloud of Descriptions', fontsize=16)
    
    # Return the figure to display in Streamlit
    return plt


