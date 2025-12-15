
import pickle
import os
import sys

# Redirect output to file
sys.stdout = open("model_info.txt", "w", encoding="utf-8")

model_dir = "Models"
models = {
    "lr": "linear_regression_model.pkl",
    "xgb": "aziz_xgboost_model.pkl",
    "lgbm": "lightgbm_model.pkl",
    "rf": "yossriforest.pkl"
}

print("Inspecting models...")
for name, filename in models.items():
    path = os.path.join(model_dir, filename)
    try:
        with open(path, "rb") as f:
            model = pickle.load(f)
            print(f"\n--- Model: {name} ({filename}) ---")
            print(f"Type: {type(model)}")
            
            # Feature inspection
            features = None
            if hasattr(model, "feature_names_in_"):
                features = list(model.feature_names_in_)
            elif hasattr(model, "get_booster") and hasattr(model.get_booster(), "feature_names"):
                 features = model.get_booster().feature_names
            elif hasattr(model, "booster_") and hasattr(model.booster_, "feature_name"):
                features = model.booster_.feature_name()
            
            if features:
                print(f"Features ({len(features)}): {features}")
            elif hasattr(model, "n_features_in_"):
                 print(f"Num Features: {model.n_features_in_}")
            else:
                print("Could not determine features")

    except Exception as e:
        print(f"Error loading {filename}: {e}")
