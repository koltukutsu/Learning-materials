VARIABLE
z;
POSITIVE VARIABLES
x11 , x12 , x21 , x22 , x31 , x32 ;

EQUATIONS
OF Objective function
Const1 Capacity production in the plant 1
Const2 Capacity production in the plant 2
Const3 Capacity production in the plant 3
Const4 Demand in the store 1
Const5 Demand in the store 2;

OF .. z =E= 4*x11 + 3*x12 + 2*x21 + 6*x22 + 4*x31 + 6*x32 ;
Const1 .. x11 + x12 =L= 50;
Const2 .. x21 + x22 =L= 65;
Const3 .. x31 + x32 =L= 45;
Const4 .. x11 + x21 + x31 =G= 85;
Const5 .. x12 + x22 + x32 =G= 75;

MODEL TP / all /;
SOLVE TP USING mip MINIMIZING z;
DISPLAY z.l,x11.l,x12.l, x21.l,x22.l,x31.l,x32.l;
