from sympy import * 
 
x, y = symbols('x y') 
 
Eqr = eval(input('Enter the Equation: ')) 
var = Poly(Eqr, x, y) 
power = var.degree() 
power -= 1 
 
fx = diff(Eqr, x) 
fy = diff(Eqr, y) 
fxx = diff(fx, x) 
fyy = diff(fy, y) 
fxy = diff(fx, y) 
 
. 
 
print(f'\nfx: {fx}\nfy: {fy}\nfxx: {fxx}\nfyy: {fyy}\nfxy: {fxy}') 
 
cp = list() 
cp_var = solve((fx, fy), (x, y)) 
 
if type(cp_var) == dict: 
    cp_var = [tuple(cp_var.values())] 
 
  
for x_val, y_val in cp_var: 
    if power == 0: 
        break 
    cp.append((x_val, y_val)) 
    power -= 1 
 
print('\nCritical Points are ',end='') 
for i in cp: 
    print(i,end='') 
print() 
 
Values = list() 
for i in cp: 
    Values.append([fxx.subs(x,i[0]),fyy.subs(y,i[1]),fxy.subs({x:i[0],y:i[1]})]) 
 
for i,j in zip(Values,cp): 
    print(f'''\nfxx at (x,y) = {j} is {i[0]} 
fyy at (x,y) = {j} is {i[1]} 
fxy at (x,y) = {j} is {i[2]}''') 
 
for i,j in zip(Values,cp): 
    D = i[0]*i[1]*i[2]**2 
    print(f'\nValue of D at {j} is {D}') 
    if D > 0 and i[0] > 0: 
        print(f'Relative Minima is present at {j}.') 
    elif D > 0 and i[0] < 0: 
        print(f'Relative Maxima is present at {j}.') 
    elif D < 0: 
        print(f'The Critical Point {j} is a saddle point.') 
    else: 
        print(f'No conclusion can be drawn on {j}.') 
