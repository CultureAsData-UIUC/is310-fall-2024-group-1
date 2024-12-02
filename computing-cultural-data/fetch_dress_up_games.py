"""
Dataset Validation Script for Dress-Up Games

This script performs comprehensive validation checks on the 'cleaned_dress_up_games.csv' dataset.
It ensures data integrity by checking for missing values, correct data types, valid categorical values,
and other consistency checks. The results of the validation are logged and summarized in a report.

Usage:
    python validate_dress_up_games.py

Requirements:
    - pandas
    - numpy
    - python-dotenv (if using environment variables)
"""

import pandas as pd
import numpy as np
import logging
import sys
import os
from dotenv import load_dotenv

# Load environment variables from a .env file (if present)
load_dotenv()

# Configuration
DATA_FILE = "cleaned_dress_up_games.csv"  # Path to your cleaned dataset
REPORT_FILE = "validation_report.txt"     # Output report file
LOG_FILE = "validate_dress_up_games.log"  # Log file for detailed logs

# Setup logging
logging.basicConfig(
    filename=LOG_FILE,
    filemode='w',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def load_data(file_path):
    """
    Load the dataset into a pandas DataFrame.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        logging.info(f"Successfully loaded data from {file_path}")
        return df
    except FileNotFoundError:
        logging.error(f"File {file_path} not found.")
        sys.exit(f"Error: File {file_path} not found.")
    except pd.errors.EmptyDataError:
        logging.error(f"File {file_path} is empty.")
        sys.exit(f"Error: File {file_path} is empty.")
    except Exception as e:
        logging.error(f"An unexpected error occurred while loading data: {e}")
        sys.exit(f"Error: An unexpected error occurred while loading data: {e}")

def check_missing_values(df):
    """
    Check for missing values in the DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to check.

    Returns:
        pd.Series: Number of missing values per column.
    """
    missing = df.isnull().sum()
    logging.info("Missing Values Check Completed.")
    return missing

def check_data_types(df):
    """
    Verify that each column has the expected data type.

    Args:
        df (pd.DataFrame): The DataFrame to check.

    Returns:
        dict: Columns with unexpected data types.
    """
    expected_types = {
        'game_name': 'object',
        'YOR': 'int64',
        'operability_status': 'object',
        'DEVELOPER': 'object',
        'PUBLISHER': 'object',
        'GENDER': 'object',
        'NO_OF_SKINTONES': 'int64',
        'GAME_LINK': 'object'
    }
    
    type_mismatches = {}
    for column, expected in expected_types.items():
        if column not in df.columns:
            type_mismatches[column] = f"Missing column."
            logging.warning(f"Missing column: {column}")
            continue
        actual = df[column].dtype
        if actual != expected:
            type_mismatches[column] = f"Expected {expected}, but got {actual}"
            logging.warning(f"Data type mismatch in column '{column}': Expected {expected}, but got {actual}")
    
    logging.info("Data Types Check Completed.")
    return type_mismatches

def check_categorical_values(df):
    """
    Ensure that categorical columns contain only expected values.

    Args:
        df (pd.DataFrame): The DataFrame to check.

    Returns:
        dict: Columns with unexpected categorical values.
    """
    categorical_checks = {
        'operability_status': ['operable', 'non-operable', 'partially operable'],
        'GENDER': ['F', 'M', 'M/F', 'Non-binary', 'Other']  # Adjust based on your dataset
    }
    
    invalid_entries = {}
    for column, valid_values in categorical_checks.items():
        if column not in df.columns:
            invalid_entries[column] = f"Missing column."
            logging.warning(f"Missing column for categorical check: {column}")
            continue
        unique_values = df[column].dropna().unique().tolist()
        invalid = [val for val in unique_values if val not in valid_values]
        if invalid:
            invalid_entries[column] = invalid
            logging.warning(f"Invalid entries found in column '{column}': {invalid}")
    
    logging.info("Categorical Values Check Completed.")
    return invalid_entries

def check_url_validity(df):
    """
    Validate that GAME_LINK URLs are properly formatted.

    Args:
        df (pd.DataFrame): The DataFrame to check.

    Returns:
        list: Indices of rows with invalid URLs.
    """
    import re
    url_pattern = re.compile(
        r'^(https?://)'  # http:// or https://
        r'(\w+(\-\w+)*\.)+'  # Domain name
        r'([a-zA-Z]{2,})'  # Top-level domain
        r'(/[^\s]*)?$'  # Optional path
    )
    
    invalid_urls = df[~df['GAME_LINK'].astype(str).str.match(url_pattern)].index.tolist()
    if invalid_urls:
        logging.warning(f"Invalid URLs found at indices: {invalid_urls}")
    logging.info("URL Validity Check Completed.")
    return invalid_urls

def check_duplicates(df):
    """
    Check for duplicate rows in the DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to check.

    Returns:
        int: Number of duplicate rows.
    """
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        logging.warning(f"Found {duplicates} duplicate rows.")
    else:
        logging.info("No duplicate rows found.")
    return duplicates

def generate_report(missing, type_mismatches, categorical_invalid, invalid_urls, duplicates):
    """
    Generate a validation report summarizing all checks.

    Args:
        missing (pd.Series): Missing values per column.
        type_mismatches (dict): Data type mismatches.
        categorical_invalid (dict): Invalid categorical values.
        invalid_urls (list): Indices of rows with invalid URLs.
        duplicates (int): Number of duplicate rows.

    Returns:
        None
    """
    with open(REPORT_FILE, 'w') as f:
        f.write("=== Dataset Validation Report ===\n\n")
        
        f.write("1. Missing Values:\n")
        if missing.sum() == 0:
            f.write("   No missing values found.\n\n")
        else:
            f.write(missing[missing > 0].to_string())
            f.write("\n\n")
        
        f.write("2. Data Type Mismatches:\n")
        if not type_mismatches:
            f.write("   All columns have expected data types.\n\n")
        else:
            for column, issue in type_mismatches.items():
                f.write(f"   - {column}: {issue}\n")
            f.write("\n")
        
        f.write("3. Categorical Values Check:\n")
        if not categorical_invalid:
            f.write("   All categorical columns contain only expected values.\n\n")
        else:
            for column, invalids in categorical_invalid.items():
                f.write(f"   - {column}: Invalid entries -> {invalids}\n")
            f.write("\n")
        
        f.write("4. URL Validity:\n")
        if not invalid_urls:
            f.write("   All GAME_LINK URLs are valid.\n\n")
        else:
            f.write(f"   Invalid URLs found at row indices: {invalid_urls}\n\n")
        
        f.write("5. Duplicate Rows:\n")
        if duplicates == 0:
            f.write("   No duplicate rows found.\n\n")
        else:
            f.write(f"   Found {duplicates} duplicate rows.\n\n")
        
        f.write("=== End of Report ===\n")
    
    logging.info(f"Validation report generated at {REPORT_FILE}")

def main():
    """
    Main function to perform all validation checks and generate a report.
    """
    # Load data
    df = load_data(DATA_FILE)
    
    # Perform validation checks
    missing = check_missing_values(df)
    type_mismatches = check_data_types(df)
    categorical_invalid = check_categorical_values(df)
    invalid_urls = check_url_validity(df)
    duplicates = check_duplicates(df)
    
    # Generate validation report
    generate_report(missing, type_mismatches, categorical_invalid, invalid_urls, duplicates)
    
    print(f"Validation completed. Report saved to {REPORT_FILE}")
    logging.info("Dataset validation process completed successfully.")

if __name__ == "__main__":
    main()
