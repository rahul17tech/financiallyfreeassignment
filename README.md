# **Vehicle Registration Dashboard**

An investor-focused interactive dashboard built with **Streamlit** to visualize vehicle registration trends using data from the Vahan dashboard.

## **Features**
- Date range selection for historical trend analysis.
- Filters by **vehicle category** and **manufacturer**.
- Year-over-Year (YoY) and Quarter-over-Quarter (QoQ) growth calculations.
- Interactive line and bar charts using Plotly.
- Investor insight highlighting top-performing manufacturers.

## **Technologies Used**
- **Python**
- **Streamlit**
- **Pandas**
- **Plotly**

## **Data Assumptions**
- The dataset `vehicle_data_clean_timeseries.csv` contains **monthly vehicle registration data** for:
  - TWO WHEELER  
  - THREE WHEELER  
  - FOUR WHEELER
- Manufacturer names are taken exactly from the real Jan 2025 Vahan dataset.
- Data is synthetic but realistic, generated for **Jan 2023 → Dec 2024** to simulate:
  - Year-over-Year (YoY) growth  
  - Quarter-over-Quarter (QoQ) growth
- Each category has its own set of manufacturers, and numbers vary slightly month-to-month with a mild growth trend.

## **Installation and Setup**
1. Clone the repository.
   ```bash
   git clone https://github.com/rahul17tech/financiallyfreeassignment.git
   cd financiallyfreeassignment

## **Feature Roadmap**
1. Current:
   - Date range filter
   - Category & manufacturer filters
   - Trend charts
   - YoY & QoQ growth charts
   - Investor insights
3. Planned:
   - Manufacturer growth comparison tab.
   - State-wise filter (if state-level data available).
   - Export to PDF/Excel for investor reports.
   - Real-time integration with Vahan dashboard.
   - Improved mobile responsiveness.
  
## **Outputs**
<img width="1917" height="869" alt="image" src="https://github.com/user-attachments/assets/13c26825-e94c-4e15-844b-435f0275f7a9" />
<img width="1919" height="865" alt="image" src="https://github.com/user-attachments/assets/658fafd6-514a-48ac-ab14-063c1e40840f" />
<img width="1919" height="837" alt="image" src="https://github.com/user-attachments/assets/6642e9f8-afb9-425a-b92e-c8563e58cf83" />



