from sympy import * 
 
x, y = symbols ('x y', Integer = True) 
expr = eval (input ("Enter Expression: ") ) 
 
fx = diff(expr, x) 
fy = diff(expr, y) 
fxx = diff(fx, x) 
fyy = diff(fy, y) 
fxy = diff(fx, y) 
 
print ("\nfx: {}".format (fx), "fy: {}" .format (fy), "fxx: {}".format (fxx), 
       "fyy: {}".format (fyy), "fxy: {}".format (fxy), sep="\n") 
 
criticalPoints = solve((fx, fy),(х, y)) 
 
if type(criticalPoints) is dict: 
    criticalPoints = [tuple(criticalPoints.values())] 
# Print critical points 
print("\nCritical points are:", *criticalPoints, end = "\n\n") 
 
subsValues = [] 
for point in criticalPoints: 
    value = [] 
    value.append(fxx.subs(x, point[0])) 
    value.append(fyy.subs(y, point[1])) 
    value.append(fxy.subs((x, y), (point[0], point[1]))) 
    subsValues.append (value) 
 
for i in range(len(subsValues)) : 
    print("fxx at (x, y) = (0}".format(criticalPoints[i]), "is", subsValues[i][0]) 
    print("fyy at (x, y) = (0}".format(criticalPoints[i]), "is", subsValues[i][1]) 
    print("fxy at (x, y) = (0}".format(criticalPoints[i]), "is", subsValues[i][2]) 
    print() 
 
for i in range (len(subsValues)) : 
    D = subsValues[i][0] * subsValues[i][1] - subsValues[i][2] ** 2 
    print ("Value of D at", criticalPoints[i], "is", D) 
    if D == 0: 
        print("No conclusion at", criticalPoints[i]) 
    elif D < 0: 
        print ("Saddle points at", criticalPoints[i]) 
    elif D > 0: 
        if subsValues[i][0] > 0: 
            print ("Relative minima at", criticalPoints[i]) 
        elif subsValues[i][0] < 0: 
            print ("Relative maxima at", criticalPoints[i]) 
    print() 
