# Algeria Housing Scraper Analysis

A comprehensive data pipeline for scraping, processing, and analyzing real estate listings from OuedKniss, Algeria's leading classified ads platform.

## Project Overview

This project automates the collection and analysis of real estate data to provide insights into the Algerian property market. It includes web scraping, data cleaning, processing, and interactive dashboard visualization using Power BI.

## Project Structure

```
.
├── analysis/
│   ├── cleaning_script.py          # Data processing and cleaning script
│   └── notebooks/
│       └── cleaning_notebook.ipynb # Jupyter notebook for data exploration
├── dashboards/
│   ├── Dashboard.pbix              # Main Power BI dashboard
│   └── report.pbix                 # Additional Power BI report
├── data/
│   └── final/
│       ├── processed_data_2025-07-25.csv  # Cleaned dataset
│       └── processed_data_2025-07-26.csv  # Cleaned dataset
└── scraper/
    └── main.py                     # Web scraper for OuedKniss listings
```

## Features

- **Automated Web Scraping**: Extracts real estate listings from OuedKniss API
- **Data Processing**: Cleans and structures raw data for analysis
- **Geospatial Analysis**: Processes location data (cities, regions/wilayas)
- **Property Classification**: Identifies property types (F1, F2, F3, etc.) and transaction types (rent/sale)
- **Interactive Dashboards**: Power BI visualizations for market insights

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.x
- Required Python packages:
  ```bash
  pip install requests pandas
  ```
- Microsoft Power BI Desktop (for dashboard viewing/editing)

## Usage

### 1. Data Scraping
To scrape real estate listings from OuedKniss:

```bash
cd scraper
python main.py <number_of_pages>
```

**Example:**
```bash
python main.py 50  # Scrapes 50 pages of listings
```

**Features:**
- Fetches listings from the "immobilier" (real estate) category
- Includes random delays to respect server limits
- Saves raw data to `../data/raw.csv`
- Uses rotating User-Agent headers

### 2. Data Processing
To clean and process the scraped data:

```bash
cd analysis
python cleaning_script.py <chunksize>
```

**Example:**
```bash
python cleaning_script.py 10000  # Processes data in chunks of 10,000 rows
```

**Processing Features:**
- Extracts location information (city and wilaya)
- Processes property area information
- Identifies property types (F1, F2, F3, etc.)
- Classifies listings as rent or sale
- Generates timestamped output files

### 3. Data Analysis
Use the Jupyter notebook for exploratory data analysis:
```bash
jupyter notebook analysis/notebooks/cleaning_notebook.ipynb
```

## Data Schema

### Processed Data Columns:
- **Title**: Property listing title
- **Date**: Listing creation/refresh date
- **Price**: Property price (numeric)
- **Town**: City name
- **Wilaya**: Region/state name
- **Area**: Property area in square meters
- **Store**: Real estate agency/store name
- **FlatType**: Apartment type (F1, F2, F3, etc.)
- **isForRent**: Boolean indicating if property is for rent

## Power BI Dashboards

The project includes comprehensive Power BI dashboards providing insights into:

### Dashboard Features:
- Market price trends and distributions
- Geographic analysis by wilaya and city
- Property type breakdown and analysis
- Rental vs. sale market comparison
- Real estate agency performance metrics
- Time-series analysis of listing activity

### Dashboard Screenshots:

*[Space reserved for Power BI dashboard screenshots]*

#### Main Dashboard Overview
![Dashboard Overview](screenshots/dashboard_overview.png)

#### Price Analysis by Region
![Price Analysis](screenshots/price_analysis.png)

#### Property Type Distribution
![Property Types](screenshots/property_types.png)

#### Market Trends Over Time
![Market Trends](screenshots/market_trends.png)

## Configuration

### Scraper Settings
- **API Endpoint**: `https://api.ouedkniss.com/graphql`
- **Category**: Real estate ("immobilier")
- **Results per page**: 48 listings
- **Delay between requests**: 1-3 seconds (randomized)

### Data Processing Settings
- **Output format**: CSV with UTF-8 encoding
- **Date format**: ISO datetime
- **Chunk processing**: Configurable batch sizes for large datasets

## Data Quality & Validation

The cleaning script implements several data quality measures:
- **Price validation**: Converts prices to numeric format
- **Date standardization**: Ensures consistent datetime formatting
- **Location extraction**: Parses nested city/region data
- **Property type identification**: Uses regex to extract apartment types
- **Transaction type classification**: Distinguishes rent from sale listings

## Important Notes

- **Rate Limiting**: The scraper includes built-in delays to respect OuedKniss server limits
- **Data Privacy**: Only public listing data is collected
- **API Changes**: Monitor for potential changes to the OuedKniss GraphQL API
- **Large Datasets**: Use appropriate chunk sizes for processing large amounts of data

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

**Last Updated**: July 2025
