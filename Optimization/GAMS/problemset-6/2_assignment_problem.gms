sets
    i streams /A, B, C, D/
    j exchangers /1*4/  ;
    
table c(i,j) cost of assigning stream i to exchanger j
    1   2   3   4
A   94  1   54  68
B   74  10  88  82
C   73  88  8   76
D   11  74  81  21  ;

Variables
x(i,j), z;
binary variables
x(i,j);

Equations ass_i(j), ass_j(i), obj   ;

ass_i(j).. sum(i, x(i,j)) =e= 1;
ass_j(i).. sum(j, x(i,j)) =e= 1;
obj.. z =e= sum((i,j), c(i,j)*x(i,j))   ;

model assignment_problem /ALL/  ;

solve assignment_problem using mip minimizing z;
display x.l, z.l;