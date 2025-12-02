import sympy
from sympy import *

print("----------Getting interval values---------")
interval = []

print("\nPlease enter the interval:")
a = int(input("Start: "))
b = int(input("End: "))
interval.append(a)
interval.append(b)
print("The interval is:", interval, "\n")

x = symbols('x')

print("========Entering f(x)========")
expr = input("\nEnter the equation here (use sympy syntax, e.g., sin(x), tan(x), x**2): ")

value = sympy.sympify(expr)
print("Given equation is:", value)

derivative = diff(value, x)
print("\nThe derivative of the given equation is:", derivative, '\n')

sol = sympy.solve(derivative, x)

# Add boundaries
sol.append(a)
sol.append(b)

# Sort numerically
sol = sorted(sol, key=lambda v: float(value.evalf(subs={x: v})))

xvalues = []
f = []

print("\n--------------------------- Calculating f(x) ---------------------------")
print("\nx\tf(x)")
for i in sol:
    fx = value.evalf(subs={x: i})
    print(i, ":\t", fx)
    xvalues.append(i)
    f.append(fx)

result = {xvalues[i]: f[i] for i in range(len(xvalues))}
print("\nResultant dictionary:", result)

print("\nAbsolute Maxima:", max(f), "occurs at x =", max(result, key=result.get))
print("Absolute Minima:", min(f), "occurs at x =", min(result, key=result.get))
