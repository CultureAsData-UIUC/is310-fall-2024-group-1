"""
Fetch Dress-Up Games from Flashpoint Archive

This script fetches dress-up games from the Flashpoint Archive API, filters out NSFW content,
and saves the data to CSV and Excel files.

Usage:
    python fetch_dress_up_games.py

Requirements:
    - requests
    - pandas
    - python-dotenv
    - openpyxl
"""

import requests
import pandas as pd
import os
import time
from dotenv import load_dotenv
import logging

# Load environment variables from a .env file
load_dotenv()

# Configuration
API_KEY = os.getenv('FLASHPOINT_API_KEY')  # Ensure this is set in your .env file
API_URL = "https://api.flashpointarchive.org/v1/games"  # Example endpoint; verify with actual API documentation
OUTPUT_CSV = "dress_up_games.csv"
OUTPUT_EXCEL = "dress_up_games.xlsx"
PAGE_SIZE = 100  # Number of records per API call
MAX_RETRIES = 5
SLEEP_TIME = 2  # Seconds between retries to respect rate limits

# Setup logging
logging.basicConfig(
    filename='fetch_dress_up_games.log',
    filemode='w',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def fetch_games(page, page_size):
    """
    Fetch games from the Flashpoint API.

    Args:
        page (int): Page number for pagination.
        page_size (int): Number of records per page.

    Returns:
        dict: JSON response from the API or None if an error occurs.
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}"  # Adjust based on API requirements
    }
    params = {
        "category": "dress-up",
        "page": page,
        "page_size": page_size
    }
    try:
        response = requests.get(API_URL, headers=headers, params=params)
        response.raise_for_status()
        logging.info(f"Successfully fetched page {page}")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed for page {page}: {e}")
        return None

def is_nsfw(game):
    """
    Determine if a game is NSFW based on its description.

    Args:
        game (dict): Game data.

    Returns:
        bool: True if NSFW, False otherwise.
    """
    nsfw_keywords = ['nsfw', 'explicit', 'adult', 'violence', 'blood', 'gore', 'sexual', 'mature', 'graphic', 'offensive']
    description = game.get('description', '').lower()
    return any(keyword in description for keyword in nsfw_keywords)

def main():
    """
    Main function to fetch, filter, and save dress-up games data.
    """
    if not API_KEY:
        logging.error("FLASHPOINT_API_KEY is not set. Please set it in the .env file.")
        print("Error: FLASHPOINT_API_KEY is not set. Please set it in the .env file.")
        return

    all_games = []
    page = 1

    while True:
        print(f"Fetching page {page}...")
        data = fetch_games(page, PAGE_SIZE)
        if not data:
            print(f"Failed to fetch data for page {page}. Exiting.")
            break

        games = data.get('results', [])
        if not games:
            print("No more games found. Finishing fetch.")
            break

        for game in games:
            if not is_nsfw(game):
                all_games.append({
                    'id': game.get('id'),
                    'title': game.get('title'),
                    'description': game.get('description'),
                    'year_of_release': game.get('year_of_release'),
                    'number_of_skin_tones': game.get('number_of_skin_tones'),
                    'operability_status': game.get('operability_status'),
                    'developer': game.get('developer'),
                    'publisher': game.get('publisher'),
                    'gender_options': game.get('gender_options'),
                    'game_link': game.get('game_link')
                })
            else:
                logging.info(f"Excluded NSFW game: {game.get('title')}")

        page += 1
        time.sleep(SLEEP_TIME)  # Respect API rate limits

    # Convert to DataFrame
    df = pd.DataFrame(all_games)

    if not df.empty:
        # Save to CSV
        df.to_csv(OUTPUT_CSV, index=False)
        logging.info(f"Saved {len(df)} games to {OUTPUT_CSV}")
        print(f"Saved {len(df)} games to {OUTPUT_CSV}")

        # Save to Excel
        df.to_excel(OUTPUT_EXCEL, index=False)
        logging.info(f"Saved {len(df)} games to {OUTPUT_EXCEL}")
        print(f"Saved {len(df)} games to {OUTPUT_EXCEL}")
    else:
        logging.warning("No games fetched to save.")
        print("No games fetched to save.")

if __name__ == "__main__":
    main()

