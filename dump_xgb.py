
import pickle
import os
import xgboost as xgb
import json

def dump_xgb():
    try:
        path = os.path.join("Models", "aziz_xgboost_model.pkl")
        with open(path, "rb") as f:
            model = pickle.load(f)
        
        # Dump to text file to read feature names
        booster = model.get_booster()
        feature_names = booster.feature_names
        print(f"Booster .feature_names: {feature_names}")
        
        # If None, try dumping
        booster.dump_model("xgb_dump.txt")
        print("Dumped to xgb_dump.txt")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    dump_xgb()
