
import pandas as pd

def check_2025():
    try:
        df = pd.read_excel('dataase_finance.xlsx')
        df['date'] = pd.to_datetime(df['date'])
        
        df_2025 = df[df['date'] >= '2025-01-01']
        print(f"Rows in 2025: {len(df_2025)}")
        
        if len(df_2025) > 0:
            print(df_2025.head())
        else:
            print("No data for 2025 found.")
            print(f"Max date is: {df['date'].max()}")
            
    except Exception as e:
        print(e)

if __name__ == "__main__":
    check_2025()
