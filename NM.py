from sympy import * 
x = symbols('x') 
def method(f, df, x1, max_iter): 
    output = list() 
    var_x = x1 
    for i in range(max_iter): 
        var_x = float(var_x - 
(f.subs(x,var_x)/df.subs(x,var_x))) 
        output.append(var_x) 
    return output 
 
def main(): 
    exp = eval(input('Enter your Expression: ')) 
    fx = diff(exp, x) 
    print(f'f(x) = {exp}') 
    print(f"f'(x) = {fx}") 
    var_start = int(input('Intial value: ')) 
    no_of_iteration = int(input('How much 
Approximation you want? ')) 
    var_list = method(exp, fx, var_start, 
no_of_iteration) 
    print(f'x1 = {var_start}') 
    for i in range(len(var_list)): 
        print(f'x{i+2} = {var_list[i]}') 
main()
