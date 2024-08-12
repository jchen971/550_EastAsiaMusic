import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_top_50_tracks(file_path):
    df = pd.read_csv(file_path)
    return df.sort_values(by='top_track_popularity', ascending=False).head(50)

def plot_genre_count(df):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, y='genres')
    plt.xlabel('Count')
    plt.ylabel('Genres')
    plt.title('Count of Genres')
    plt.show()

def plot_followers_vs_popularity(df):
    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=df, x='followers', y='top_track_popularity', hue='genres')
    plt.title('Artist Followers and Top Track Popularity')
    plt.xlabel('Followers')
    plt.ylabel('Top Track Popularity')
    plt.show()

def run_analysis(file_path):
    top_50 = load_top_50_tracks(file_path)

    plot_genre_count(top_50)
    plot_followers_vs_popularity(top_50)

if __name__ == '__main__':
    top_tracks_path = './data/processed/cleaned_artists.csv'
    
    run_analysis(top_tracks_path)
