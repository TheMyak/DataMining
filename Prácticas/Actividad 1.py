import kaggle
import os

# DataSet URL: https://www.kaggle.com/datasets/brenda89/fifa-world-cup-2022

def get_csv_kaggle ():
  kaggle.api.authenticate()
  kaggle.api.dataset_download_files('brenda89/fifa-world-cup-2022', path=os.path.join(os.getcwd(), "DataSet"), unzip=True)

get_csv_kaggle()