import pandas as pd
import os

# Directory containing the CSV files
directory = '/routes'

# List all files in the directory
files = os.listdir(directory)

# Initialize an empty dictionary to store DataFrames
dfs = {}

# Iterate over each file in the directory
for file in files:
    if file.endswith(".csv"):  # Check if the file is a CSV file
        # Construct the full file path
        file_path = os.path.join(directory, file)
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Store the DataFrame in the dictionary with the file name as the key
        dfs[file] = df


print(df)

# Do whatever operations you need with the DataFramesr