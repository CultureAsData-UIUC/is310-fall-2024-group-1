import pandas as pd

def validate_data(file_path):
    # Load the dataset
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return

    # Check for missing values
    print("Missing Values:")
    print(df.isnull().sum())

    # Validate data types
    print("\nData Types:")
    print(df.dtypes)

    # Check for unexpected values
    if 'OPERABILITY_STATUS' in df.columns:
        print("\nUnique values in 'OPERABILITY_STATUS':")
        print(df['OPERABILITY_STATUS'].unique())

    if 'GENDER' in df.columns:
        print("\nUnique values in 'GENDER':")
        print(df['GENDER'].unique())

    # Check numeric ranges
    if 'NO_OF_SKINTONES' in df.columns:
        print("\nRange of 'NO_OF_SKINTONES':")
        print(df['NO_OF_SKINTONES'].min(), "-", df['NO_OF_SKINTONES'].max())

    if 'YOR' in df.columns:
        print("\nRange of 'YOR':")
        print(df['YOR'].min(), "-", df['YOR'].max())

if __name__ == "__main__":
    validate_data("cleaned_dress_up_games.csv")
