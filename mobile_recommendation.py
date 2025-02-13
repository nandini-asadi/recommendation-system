import pandas as pd
try:
    # Load the dataset
    file_path = './Dataset/mobile_recommendation_system_dataset.csv'
    data = pd.read_csv(file_path, encoding='ISO-8859-1')
    print("Data loaded successfully!")
except FileNotFoundError:
    print(f"File not found: {file_path}")
    raise

# Display the first few rows of the dataset to understand its structure
print("First few rows of the dataset:")
print(data.head())

# Example of basic data exploration
print("\nDataset Info:")
print(data.info())

print("\nSummary Statistics:")
print(data.describe())

# You can add more code here to preprocess and analyze the data
# For instance, checking for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Basic data cleaning (if needed)
data.dropna(inplace=True)  # Uncomment if you want to drop rows with missing values

# Example of further analysis or model building
# For instance, if you're building a recommendation system:
# - Data preprocessing
# - Model training
# - Evaluation

# Save any results or models if needed
data.to_csv('./Recommendations/cleaned_data.csv', index=False)

print("Script execution completed.")