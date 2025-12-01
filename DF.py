from sympy import * 
x = symbols('x') 
h = symbols('h') 
expr = x**3 
print(f"Expression: {expr}") 
a = ((x+h)**3 - x**3)/h 
limit_expr = limit(a, h, 0) 
print(f"f`({expr}) = {limit_expr}") 
