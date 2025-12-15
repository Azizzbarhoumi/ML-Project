
import pandas as pd
import pickle
import os

def inspect_excel():
    try:
        df = pd.read_excel('dataase_finance.xlsx')
        print("Excel Columns:", df.columns.tolist())
        print("First 5 rows:")
        print(df.head())
        # Check for date and value columns
        # Assuming we need monthly averages or specific points for the chart
        # The chart in ComparisonSection.tsx has months Jan-Dec and 'actual' values.
    except Exception as e:
        print(f"Error reading excel: {e}")

def inspect_lgbm():
    try:
        path = os.path.join("Models", "lightgbm_model.pkl")
        with open(path, "rb") as f:
            model = pickle.load(f)
        print("\nLightGBM Model Type:", type(model))
        
        # specific attributes for LightGBM
        if hasattr(model, 'num_feature'):
            print("LGBM num_feature:", model.num_feature())
        if hasattr(model, 'feature_name'):
            print("LGBM feature_name:", model.feature_name())
            
    except Exception as e:
        print(f"Error inspecting LGBM: {e}")

if __name__ == "__main__":
    inspect_excel()
    inspect_lgbm()
