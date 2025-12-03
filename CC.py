from sympy import * 
x = symbols('x') 
exp = eval(input("Enter the expression : ")) 
low = int(input("Enter the Lower Limit : ")) 
upp = int(input("Enter the Upper Limit : ")) 
ig = integrate(exp,(x,low,upp)) 
print(f"Area below the {exp} is {ig}") 



from sympy import * 
x = symbols('x') 
exp = eval(input("Enter the expression : ")) 
low = int(input("Enter the Lower Limit : ")) 
upp = int(input("Enter the Upper Limit : ")) 
df = diff(exp) 
expr = eval(f"(1 + {df}**2)**(1/2)") 
ig = integrate(expr,(x,low,upp)) 
print(f"The length of the curve of the {exp} is 
{ig}") 
