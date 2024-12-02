import pandas as pd
import logging

# Configure logging
logging.basicConfig(filename='clean_dress_up_games.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Main Script
def main():
    try:
        # Load the dataset with the correct delimiter
        df = pd.read_csv('dress_up_games.csv', delimiter=',', header=0)  # Explicitly use comma as delimiter
        logging.info("Loaded 'dress_up_games.csv' successfully.")
    except FileNotFoundError:
        logging.error("File 'dress_up_games.csv' not found.")
        return
    except Exception as e:
        logging.error(f"Error loading CSV: {e}")
        return

    # Display initial data info
    print("Initial Data Info:")
    print(df.info())
    print("\nInitial Data Sample:")
    print(df.head())

    # Standardize Column Names
    df.columns = [col.strip().upper().replace(' ', '_') for col in df.columns]
    logging.info("Standardized column names.")

    # Handle Missing Values
    df['DEVELOPER'] = df['DEVELOPER'].fillna('Unknown')
    df['PUBLISHER'] = df['PUBLISHER'].fillna('Unknown')
    logging.info("Filled missing values in 'DEVELOPER' and 'PUBLISHER'.")

    # Standardize 'GENDER'
    df['GENDER'] = df['GENDER'].apply(lambda x: x.strip().upper() if pd.notna(x) else 'Unknown')
    logging.info("Standardized 'GENDER' column.")

    # Handle 'NO_OF_SKINTONES'
    df['NO_OF_SKINTONES'] = pd.to_numeric(df['NO_OF_SKINTONES'], errors='coerce').fillna(0).astype(int)
    logging.info("Converted 'NO_OF_SKINTONES' to numeric.")

    # Standardize 'OPERABILITY_STATUS'
    df['OPERABILITY_STATUS'] = df['OPERABILITY_STATUS'].str.lower().replace({
        'non-operable': 'Non-operable',
        'operable': 'Operable',
        'partially operable': 'Partially Operable'
    }).fillna('Unknown')
    logging.info("Standardized 'OPERABILITY_STATUS' column.")

    # Convert 'YOR' to integer
    df['YOR'] = pd.to_numeric(df['YOR'], errors='coerce').fillna(0).astype(int)
    logging.info("Converted 'YOR' to integer.")

    # Remove duplicate entries based on 'GAME_NAME' and 'YOR'
    before_dedup = len(df)
    df = df.drop_duplicates(subset=['GAME_NAME', 'YOR'])
    after_dedup = len(df)
    logging.info(f"Removed duplicates: {before_dedup - after_dedup} entries dropped.")

    # Reset index
    df.reset_index(drop=True, inplace=True)

    # Display cleaned data info
    print("\nCleaned Data Info:")
    print(df.info())
    print("\nCleaned Data Sample:")
    print(df.head())

    # Save the cleaned dataset
    try:
        df.to_csv('cleaned_dress_up_games.csv', index=False)
        logging.info("Cleaned data saved to 'cleaned_dress_up_games.csv'.")
        print("\nCleaned data saved to 'cleaned_dress_up_games.csv'")
    except Exception as e:
        logging.error(f"Error saving cleaned CSV: {e}")

if __name__ == "__main__":
    main()


