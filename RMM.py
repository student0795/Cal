from sympy import * 
 
x, y = symbols('x y') 
equation = input('Enter a Equation: ')

diffx = diff(equation,x) 
diffy = diff(equation,y) 
 
print(f"Entered Equation:{equation} \n\tf'x(x,y):{diffx} \n\tf'x(x,y):{diffy}") 
 
x_input = input("Enter the Value of x: ") 
y_input = input("Enter the Value of y: ") 
 
sub1 = diffx.subs({x: x_input, y: y_input}) 
sub2 = diffy.subs({x: x_input, y: y_input}) 

print(f'''Value of fx(x,y) at point x = {x_input} and y = {y_input} is {sub1} 
Value of fy(x,y) at point x = {x_input} and y = {y_input} is {sub2}''')  
