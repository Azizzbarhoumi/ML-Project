
import pandas as pd

try:
    df = pd.read_excel('dataase_finance.xlsx')
    cols = df.columns.tolist()
    print("COUNT:", len(cols))
    for i, c in enumerate(cols):
        print(f"{i}: {c}")
except Exception as e:
    print(e)
