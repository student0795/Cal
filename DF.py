from sympy import * 
x = symbols('x') 
h = symbols('h') 
expr = x**3 
print(f"Expression: {expr}") 
a = ((x+h)**3 - x**3)/h 
limit_expr = limit(a, h, 0) 
print(f"f`({expr}) = {limit_expr}") 


from sympy import * 
x = symbols('x') 
h = symbols('h') 
#Exp 
expr = 4 - x**2 
print(f"Expressions: {expr}") 
a = (4 - ((x+h)**2) - (4-(x**2)))/h 
limit_expr = limit(a, h, 0) 
print(f"f' ({expr}) = {limit_expr}")
