
import pandas as pd

def extract_monthly_actuals():
    try:
        df = pd.read_excel('dataase_finance.xlsx')
        # date is 'date', value is 'Natural GAZ' (from debug info)
        df['date'] = pd.to_datetime(df['date'])
        df = df.set_index('date')
        
        # Filter for 2024
        df_2024 = df[df.index.year == 2024]
        
        # Resample by month and get mean
        monthly_avg = df_2024['Natural GAZ'].resample('M').mean()
        
        print("MONTHLY AVERAGES 2024:")
        for date, val in monthly_avg.items():
            month_name = date.strftime('%b')
            print(f"{month_name}: {val:.2f}")
            
    except Exception as e:
        print(e)

if __name__ == "__main__":
    extract_monthly_actuals()
