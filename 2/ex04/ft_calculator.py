from typing import List

class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def dotproduct(v1: List[float], v2: List[float]) -> float:
        if len(v1) != len(v2):
            raise ValueError("Vectors must be the same length")
        print(f"Dot product is: {sum(a * b for a, b in zip(v1, v2))}")

    @staticmethod
    def add_vec(v1: List[float], v2: List[float]) -> List[float]:
        if len(v1) != len(v2):
            raise ValueError("Vectors must be the same length")
        print(f"Add Vector is : {[float(a + b) for a, b in zip(v1, v2)]}")

    @staticmethod
    def sub_vec(v1: List[float], v2: List[float]) -> List[float]:
        if len(v1) != len(v2):
            raise ValueError("Vectors must be the same length")
        print(f"Sous Vector is : {[float(a - b) for a, b in zip(v1, v2)]}")
