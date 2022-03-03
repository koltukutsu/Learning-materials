sets
t zaman /1,2,3,4/  ;

parameters
d(t) t. donemde yelkenli talebi /1 30, 2 60, 3 75, 4 25/                 ;

positive variables
x(t)
y(t)
i(t)

variables
z ama�;

equations
objective
aylikUretim(t)
envanter(t);

objective.. z=e=400*sum(t,x(t))+ 450*sum(t,y(t)) + 20*sum(t,i(t));
aylikUretim(t)..x(t)=l= 40;
envanter(t)..i(t)=e=i(t-1)+ x(t) + y(t) - d(t)

model sailco /all/;

solve sailco using MIP minimizing z;