
import pandas as pd
import pickle
import os

def clean_print(msg):
    # print without encoding errors
    try:
        print(msg.encode('ascii', 'ignore').decode('ascii'))
    except:
        print(msg)

def inspect():
    # EXCEL
    try:
        df = pd.read_excel('dataase_finance.xlsx')
        cols = [str(c).replace('\n', ' ').strip() for c in df.columns]
        clean_print(f"COLUMNS: {cols}")
        
        # Check for Natural Gas
        ng_col = next((c for c in cols if 'Natural' in c or 'Gas' in c or 'Price' in c), None) # Heuristic
        clean_print(f"POTENTIAL TARGET COL: {ng_col}")

        # Date range
        if 'date' in cols:
            # ensure date parsing
             clean_print("Date column found.")
             # print last few dates
             clean_print(f"Last dates: {df['date'].tail().tolist()}")

        num_rows = len(df)
        clean_print(f"TOTAL ROWS: {num_rows}")
        
    except Exception as e:
        clean_print(f"EXCEL ERROR: {e}")

    # LGBM
    try:
        path = os.path.join("Models", "lightgbm_model.pkl")
        with open(path, "rb") as f:
            model = pickle.load(f)
        
        if hasattr(model, 'num_feature'):
            clean_print(f"LGBM NUM FEATURES: {model.num_feature()}")
        if hasattr(model, 'feature_name'):
             clean_print(f"LGBM FEATURE NAMES: {model.feature_name()}")
    except Exception as e:
        clean_print(f"LGBM ERROR: {e}")

if __name__ == "__main__":
    inspect()
