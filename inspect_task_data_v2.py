
import pandas as pd
import pickle
import os

def inspect_excel():
    try:
        df = pd.read_excel('dataase_finance.xlsx')
        print("Excel Columns List:")
        for col in df.columns:
            print(f"- {col}")
        
        # Try to identify the target column (Natural Gas Price)
        # Usually it's 'Natural Gas' or 'Henry Hub' or similar.
        print("\nLast 5 rows:")
        print(df.tail())
        
        # Check date range
        if 'date' in df.columns:
            print(f"\nDate Range: {df['date'].min()} to {df['date'].max()}")
            
    except Exception as e:
        print(f"Error reading excel: {e}")

def inspect_lgbm():
    try:
        path = os.path.join("Models", "lightgbm_model.pkl")
        if not os.path.exists(path):
            print("LGBM model file not found in Models/")
            return

        with open(path, "rb") as f:
            model = pickle.load(f)
        print("\nLightGBM Model Info:")
        print(type(model))
        
        if hasattr(model, 'num_feature'):
            print("Num Features:", model.num_feature())
        if hasattr(model, 'feature_name'):
            print("Feature Names:", model.feature_name())
            
    except Exception as e:
        print(f"Error inspecting LGBM: {e}")

if __name__ == "__main__":
    inspect_excel()
    inspect_lgbm()
