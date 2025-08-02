# Algeria Housing Market Analysis

**A data-driven exploration of Algerian real estate listings by scraping, cleaning, and visualizing insights from OuedKniss.**

---

## 📌 Project Overview

This project pipelines raw property listings from OuedKniss into a cleaned dataset, enabling detailed market analysis and interactive Power BI dashboards. It demonstrates end-to-end data analytics skills:

1. **Web Scraping**: Automated collection of real estate listings via the OuedKniss GraphQL API.
2. **Data Cleaning & Enrichment**: Processing raw JSON to structured CSV, extracting geolocation and property attributes.
3. **Visualization & Reporting**: Building interactive Power BI dashboards to communicate key findings.

![Dashboard Overview](https://tntaizamsozuvsaecpsl.supabase.co/storage/v1/object/public/portfolio/images/RealEstateProject.png)

---

## 🔍 Key Questions & Findings

* **How do average prices vary by Wilaya and city?**
  
![Price Analysis](https://tntaizamsozuvsaecpsl.supabase.co/storage/v1/object/public/portfolio/images/RealEstateProject2.png)

* **What is the distribution of apartment types (F1–F5+) across regions?**

  * F2 and F3 dominate rental listings; F4+ more common in sale market.

![Property Types](https://tntaizamsozuvsaecpsl.supabase.co/storage/v1/object/public/portfolio/images/RealEstateProject3.png)

*(Detailed charts available in the `dashboards/` Power BI files.)*

---

## 📁 Repository Structure

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

---

## 🚀 Setup & Usage

1. **Clone the repo**

   ```bash
   git clone https://github.com/solxire88/algeria-housing-scraper-analysis.git
   cd algeria-housing-scraper-analysis
   ```

2. **Fetch listings**

   ```bash
   python scraper/main.py 50   # Scrape 50 pages
   ```

   This generates `data/raw/listings_<date>.csv`.

3. **Clean & preprocess**

   ```bash
   python analysis/cleaning_script.py 500 # Get a chunk of 500 listings
   ```

   Generates timestamped CSVs with standardized columns: `Price`, `Wilaya`, `Town`, `Area_m2`, `Type`, `Rent_Sale`.


4. **Open Power BI Dashboards**
   Load `.pbix` files in `dashboards/` to interact with filters, maps, and trend visuals.

---

## 🛠 Data Schema (Processed)

| Column      | Description                      |
| ----------- | -------------------------------- |
| Listing     | Unique identifier                |
| Date        | Scrape date (ISO 8601)           |
| Price\_DZD  | Numeric property price           |
| Wilaya      | Administrative region            |
| Town        | City/commune name                |
| Area\_m2    | Property size in square meters   |
| FlatType    | Apartment type (F1, F2, ... F5+) |
| isForRent   | "True" or "False"                |
| Store       | Listing agency/store name        |
