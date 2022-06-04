from pyDatalog import pyDatalog
pyDatalog.create_terms("A, Pow2, Pow3")
def square(n):
    return n*n
pyDatalog.create_terms("square") 
input_values = range(10)[::-1]  
print ( A.in_(input_values) & (Pow2 == square(A)) & (Pow3 == A**3))
