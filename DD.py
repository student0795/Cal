from sympy import * 
from math import sqrt 
 
x, y, z = symbols("x y z") 
 
def directional_derivative(): 
    eqn=input(">>Enter Equation : ") 
    diff_x=str(diff(eqn,x)) 
    diff_y=str(diff(eqn,y)) 
    diff_z=str(diff(eqn,z)) 
    val_diff_x=eval(diff_x) 
    val_diff_y=eval(diff_y) 
    val_diff_z=eval(diff_z) 
 
    print(">>Enter vector equation : ") 
    u1 = eval(input(">>Enter coefficient of i : ")) 
    u2 = eval(input(">>Enter coefficient of j : ")) 
    u3 = eval(input(">>Enter coefficient of k : ")) 
    directional_derivative = u1*val_diff_x + u2*val_diff_y + u3*val_diff_z 
    return(directional_derivative) 
 
ans = str(directional_derivative()) 
x = int(input(">>Enter value of X : ")) 
y = int(input(">>Enter value of y : ")) 
z = int(input(">>Enter value of z : ")) 
final_ans = eval(ans) 
print("Directional Derivcative pf equatuion : ",final_ans)



from sympy import * 
from math import * 
 
x,y,z = symbols("x y z") 
 
def directed_derivative(equ,num,values): 
    diff_list = list() 
    final_value = list() 
    vec_list = list() 
    vec_value = ['i','j','k'] 
    value_list = ['x','y','z'] 
         
    if num == 3: 
        diff_x = diff(equ,value_list[0]) 
        diff_y = diff(equ,value_list[1]) 
        diff_z = diff(equ,value_list[2]) 
        final_value1 = diff_x.subs({x:values[0], y:values[1], z:values[2]}) 
        final_value2 = diff_y.subs({x:values[0], y:values[1], z:values[2]}) 
        final_value3 = diff_z.subs({x:values[0], y:values[1], z:values[2]}) 
         
    if num == 2: 
        diff_x = diff(equ,value_list[0]) 
        diff_y = diff(equ,value_list[1]) 
        final_value1 = diff_x.subs({x:values[0], y:values[1]}) 
        final_value2 = diff_y.subs({x:values[0], y:values[1]}) 
         
    print('Enter Vecter Equation Details:') 
    for i in range(num): 
        vec_list.append(eval(input(f'Enter the Coefficent {vec_value[i]}:'))) 
    if num == 3: 
        dd = vec_list[0]*final_value1+vec_list[1]*final_value2+vec_list[2]*final_value3 
    if num == 2: 
        dd = vec_list[0]*final_value1+vec_list[1]*final_value2 
    return dd 
 
var = int(input('Enter the number of Variable: ')) 
var_list = ['x','y','z'] 
Value = list() 
for i in range(var): 
    Value.append(int(input(f'Enter the value of {var_list[i]}:'))) 
answer = directed_derivative(input('Enter Equation: '),var,Value) 
print(answer) 
