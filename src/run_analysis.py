import pandas as pd
import json
import os

def load_top_50_tracks(file_path):

    with open(file_path, 'r') as file:
        data = json.load(file)
    df = pd.DataFrame(data)
    return df.sort_values(by='top_track_popularity', ascending=False).head(50)

def count_genre_occurrences(df, genre):

    return len(df[df['genres'].str.contains(genre, case=False, na=False)])

def standardize_genres(df):
    df['genres'] = df['genres'].str.lower()
    df.loc[df['genres'].str.contains('k-pop', na=False), 'genres'] = 'k-pop'
    df.loc[df['genres'].str.contains('j-pop', na=False), 'genres'] = 'j-pop'
    return df

def save_data_as_json(df, file_path):
    df.to_json(file_path, orient='records', indent=4)

def run_analysis(file_path):
    top_50 = load_top_50_tracks(file_path)

    standardized_top_50 = standardize_genres(top_50)

    kpop_count = count_genre_occurrences(standardized_top_50, 'k-pop')
    jpop_count = count_genre_occurrences(standardized_top_50, 'j-pop')
    other_count = len(standardized_top_50[(standardized_top_50['genres'] != 'k-pop') & (standardized_top_50['genres'] != 'j-pop')])

    summary = pd.DataFrame({
        "Genre": ["K-pop", "J-pop", "Others"],
        "Count": [kpop_count, jpop_count, other_count]
    })

    return summary, standardized_top_50

if __name__ == '__main__':
    top_tracks_path = './data/processed/cleaned_artists.json'
    processed_data_dir = './data/processed'
    analysis_file_path = os.path.join(processed_data_dir, 'analysis_artists.json')

    summary, analyzed_data = run_analysis(top_tracks_path)

    save_data_as_json(analyzed_data, analysis_file_path)
