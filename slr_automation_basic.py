import pandas as pd

# Function to clean metadata data from downloads (Scopus/WoS)
def clean_metadata(file_path):
    """
    Automating metadata cleaning as inspired by the efficiency 
    framework of Atkinson & Flint (2023).
    """
    try:
        df = pd.read_csv(file_path)
        # Menghapus baris yang tidak memiliki judul atau abstrak
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
