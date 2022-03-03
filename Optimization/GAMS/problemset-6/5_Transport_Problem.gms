sets i factories /1,2,3/
     j consumers /1*4/;
     
table c(i,j)
    1   2   3   4
1   8   6   10  9
2   9   12  13  7
3   14  9   16  5;

scalar fa /200000/;
parameter demand(j) /1 40000, 2 30000, 3 25000, 4 15000/;
parameter capacity(i) /1 60000, 2 55000, 3 45000/;

positive variables x(i,j);
binary variables y(i);
variable z;

equations obj, capacity_limit, demand_limit;

obj.. z =e= sum((i,j), x(i,j)*c(i,j)) + fa*sum(i,y(i));
capacity_limit(i).. sum(j, x(i,j)) =l= capacity(i) * y(i);
demand_limit(j).. sum(i, x(i,j)) =g= demand(j);

model transport /all/;
solve transport using mip minimizing z;
display x.l, y.l;