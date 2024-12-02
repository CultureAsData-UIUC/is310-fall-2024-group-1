import pandas as pd
import logging

# Configure logging
logging.basicConfig(filename='clean_dress_up_games.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def standardize_gender(gender):
    if pd.isna(gender):
        return 'Unknown'
    gender = gender.replace(',', '/').replace(' ', '').upper()
    if gender in ['M', 'F', 'M/F']:
        return gender
    return 'Other'

def standardize_operability(status):
    if pd.isna(status):
        return 'Unknown'
    status = status.lower()
    if 'operable' in status and 'non-operable' not in status:
        return 'Operable'
    elif 'non-operable' in status:
        return 'Non-operable'
    elif 'partially operable' in status:
        return 'Partially Operable'
    else:
        return 'Unknown'

def clean_game_link(link):
    if isinstance(link, str):
        return link.strip()
    return link

def main():
    try:
        # Load the dataset with the correct delimiter
        df = pd.read_csv('dress_up_games.csv', delimiter=',')
        logging.info("Loaded 'dress_up_games.csv' successfully.")
        print("Columns Detected:", df.columns)  # Debugging line to check column names
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
    df.columns = [col.strip().upper().replace(' ', '_').replace('.', '') for col in df.columns]
    logging.info("Standardized column names.")

    # Handle Missing Values
    df['DEVELOPER'] = df['DEVELOPER'].fillna('Unknown')
    df['PUBLISHER'] = df['PUBLISHER'].fillna('Unknown')
    logging.info("Filled missing values in 'DEVELOPER' and 'PUBLISHER'.")

    # Standardize 'GENDER'
    df['GENDER'] = df['GENDER'].apply(standardize_gender)
    logging.info("Standardized 'GENDER' column.")

    # Handle 'NO_OF_SKINTONES'
    df['NO_OF_SKINTONES'] = pd.to_numeric(df['NO_OF_SKINTONES'], errors='coerce').fillna(0).astype(int)
    logging.info("Converted 'NO_OF_SKINTONES' to numeric.")

    # Clean 'GAME_LINK'
    if 'GAME_LINK' in df.columns:
        df['GAME_LINK'] = df['GAME_LINK'].apply(clean_game_link)
        logging.info("Cleaned 'GAME_LINK' column.")
    else:
        logging.warning("'GAME_LINK' column not found in dataset.")

    # Standardize 'OPERABILITY_STATUS'
    if 'OPERABILITY_STATUS' in df.columns:
        df['OPERABILITY_STATUS'] = df['OPERABILITY_STATUS'].apply(standardize_operability)
        logging.info("Standardized 'OPERABILITY_STATUS' column.")
    else:
        logging.warning("'OPERABILITY_STATUS' column not found in dataset.")

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






