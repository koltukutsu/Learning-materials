from sympy import expand, symbols, Eq, solve, simplify


x = symbols("x")
# y = symbols("y")
result = expand(15*(x - 5)**2 + (62.25) * (x - 5) + 48)
## you can use expand to expand the functionsd and not do the calculations
print("Expanded State >> ", result)
# print("Expanded State >> ", simplify(result)) ## Simplifying the equation like x*y / y
