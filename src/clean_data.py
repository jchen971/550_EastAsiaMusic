import pandas as pd
import json
import os

def load_and_clean_csv_data(artist_path, columns):
    df_artists = pd.read_csv(artist_path)

    df_artists_filtered = df_artists[columns]

    df_artists_cleaned = df_artists_filtered.dropna()

    cleaned_data = df_artists_cleaned.to_dict(orient='records')

    return cleaned_data

def save_data_as_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    raw_data_dir = './data/raw'
    processed_data_dir = './data/processed'
    os.makedirs(processed_data_dir, exist_ok=True)

    top_artists_path = os.path.join(raw_data_dir, 'east_asia_top_artists.csv')
    processed_file_path = os.path.join(processed_data_dir, 'cleaned_artists.json')

    updated_top_artists_columns = ['artist_name', 'followers', 'top_track', 
                                   'top_track_popularity', 'top_track_release_date', 
                                   'genres', 'query_genre']

    cleaned_data = load_and_clean_csv_data(top_artists_path, updated_top_artists_columns)

    save_data_as_json(cleaned_data, processed_file_path)

if __name__ == '__main__':
    main()
