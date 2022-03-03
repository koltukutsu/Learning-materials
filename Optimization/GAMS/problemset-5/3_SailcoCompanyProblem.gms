set
    t years /1*4/;
    
parameters
    demands(t) /1 3500, 2 6000, 3 4288, 4 3200/;
variables
    x(t) normal production
    y(t) excessive work
    i(t) the boats in the inventory for the current season
    Z;
positive variables
x(t)
y(t)
i(t);

scalar
    production /40/
    cost_per_boat /400/
    additional_cost_per_boat /450/
    keeping_cost /20/
    limit /3000/;
    
equations objective, production_limit(t), decision_made_calculation(t);
    objective.. Z =E= sum(t, x(t) * 400 + y(t) * 450 + i(t) * 20);
    production_limit(t).. x(t) =L= limit;
    decision_made_calculation(t).. i(t) =E= i(t-1) + x(t) + y(t) - demands(t);
model sailco /all/;
solve sailco using mip minimizing Z;
display x.L, y.L, i.L, Z.L;