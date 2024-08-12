Welcome to my final project!!!
1. I use the python==3.10.12 version, and these dependencies are needed to download to run my code: 
    pandas==2.1.3
    kaggle==1.5.16
    matplotlib==3.7.1
    seaborn==0.12.2
2. There are two folders of my dataset: The first one is the raw folder, where the original datasets from Kaggle,     east_asia_top_artists.csv and east_asia_top_tracks.csv, are stored. The second one is the processed folder, where the processed and cleaned data is stored, likely in JSON format. It also contains two file: cleaned_artists.json and analysis_artists.json.
3. There are four python files in src folder: get_data.py (you should run this first), clean_data.py, run_analysis.py and visualize_results.py.
4. There are a few points that you need to pay attention to:
   i. Make sure all dependencies are installed with the correct versions in your Python environment.
   ii. Download the datasets from Kaggle using the Kaggle API and save them in the raw data folder.
   iii. Execute the Python scripts that perform data cleaning, processing, and analysis. These scripts read the raw data, perform the necessary transformations, and save the output to the processed data folder.
