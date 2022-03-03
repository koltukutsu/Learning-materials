Sets
    i cities /0*9/
    k vehicles /1*12/;
*/istanbul(depot),ankara,adana,bursa,g.antep,izmir,izmit,bodrum,alanya,konya/;
alias(i,j,s);

parameters
m(i) demand in city i /
    0 0
    1 25284
    2 9624
    3 10237
    4 15818
    5 4191
    6 8716
    7 25557
    8 19490
    9 8892 / ;

scalar
    vcap  vehicle capacity in desi  /17000/
    inc  cost of holding an inventory in warehouse /0.3/
    a a very large number /10000/;

table c(i,j) cost of transport between each city
   0      1      2      3      4     5      6      7      8       9
0 10000  400    738    203    881   432    158    565    568     529
1 400   10000   467    389    598   532    360    564    507     299
2 738    467   10000   716    264   761    712    740    515     258
3 203    389    716   10000   868   345    208    505    506     463
4 881    598    264    868   10000  913    846    892    666     521
5 432    532    761    345    913  10000   440    277    433     208
6 158    360    712    208    846   440   10000   600    556     513
7 565    564    740    505    892   277    600   10000   337     516
8 568    507    515    506    666   433    556    337  10000     364
9 529    299    258    463    521   208    513    516    364   10000 ;


variables
    Z;
positive variables
    d_satisfy(k,s)  demand met on point i
    minus(s) demand that can not be met on point i;
binary variables
    x(i,j,k);

EQUATIONS
$ontext
    obj
    satisfying_demands_constraint(k)
    
    forward_backward_constraint(s, k)
    
    starting_constraint(k)
    
    demand_constraint(s)

    city_supply_demand_constraint(k, j)
    
    do_not_return_from_the_same_path_constraint(k, i, j);
    
    obj.. Z =e= sum((i,j,k), c(i,j) * x(i,j,k)) + sum(s, minus(s) * 0.3);
    satisfying_demands_constraint(k).. sum((s), d_satisfy(k,s)) =l= 17000;  

    
    forward_backward_constraint(s,k).. sum(i$(ord(s) ne 1), x(i,s,k)) =g= sum(j$(ord(s) ne 1), x(s,j,k));
    
    starting_constraint(k).. sum((i,j)$(ord(j)ge 2), x('0', j, k)) =g= sum((i,j)$(ord(j)ge 2 and ord(i) ne ord(j)), x(i,j,k));
    
    demand_constraint(s).. sum(k, d_satisfy(k,s)) + minus(s) =e= m(s);
    
    city_supplY_demand_constraint(k, s).. sum(i, x(i,s,k)) * 10000 =g= d_satisfy(k, s);
    
    do_not_return_from_the_same_path_constraint(k, i, j).. x(i,j,k) + x(j,i,k) =l= 1;
$offtext
amac minimize total cost
arac(k) vehicle capacity constraint
girencikan(s,k) the ones that are entering should be greater than the ones that are leaving
depodancik(k) every vehicle should start their path from the warehouse
talep(s) demand constraint
rotaolsun(k,j) having as much paths to satisfy the demand
ciftler(k,i,j)  prevent using the same road while going back;

amac.. Z=e=sum((i,j,k),c(i,j)*x(i,j,k))+ sum(s, minus(s)*0.3);
arac(k).. sum((s), d_satisfy(k,s)) =l= 17000;
girencikan(s,k).. sum(i$(ord(s) ne 1),x(i,s,k))=g= sum(j$(ord(s) ne 1),x(s,j,k));
depodancik(k).. sum((i,j)$(ord(j) ge 2),x('0',j,k))=g= sum((i,j)$(ord(j) ge 2 and ord(i) ne ord(j)),x(i,j,k));
talep(s).. sum(k, d_satisfy(k,s)) + minus(s) =e= m(s);
rotaolsun(k,s).. sum(i, x(i,s,k))*100000 =g= d_satisfy(k,s) ;
ciftler(k,i,j).. x(i,j,k) + x(j,i,k) =l=1;


model my_model /all/;
solve my_model using mip minimizing Z;
display x.l, Z.l, d_satisfy.l, minus.l;
