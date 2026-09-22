import pandas as pd
import numpy as np

def process_sales_data(input_path="sales_data.csv", output_path="cleaned_sales_data.csv"):
    df = pd.read_csv(input_path)
    df['Date'] = pd.to_datetime(df['Date'])

    df['Total_Revenue'] = df['Units_Sold'] * df['Unit_Price']
    df['Total_Cost'] = df['Units_Sold'] * df['Cost_Per_Unit']
    df['Profit'] = df['Total_Revenue'] - df['Total_Cost']

    df['Profit_Margin_%'] = np.where(
        df['Total_Revenue'] > 0, 
        np.round((df['Profit'] / df['Total_Revenue']) * 100, 2), 
        0
    )

    df['Performance_Category'] = np.where(
        df['Profit'] >= 500, 'High Profit', 'Moderate Profit'
    )

    df.to_csv(output_path, index=False)
    print("Data processed successfully.")

if __name__ == "__main__":
    process_sales_data()
