import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# 1. FUNCTION: Metadata Cleaning
def clean_metadata(df):
    """
    Removes entries with missing Titles or Abstracts to ensure data quality.
    """
    initial_count = len(df)
    df_cleaned = df.dropna(subset=['Title', 'Abstract'])
    print(f"[Cleaning] Removed {initial_count - len(df_cleaned)} incomplete records.")
    return df_cleaned

# 2. FUNCTION: Keyword Screening (NLP-based logic)
def keyword_screening(df, keywords):
    """
    Filters papers based on research keywords within the Abstract.
    """
    pattern = '|'.join(keywords)
    mask = df['Abstract'].str.contains(pattern, case=False, na=False)
    filtered_df = df[mask]
    print(f"[Screening] Found {len(filtered_df)} papers matching keywords.")
    return filtered_df

# 3. FUNCTION: Detailed Data Extraction (Country & Journal)
def extract_detailed_metadata(df):
    """
    Extracts Country from Affiliations and prepares data for visualization.
    """
    if 'Affiliations' in df.columns:
        # Extract last part of the string as Country
        df['Country'] = df['Affiliations'].str.split(',').str[-1].str.strip()
    return df

# 4. FUNCTION: Visualization - Yearly Trend (Line Chart)
def plot_yearly_trend(df):
    if 'Year' in df.columns:
        yearly_counts = df['Year'].value_counts().sort_index()
        plt.figure(figsize=(10, 5))
        plt.plot(yearly_counts.index.astype(str), yearly_counts.values, marker='o', color='#2c3e50')
        plt.title('Research Trend: Publications per Year')
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.show()

# 5. FUNCTION: Visualization - Global Map (Bubble Map)
def plot_research_map(df):
    if 'Country' in df.columns:
        map_data = df['Country'].value_counts().reset_index()
        map_data.columns = ['Country', 'Paper_Count']
        fig = px.scatter_geo(map_data, locations="Country", locationmode='country names',
                             size="Paper_Count", hover_name="Country", 
                             template="plotly_white", title='Global Research Distribution')
        fig.show()

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    print("🚀 AI-Enhanced Research Tools: SLR Module Loaded.")

    # [DUMMY DATA SECTION] 
    # Designed to mimic Scopus/WoS Export structure
    dummy_data = {
        'Title': ['AI in Construction', 'BIM for Safety', 'Knowledge Graph in Oil & Gas', 'Digital Twin for PM'],
        'Abstract': ['Applying Machine Learning in buildings', 'Safety protocols', 'Knowledge management AI', 'Project management Digital Twin'],
        'Year': [2023, 2024, 2024, 2025],
        'Affiliations': ['Univ X, USA', 'Univ Y, China', 'Univ Z, Saudi Arabia', 'Univ W, USA'],
        'Source title': ['Journal of Automation', 'Safety Science', 'KM Journal', 'Construction Review']
    }
    df_sample = pd.DataFrame(dummy_data)

    # PROCESS FLOW
    # 1. Cleaning
    cleaned = clean_metadata(df_sample)
    
    # 2. Screening
    my_keywords = ['Machine Learning', 'AI', 'Digital Twin']
    final_selection = keyword_screening(cleaned, my_keywords)
    
    # 3. Metadata Enhancement (Country Extraction)
    final_with_meta = extract_detailed_metadata(final_selection)

    print("\n--- Final Selected Papers (Preview) ---")
    print(final_with_meta[['Title', 'Country', 'Year']])

    # 4. Visualizations (Uncomment to test)
    # plot_yearly_trend(final_with_meta)
    # plot_research_map(final_with_meta)
