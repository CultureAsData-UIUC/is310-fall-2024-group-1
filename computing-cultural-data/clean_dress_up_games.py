import pandas as pd
import logging

# Configure logging
logging.basicConfig(
    filename='clean_dress_up_games.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

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

def main():
    try:
        # Load the dataset with enhanced parameters
        df = pd.read_csv(
            'dress_up_games.csv',
            delimiter=',',
            quotechar='"',
            escapechar='\\',
            encoding='utf-8-sig',  # Handles BOM if present
            engine='python',       # Python engine for better handling
            on_bad_lines='warn'    # Warn about bad lines without stopping
        )
        logging.info("Loaded 'dress_up_games.csv' successfully.")
    except FileNotFoundError:
        logging.error("File 'dress_up_games.csv' not found.")
        print("File 'dress_up_games.csv' not found.")
        return
    except Exception as e:
        logging.error(f"Error loading CSV: {e}")
        print(f"Error loading CSV: {e}")
        return

    # Display initial data info
    print("Initial Data Info:")
    print(df.info())
    print("\nInitial Data Sample:")
    print(df.head())

    # Print columns to verify
    print("\nColumns in DataFrame:")
    print(df.columns.tolist())

    # Standardize Column Names
    df.columns = [col.strip().upper().replace(' ', '_') for col in df.columns]
    logging.info("Standardized column names.")

    # Print standardized columns
    print("\nStandardized Columns:")
    print(df.columns.tolist())

    # Verify if expected columns exist
    expected_columns = [
        'GAME_NAME',
        'YOR',
        'OPERABILITY_STATUS',
        'DEVELOPER',
        'PUBLISHER',
        'GENDER',
        'NO_OF_SKINTONES',
        'GAME_LINK'  # Ensure this matches your CSV
    ]
    missing_columns = [col for col in expected_columns if col not in df.columns]
    if missing_columns:
        logging.error(f"Missing columns after parsing: {missing_columns}")
        print(f"Missing columns: {missing_columns}")
        return
    else:
        logging.info("All expected columns are present.")

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

    # Standardize 'OPERABILITY_STATUS'
    df['OPERABILITY_STATUS'] = df['OPERABILITY_STATUS'].apply(standardize_operability)
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
        print(f"Error saving cleaned CSV: {e}")

if __name__ == "__main__":
    main()





