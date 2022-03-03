sets
    i /seattle, san-diego/
    j /new-york, chicago, topeka/;
    
Parameters
    a(i) capacity of plant i in cases
    /   seattle     350
        san-diego   600 /
    b(i) demand at market j in cases
    /   new-york   325
        chicago    300
        topeka     275  /;
        
table d(i,j) distance in thousands of miles
            new-york    chicago     topeka
seattle         2.5         1.7     1.8
san-diego       2.5         1.8     1.4;

scalar f freight in dollars per case per thousand miles /90/;

Parameter c(i,j) transport cost in thousands of dollars per case;
    c(i,j) = f* d(i,j) / 1000;
    
variables
    x(i,j) shipment quantities in cases
    z      total transportation costs in thousand of dollars;

positive variable x;

Equations
    cost
    supply(i)
    demand(j);
    
cost.. z =e= sum((i,j), c(i,j)*x(i,j));
supply(i).. sum(j, x(i,j)) =l= a(i);
demand(j).. sum(i, x(i,j)) =g= b(j);

model transport /all/;
solve transport using lp minimizing z;
display x.l, x.m;