# Retail Sales & Product Performance Analytics

I built this project to analyze retail sales performance across different product lines and store locations. The main goal was to take raw sales records, clean the data using Python, and present key profit trends in a clear Power BI dashboard layout.

---

## What I Used
* **Python (Pandas & NumPy):** For cleaning raw CSV files, calculating margins, and bucketing products by profitability.
* **Power BI & Excel:** For building visual reports, KPI cards, and regional slicers.
* **GitHub:** For version control and sharing the project files.

---

## Project Workflow

1. **Raw Data:** Started with order records in `sales_data.csv` covering date, product, category, region, units sold, price, and unit cost.
2. **Data Processing:**
   * Used Pandas to convert dates and compute Total Revenue, Cost, and Net Profit.
   * Applied NumPy logic to calculate Profit Margin percentages and flag high-performing transactions.
   * Exported the cleaned dataset to `cleaned_sales_data.csv`.
3. **Dashboard Setup:** 
   * Designed top KPI cards for Revenue, Profit, and Units Sold.
   * Created simple bar and donut charts to compare category trends and regional profit performance.

---

## Main Takeaways
* **High Margin Categories:** Clothing items like jackets and t-shirts delivered strong profit margins (over 50%) despite lower individual unit costs.
* **Regional Insights:** The North and East store regions led total sales volume across all quarters.
* **Volume Drivers:** Fast-moving items like keyboards and headphones provided steady cash flow and volume, balancing out slower-selling furniture items.
