import pandas as pd

print("Loading all datasets...")

# Notice we added encoding='latin1' to the end of every line!
main_data = pd.read_csv(r"D:\sanjai\studies\institution\Guvi\Projects by Guvi\Project 2\Original Datasets\IDS_ALLCountries_Data.csv", low_memory=False, encoding='latin1')

country_meta = pd.read_csv(r"D:\sanjai\studies\institution\Guvi\Projects by Guvi\Project 2\Original Datasets\IDS_CountryMetaData.csv", encoding='latin1')

series_meta = pd.read_csv(r"D:\sanjai\studies\institution\Guvi\Projects by Guvi\Project 2\Original Datasets\IDS_SeriesMetaData.csv", encoding='latin1')

footnote_meta = pd.read_csv(r"D:\sanjai\studies\institution\Guvi\Projects by Guvi\Project 2\Original Datasets\IDS_FootNoteMetaData.csv", encoding='latin1')

country_series_meta = pd.read_csv(r"D:\sanjai\studies\institution\Guvi\Projects by Guvi\Project 2\Original Datasets\Country-Series - Metadata.csv", encoding='latin1')

print("Data loaded successfully!")

# --------------------------------------------------------
# STEP 2: Clean the Main Data (CORRECTED)
# --------------------------------------------------------
print("Cleaning Main Data...")

# 1. Drop completely empty ghost columns
main_data = main_data.dropna(how='all', axis=1)

# 2. UPDATED: These are the exact text columns present in your CSV!
id_vars = [
    'Country Name', 
    'Country Code', 
    'Counterpart-Area Name', 
    'Counterpart-Area Code', 
    'Series Name', 
    'Series Code'
]

# 3. Melt the years into a single column
clean_main = main_data.melt(
    id_vars=id_vars, 
    var_name='Year', 
    value_name='Debt_Value'
)

# 4. Convert Year to numbers and drop empty debt rows
clean_main['Year'] = pd.to_numeric(clean_main['Year'], errors='coerce')
clean_main = clean_main.dropna(subset=['Debt_Value'])
clean_main = clean_main.reset_index(drop=True)


# --------------------------------------------------------
# STEP 3: Clean the Metadata (CORRECTED)
# --------------------------------------------------------
print("Cleaning Metadata dictionaries...")

# --- COUNTRY METADATA ---
clean_country = country_meta.dropna(how='all', axis=1).dropna(how='all', axis=0)

# The dictionary uses 'Code', so we rename it to 'Country Code' to match the main data!
clean_country = clean_country.rename(columns={'Code': 'Country Code'})

# Fill in missing aggregate regions
clean_country['Region'] = clean_country['Region'].fillna('Regional Aggregate')
clean_country['Income Group'] = clean_country['Income Group'].fillna('Regional Aggregate')


# --- SERIES METADATA ---
clean_series = series_meta.dropna(how='all', axis=1).dropna(how='all', axis=0)

# The dictionary uses 'Code', so we rename it to 'Series Code' to match the main data!
clean_series = clean_series.rename(columns={'Code': 'Series Code'})

# Keep only the essential reference columns
columns_to_keep = ['Series Code', 'Indicator Name', 'Long definition', 'Topic']
clean_series = clean_series[[c for c in columns_to_keep if c in clean_series.columns]]

# clean_main.to_csv('AllCountries_DATA.csv',index=False)
# clean_country.to_csv('CountriesMeta_DATA.csv',index=False)
# clean_series.to_csv('SeriesMeta_DATA.csv',index=False)


# print(clean_main.mean(numeric_only=True))
D=pd.read_csv("D:\sanjai\studies\institution\Guvi\Projects by Guvi\Project 2\SQL tables\AllCountries_DATA.csv")
D.to_csv("ALLCountries_Dataset.csv", index=False, float_format='%.0f')








