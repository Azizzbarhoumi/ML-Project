
import pandas as pd
try:
    df = pd.read_excel('dataase_finance.xlsx')
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
        print(f"Date Range: {df['date'].min()} to {df['date'].max()}")
    else:
        print("Column 'date' not found")
except Exception as e:
    print(e)
