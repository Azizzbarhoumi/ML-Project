
import pickle
import os
import pandas as pd
import numpy as np
# Attempt to import xgboost - might fail if not installed, but usually pre-installed in this env or user has it
try:
    import xgboost as xgb
except ImportError:
    pass

model_dir = "Models"

def clean_print(msg):
    try:
        print(str(msg).encode('ascii', 'ignore').decode('ascii'))
    except:
        print("Printing error")

def inspect_lr():
    print("\n--- Linear Regression ---")
    try:
        path = os.path.join(model_dir, "linear_regression_model.pkl")
        with open(path, "rb") as f:
            obj = pickle.load(f)
        
        if isinstance(obj, dict):
            print("Keys:", obj.keys())
            if "scaler" in obj:
                print("Scaler n_features_in_:", getattr(obj["scaler"], "n_features_in_", "Unknown"))
                if hasattr(obj["scaler"], "feature_names_in_"):
                    clean_print(f"Scaler Feature Names: {obj['scaler'].feature_names_in_}")
            if "model" in obj:
                print("Model coef shape:", getattr(obj["model"], "coef_", "Unknown").shape)
                if hasattr(obj["model"], "feature_names_in_"):
                    clean_print(f"Model Feature Names: {obj['model'].feature_names_in_}")
    except Exception as e:
        print("LR Error:", e)

def inspect_xgb():
    print("\n--- XGBoost ---")
    try:
        path = os.path.join(model_dir, "aziz_xgboost_model.pkl")
        with open(path, "rb") as f:
            model = pickle.load(f)
        print("Type:", type(model))
        
        if hasattr(model, "n_features_in_"):
            print("n_features_in_:", model.n_features_in_)
        
        if hasattr(model, "feature_names_in_"):
             clean_print(f"Feature Names: {model.feature_names_in_}")
        elif hasattr(model, "get_booster"):
            booster = model.get_booster()
            clean_print(f"Booster Feature Names: {booster.feature_names}")
            
    except Exception as e:
        print("XGB Error:", e)

if __name__ == "__main__":
    inspect_lr()
    inspect_xgb()
