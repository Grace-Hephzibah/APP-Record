import sympy
from sympy import *

x, y, z = symbols('x y z')
exp = x**2 + 7 * y + z
print("Before Substitution : {}".format(exp))

# Use sympy.subs() method
res_exp = exp.subs([(x, 2), (y, 4), (z, 1)])

print("After Substitution : {}".format(res_exp))

x = symbols('x')
exp = cos(x) + 7
print("Before Substitution : {}".format(exp))

# Use sympy.subs() method
res_exp = exp.subs(x, 0)

print("After Substitution : {}".format(res_exp))

x, y = symbols('x y')
exp = x**2 + 1
print("Before Substitution : {}".format(exp))

# Use sympy.subs() method
res_exp = exp.subs(x, y)

print("After Substitution : {}".format(res_exp))
