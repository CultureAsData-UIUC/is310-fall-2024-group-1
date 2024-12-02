import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(file_path):
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return

    # Plot number of games released by year
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='YOR', palette='viridis')
    plt.title('Number of Dress-Up Games Released by Year')
    plt.xlabel('Year of Release')
    plt.ylabel('Number of Games')
    plt.xticks(rotation=45)
    plt.show()

    # Plot distribution of skin tones
    if 'NO_OF_SKINTONES' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(df['NO_OF_SKINTONES'], bins=10, kde=True, color='blue')
        plt.title('Distribution of Skin Tones in Dress-Up Games')
        plt.xlabel('Number of Skin Tones')
        plt.ylabel('Frequency')
        plt.show()

if __name__ == "__main__":
    visualize_data("cleaned_dress_up_games.csv")
