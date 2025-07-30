import pandas as pd
from typing import Optional


def load(path: str) -> Optional[pd.DataFrame]:
    "load a csv"
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as e:
        print(f"Failed to load dataset: {e}")
        return None
