###this is made to use in solving quadratic equations
###Below means this equation >> 15*x**2 -87.75*x - 111.75
### YOU CAN CHANGE THESE COEFFICIENTS AS YOU LIKE !!!

values = "15 -87.75 111.75"

values = list(map(float, [eval(item) for item in values.split()]))
a = values[0]
b = values[1]
c = values[2] 
disc = (b**2) - (4 * a * c) #b**2 - 4*a*c
print(f"a >> {a}  |  b >> {b}  |  c >> {c}")
print(f"DISCRIMINANT >> {disc}")
print(f"DISCRIMINANT^0.5 >> {disc**0.5}")
if disc > 0:
    print("<<Two Real Roots>>")
    x_1 = (-b - ((disc) ** 0.5)) / (2 * a)
    x_2 = (-b + ((disc) ** 0.5)) / (2 * a)
    print(
f"""X- >> {x_1}
X+ >> {x_2}""")
elif disc == 0:
    print("<<Coincident Roots>>")
    print(f"X1=X2 >> {-b / (2 * a)}")
else:
    x1 = -(disc)**0.5 / (2 * a)
    x2 = (disc)**0.5 / (2 * a)
    print("Complex Roots")
    print(
f"""X-(complex) >> {-b / (2 * a)} + {x1}
X+(complex) >> {-b / (2 * a)} + {x2}""")
    

equation = ""
for i in range(len(values)):
    if i == len(values) - 1:
        equation += f"{values[i]} * x**{len(values) - (i + 1)}"
    else:
        equation += f"{values[i]}*x**{len(values) - (i + 1)} + "
    
    
print("The Equation >>", equation)