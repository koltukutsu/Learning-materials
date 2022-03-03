Sets
    i PLANTS /Seattle, San-Diego/ 
    j MARKETS /New-York, Chicago, Topeka/;

Parameters
    capacities(i) /Seattle 350, San-Diego 600/
    demands(j)  /New-York 325, Chicago 300, Topeka 275/;

Table shipment_cost(i, j)
            New-York    Chicago     Topeka
Seattle     2.5         1.7         1.8
San-Diego   2.5         1.8         1.4 ;

Variable
    x(i, j) the places that I am going to send the goods
    Z;

Positive Variable x;

Equations obj, satisfy_demand(j), not_exceed_capacity(i);
    obj.. Z =E= sum((i, j), shipment_cost(i,j) * x(i,j));
    not_exceed_capacity(i).. sum(j, x(i,j)) =L= capacities(i);    
    satisfy_demand(j).. sum(i, x(i,j) ) =G= demands(j);
    
Model transport_model /all/;
Solve transport_model using lp minimizing Z;
DISPLAY x.L, Z.L;

scalar result;
    result = sum(i, capacities(i));
display result;