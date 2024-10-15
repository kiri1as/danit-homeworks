import kaggle

if __name__ == "__main__":
    kaggle.api.dataset_download_files('heptapod/titanic', path='titanic', unzip=True)
