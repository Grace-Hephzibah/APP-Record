from functools import reduce
f=[10,24,34,24,19]
d=reduce(lambda a,b:a*b,f)
e=reduce(lambda a,b:a/b,f)
print(d)
print(e)
