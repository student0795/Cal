from sympy import * 
#Making X as a symbol And taking input from the user. 
x, y = symbols('x y') 
equation = input('Enter a Equation: ') 
#Differentiating the equation 
diffx = diff(equation,x) 
diffy = diff(equation,y) 
#Printitng the Values. 
print(f"Entered Equation:{equation} \n\tf'x(x,y):{diffx} \n\tf'x(x,y):{diffy}") 
#Taking input for x and y. 
x_input = input("Enter the Value of x: ") 
y_input = input("Enter the Value of y: ") 
#Subtituting the Values. 
sub1 = diffx.subs({x: x_input, y: y_input}) 
sub2 = diffy.subs({x: x_input, y: y_input}) 
#Printing the Values. 
print(f'''Value of fx(x,y) at point x = {x_input} and y = {y_input} is {sub1} 
Value of fy(x,y) at point x = {x_input} and y = {y_input} is {sub2}''')    
