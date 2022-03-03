Sets
    i factories /1*3/
    j customers /1*4/;
    
parameters
    capacities(i) /1 60000, 2 55000, 3 45000/ 
    demands(j) /1 40000, 2 30000, 3 25000, 4 15000/;
    
scalar opening_cost factory opening cost;
    opening_cost = 200000;

table cost_of_sending(i, j)
    1   2   3   4
1   8   6   10  9
2   9   12  13  7
3   14  9   16  5   ;
    
Variable
    z;
Positive Variable
    x(i, j);
Binary Variable
    y(i);
    
Equations
    obj
    not_exceed_capacity(i)
    satisfy_demand(j);
    
    obj.. z =E= sum((i,j), cost_of_sending(i,j) * x(i, j)) + sum(i, y(i) * opening_cost);
    not_exceed_capacity(i).. sum(j, x(i, j)) =L= capacities(i) * y(i);
    satisfy_demand(j).. sum(i, x(i, j)) =G= demands(j);

Model trans /all/;
Solve trans using mip minimizing z;
display x.l, z.l;