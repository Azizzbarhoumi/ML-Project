
import requests
import json

def test_forecast():
    url = "http://127.0.0.1:8000/predict_dataset"
    try:
        r = requests.post(url, json={"model_name": "rf"})
        print(f"Status: {r.status_code}")
        print(r.json())
    except Exception as e:
        print(e)

if __name__ == "__main__":
    test_forecast()
