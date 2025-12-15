
import pandas as pd
import pickle
import os
import numpy as np

def run():
    output = []
    
    # EXCEL
    try:
        df = pd.read_excel('dataase_finance.xlsx')
        output.append("EXCEL COLUMNS:")
        for i, c in enumerate(df.columns):
            output.append(f"{i}: {c}")
        
        output.append("\nTAIL DATA (Last 5 rows):")
        output.append(str(df.tail()))
        
    except Exception as e:
        output.append(f"EXCEL ERROR: {e}")

    # LGBM
    try:
        path = os.path.join("Models", "lightgbm_model.pkl")
        with open(path, "rb") as f:
            model = pickle.load(f)
        
        output.append("\nLGBM INFO:")
        if hasattr(model, 'num_feature'):
            output.append(f"Num Features: {model.num_feature()}")
        if hasattr(model, 'feature_name'):
            output.append(f"Feature Names: {model.feature_name()}")
            
        # Try prediction with 7 features (what frontend sends)
        try:
            dummy = np.random.rand(1, 7)
            model.predict(dummy)
            output.append("Prediction with 7 features: SUCCESS")
        except Exception as pred_e:
            output.append(f"Prediction with 7 features FAILED: {pred_e}")
            
    except Exception as e:
        output.append(f"LGBM ERROR: {e}")

    with open("debug_info.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(output))

if __name__ == "__main__":
    run()
