import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('dress_up_games.csv', delimiter='\t')  # Assuming tab-separated based on your data

# Display initial data info
print("Initial Data Info:")
print(df.info())
print("\nInitial Data Sample:")
print(df.head())

# Standardize Column Names
df.columns = [col.strip().upper().replace(' ', '_').replace('.', '') for col in df.columns]

# Handle Missing Values
# For 'DEVELOPER' and 'PUBLISHER', fill missing with 'Unknown'
df['DEVELOPER'] = df['DEVELOPER'].fillna('Unknown')
df['PUBLISHER'] = df['PUBLISHER'].fillna('Unknown')

# For 'GENDER', standardize entries
def standardize_gender(gender):
    if pd.isna(gender):
        return 'Unknown'
    gender = gender.replace(',', '/').replace(' ', '').upper()
    if gender in ['M', 'F', 'M/F']:
        return gender
    return 'Other'

df['GENDER'] = df['GENDER'].apply(standardize_gender)

# For 'NO_OF_SKINTONES', handle 'n/a' and convert to numeric
df['NO_OF_SKINTONES'] = pd.to_numeric(df['NO_OF_SKINTONES'], errors='coerce').fillna(0).astype(int)

# Clean 'GAME_LINK' - ensure URLs are valid (basic check)
df['GAME_LINK'] = df['GAME_LINK'].apply(lambda x: x.strip() if isinstance(x, str) else x)

# Handle 'OPERABILITY_STATUS' - standardize entries
def standardize_operability(status):
    if pd.isna(status):
        return 'Unknown'
    status = status.lower()
    if 'operable' in status:
        return 'Operable'
    elif 'non-operable' in status or 'non-operable' in status:
        return 'Non-operable'
    elif 'partially operable' in status:
        return 'Partially Operable'
    else:
        return 'Unknown'

df['OPERABILITY_STATUS'] = df['OPERABILITY_STATUS'].apply(standardize_operability)

# Convert 'YOR' to integer
df['YOR'] = pd.to_numeric(df['YOR'], errors='coerce').fillna(0).astype(int)

# Remove duplicate entries based on 'GAME_NAME' and 'YOR'
df = df.drop_duplicates(subset=['GAME_NAME', 'YOR'])

# Reset index
df.reset_index(drop=True, inplace=True)

# Display cleaned data info
print("\nCleaned Data Info:")
print(df.info())
print("\nCleaned Data Sample:")
print(df.head())

# Save the cleaned dataset
df.to_csv('cleaned_dress_up_games.csv', index=False)
print("\nCleaned data saved to 'cleaned_dress_up_games.csv'")





