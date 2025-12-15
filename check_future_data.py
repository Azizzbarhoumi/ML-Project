
import pandas as pd

def check_future_features():
    try:
        df = pd.read_excel('dataase_finance.xlsx')
        df['date'] = pd.to_datetime(df['date'])
        
        # Filter > 2024-10-17
        future_df = df[df['date'] > '2024-10-17']
        
        print(f"Rows after Oct 17 2024: {len(future_df)}")
        
        features = ['crude oil ( WTI)', 'Heating Oil ', 'Conventional Gasoline', ' RBOB', 'Ultra-Low Sulfur CARB Diesel', 'Kerosene-Type Jet Fuel', 'Propane ', 'DJIA', 'NASDAQ', 'sp500']
        
        print("\nFeature Availability (Non-null count):")
        print(future_df[features].count())
        
        print("\nFirst 5 future rows:")
        print(future_df.head())
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    check_future_features()
