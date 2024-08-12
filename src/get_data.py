!pip install kaggle
import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_kaggle_dataset(username, key, dataset_path, save_path):
    os.environ['KAGGLE_USERNAME'] = username
    os.environ['KAGGLE_KEY'] = key
  
    api = KaggleApi()
    api.authenticate()

    os.makedirs(save_path, exist_ok=True)

    for file_name in file_names:
        api.dataset_download_file(dataset_path, file_name, path=save_path)


if __name__ == '__main__':
    KAGGLE_USERNAME = 'janejing'
    KAGGLE_KEY = '27d2b3c50b39b9da42f5083bcfe02898'
    KAGGLE_DATASET_PATH = 'crxxom/spotify-popular-east-asian-artists-and-tracks'
    CSV_FILE_PATH = './data/raw'
    FILES_TO_DOWNLOAD = ['east_asia_top_artists.csv', 'east_asia_top_tracks.csv']

    download_kaggle_dataset_files(KAGGLE_USERNAME, KAGGLE_KEY, KAGGLE_DATASET_PATH, CSV_FILE_PATH, FILES_TO_DOWNLOAD)
