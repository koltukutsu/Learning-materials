sets
    i 'of clients/cities' / 1 * 7 /
    j 'of facility sites'/ 1 * 6 /;
    
    
parameters
    f(j) /
    1   10
    2   10
    3   10
    4   10
    5   10
    6   10/
    
    u(j)/
    1   6
    2   6
    3   6
    4   6
    5   6
    6   6/
    
    b(i)/
    1   1.5
    2   2.0
    3   3.0
    4   4.0
    5   2.5
    6   1.0
    7   2.0
    /;
    
table c(j, i)  'profits j to i'
    1   2   3   4   5   6   7
1   4   4.5 2.5 0.5 1   0.5 -3.5
2   4   4.5 2.5 4.2 3.5 1.5 -0.5
3   3.5 5   4   3.5 4.5 1.5 0
4   1.3 3   5   3.3 5.5 1.8 1.3
5   0.5 1   1.5 5   4   5.5 3
6   -1  0   1.5 3.3 4   4.5 2;

variable
    Z;
positive variable
    x(i, j);

binary variable
    y(j);
    
equations
    obj
    demand_satisfaction_constraint(i)
    falicility_opening_constraint(j);
    
    obj.. Z =e= sum((i, j), c(j, i) * x(i, j)) - sum(j, f(j) * y(j));
    
    demand_satisfaction_constraint(i).. sum(j, x(i, j)) =e= b(i);
    
    falicility_opening_constraint(j).. sum(i, x(i, j)) =l= u(j) * y(j);
    
model my_model /all/;
solve my_model using mip maximizing Z;
display Z.l;
display y.l;
display x.l;