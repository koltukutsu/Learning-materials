set
t time /1,2,3,4/    ;

parameters
session sessional production rate /40/
d(t) the demand of sailbots at t'th session/1 30, 2 60, 3 75, 4 25/
normal_shift_cost /400/
extra_shift_cost /450/
keeping_cost /20/   ;

positive variables
x(t) normal produced sailbots at t'th session
y(t) extra produced sailbots at t'th session
i(t) kept sailboats at t'th session ;

Variables
z;

equations
objective
sessional_production(t)
inventory(t)    ;

objective.. z =e= normal_shift_cost*sum(t,x(t)) + extra_shift_cost*sum(t,y(t)) + keeping_cost*sum(t,i(t));
sessional_production(t).. x(t) =l= session;
inventory(t).. i(t) =e= i(t-1) + x(t) + y(t) - d(t);

model sail /all/;
solve sail using mip minimizing z;
display z.l;