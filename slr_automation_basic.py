import pandas as pd

# Function to clean metadata data from downloads (Scopus/WoS)
def clean_metadata(file_path):
    try:
        df = pd.read_csv(file_path)
        # Delete rows that do not have a title or abstract
        df_cleaned = df.dropna(subset=['Title', 'Abstract'])
        print(f"Success! Processed {len(df_cleaned)} papers.")
        return df_cleaned
    except Exception as e:
        print(f"Error: {e}")

# Simple screening function based on keywords
def keyword_screening(df, keywords):
    """
    NLP-based screening logic for faster inclusion/exclusion process.
    """
    mask = df['Abstract'].str.contains('|'.join(keywords), case=False, na=False)
    filtered_df = df[mask]
    return filtered_df

# Example of use (can be adjusted later)
if __name__ == "__main__":
    print("AI-Enhanced Research Tools: SLR Module Loaded.")

# Creating sample data (Dummy Data)
data = {
    'Title': ['Research A', 'Research B', 'Research C'],
    'Abstract': ['Artificial Intelligence in education', 'Traditional teaching', 'Machine learning and SLR']
}
df_test = pd.DataFrame(data)

# Testing screening functions
keywords = ['Artificial Intelligence', 'Machine learning']
result = keyword_screening(df_test, keywords)

print("\n--- Screening Test Results ---")
print(result)
