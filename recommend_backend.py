# recommend_backend.py

import pandas as pd

class RecommendationSystem:
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)

    def filter_movies(self, genre, year_start, year_end, type_, duration_range):
        # Filter based on genre
        if genre != "All":
            filtered_data = self.data[self.data['listed_in'].str.contains(genre, case=False, na=False)]
        else:
            filtered_data = self.data

        # Filter based on release year range
        filtered_data = filtered_data[(filtered_data['release_year'] >= year_start) & (filtered_data['release_year'] <= year_end)]

        # Filter based on type
        if type_ != "All":
            filtered_data = filtered_data[filtered_data['type'] == type_]

        # Convert 'duration' to numeric values
        def convert_duration(duration):
            if 'min' in duration:  # For movies
                return pd.to_numeric(duration.replace(' min', '').strip(), errors='coerce')
            elif 'Season' in duration:  # For shows
                season_count = pd.to_numeric(duration.replace(' Season', '').strip(), errors='coerce')
                return season_count * 360  # 1 season = 360 minutes
            return None  # For any unexpected format

        filtered_data['duration'] = filtered_data['duration'].apply(convert_duration)

        # Filter based on duration range
        if duration_range[0] is not None and duration_range[1] is not None:
            filtered_data = filtered_data[(filtered_data['duration'] >= duration_range[0]) & (filtered_data['duration'] <= duration_range[1])]

        return filtered_data

    def get_recommendations(self, genre, year_start, year_end, type_, duration_range):
        filtered_movies = self.filter_movies(genre, year_start, year_end, type_, duration_range)
        return filtered_movies.head(10)  # Return top 10 recommendations