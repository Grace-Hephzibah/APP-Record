from typing import List
# Vector is a list of float values
Vector = List[float]
def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]
a = scale(scalar=2.0, vector=[1.0, 2.0, 3.0])
print(a)
