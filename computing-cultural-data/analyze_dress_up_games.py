import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
try:
    df_games = pd.read_csv('dress_up_games.csv')
except FileNotFoundError:
    print("Error: The dataset 'dress_up_games.csv' was not found. Make sure the file is in the correct directory.")
    exit()

# Preview the dataset
print("First five rows of the dataset:")
print(df_games.head())

# Data Cleaning: Convert 'YOR' to numeric for analysis and handle missing values
df_games['YOR'] = pd.to_numeric(df_games['YOR'], errors='coerce')

# Drop rows with missing 'YOR' values, as these cannot be used for analysis
df_games = df_games.dropna(subset=['YOR'])

# Convert 'YOR' to integers after removing NaN values
df_games['YOR'] = df_games['YOR'].astype(int)

# Plot: Number of games released by year
plt.figure(figsize=(10, 6))
sns.countplot(data=df_games, x='YOR', palette='viridis', order=sorted(df_games['YOR'].unique()))
plt.title('Number of Dress-Up Games Released by Year')
plt.xlabel('Year of Release')
plt.ylabel('Number of Games')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Handle missing values in 'NO_OF_SKINTONES' by filling with 0 (assuming missing data implies no data available)
df_games['NO_OF_SKINTONES'] = pd.to_numeric(df_games['NO_OF_SKINTONES'], errors='coerce').fillna(0)

# Plot: Distribution of the number of skin tones available
plt.figure(figsize=(10, 6))
sns.histplot(df_games['NO_OF_SKINTONES'], bins=10, kde=True, color='blue')
plt.title('Distribution of Number of Skin Tones in Dress-Up Games')
plt.xlabel('Number of Skin Tones')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Analyze the evolution of skin tones pre- and post-2011
df_games['period'] = df_games['YOR'].apply(lambda x: 'pre-2011' if x < 2011 else 'post-2011')

plt.figure(figsize=(10, 6))
sns.boxplot(data=df_games, x='period', y='NO_OF_SKINTONES', palette='coolwarm')
plt.title('Number of Skin Tones in Dress-Up Games Pre- and Post-2011')
plt.xlabel('Period')
plt.ylabel('Number of Skin Tones')
plt.tight_layout()
plt.show()

# Save the processed dataset for future analysis
output_file = 'processed_dress_up_games.csv'
df_games.to_csv(output_file, index=False)
print(f"Processed dataset saved to '{output_file}'")
