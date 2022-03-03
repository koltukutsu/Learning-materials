sets i/a,b,c,d,e,f,g,h/;

alias (i,j);

variables
m cost;

binary variables
z(i,j)
y(j)

Parameters
n /8/
p /2/
a(i) /a 3, b 3, c 2, d 3, e 5, f 4, g 4, h 2/;

table d(i,j)
    a   b   c   d   e   f   g   h
a   0   16  12  29  14  34  28  48
b   16  0   28  33  18  34  12  32
c   12  28  0   18  26  33  40  50
d   29  33  18  0   15  15  30  32
e   14  18  26  15  0   20  15  35
f   34  34  26  15  20  0   22  17
g   28  12  40  30  15  22  0   20
h   48  32  50  32  35  17  20  0;

Equations
constraint1(i)
constraint2(i,j)
constraint3
obj;

constraint1(i)..     sum(j,z(i,j)) =e= 1;
constraint2(i,j)..   z(i,j)=l=y(j);
constraint3..        sum(j, y(j))=e=p;
obj..          m=e=sum((i,j), a(i)*d(i,j)*z(i,j));

model pmedian /all/;
solve pmedian using mip minimizing m;
display m.l, z.l;