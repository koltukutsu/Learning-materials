sets
    i customers /1*3/
    j factories /1*4/;

parameters
    capacities(i) /1 60000, 2 55000, 3 45000/
    demands(j) /1 40000, 2 30000, 3 25000, 4 15000/
    opening_cost /200000/;
    
table costs(i, j)
    1   2   3   4
1   8   6   10  9
2   9   12  13  7
3   14  9   16  5;

variable Z;
positive variables x(i, j);
binary variables y(i);

Equations
    obj,
    not_exceed_the_capacity(i), satisfy_the_demand(j);
    
    obj.. Z =E= sum((i,j), costs(i, j) * x(i, j)) + 200000 * sum(i, y(i));
    not_exceed_the_capacity(i).. sum(j, x(i,j)) =L= capacities(i) * y(i);
    satisfy_the_demand(j).. sum(i, x(i, j)) =G= demands(j);

model distribution /all/;
solve distribution using mip minimizing Z;
display x.l, Z.l;
    