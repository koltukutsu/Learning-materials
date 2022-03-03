sets i/ A,B,C,D,E,F,G,H/;

alias (i,j);

variables
cost;

binary variables
z(i,j)
y(j);

parameters
n /8/
p /2/
demands(i) /
A 3,
B 3,
C 2,
D 3,
E 5,
F 4,
G 4,
H 2/;

table dist(i,j)
  A  B  C  D  E  F  G  H
A 0  16 12 29 14 34 28 48
B 16 0  28 33 18 34 12 32
C 12 28 0  18 26 33 40 50
D 29 33 18 0  15 15 30 32
E 14 18 26 15 0  20 15 35
F 34 34 26 15 20 0  22 17
G 28 12 40 30 15 22 0  20
H 48 32 50 32 35 17 20 0;

equations
obj
const1(i)
const2(i,j)
const3 ;

obj.. cost=E=sum((i,j), demands(i)*dist(i,j)*z(i,j));
const1(i).. sum(j, z(i,j))=E=1;
const2(i,j).. z(i,j) =L= y(j);
const3.. sum(j, y(j)) =E= p;


model problem /all/;
solve problem using mip minimizing cost;
display cost.l, z.l;