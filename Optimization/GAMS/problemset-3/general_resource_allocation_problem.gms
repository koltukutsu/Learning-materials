
set
    j 'number of products' /1*5/
    i 'number of machines' /1*4/;

parameters
    p(j) 'profit for activity j' /
    1   18
    2   25
    3   10
    4   12
    5   15/
    b(i) 'amount of available resources i'/
    1   4
    2   5
    3   3
    4   7
    /
;
b(i) = b(i)*40;

table a(i, j) 'amount of resource i used by a unit of activity j'
    1   2   3   4   5
1   1.2 1.3 0.7 0.0 0.5
2   0.7 2.2 1.6 0.5 1.0
3   0.9 0.7 1.3 1.0 0.8
4   1.4 2.8 0.5 1.2 0.6;

variable
    Z
    ;

positive variable
    x(j) 'amount of activity j selected'
    ;

equations
    obj
    resource_constraint(i) 'using i to visit all the resources'
    position_constraint(j) 'chosen ones must be greater or equal to zero';
    
    obj.. Z =e= sum(j, p(j)*x(j));
    
    resource_constraint(i).. sum(j, a(i, j) * x(j)) =l= b(i);
    
    position_constraint(j).. x(j) =g= 0;
    

model my_model /all/;

solve my_model using lp maximizing Z;

display x.l;
display Z.l;
display b;