
$set first 1
$set last 5

sets
    i /1*5/
    k /1,2/
    ;
alias(i, j);

set f(i) /%first%/;
set l(i) /%last%/;

set r(i);
r(i)$(not f(i) and not l(i)) = yes;

table t(i, j)
    1   2   3   4   5
1   0   5   4   6   8
2   5   0   2   4   6
3   4   2   0   3   5
4   6   4   3   0   1
5   8   6   5   1   0;

parameters
    s(i)/
    1   20
    2   35
    3   40  
    4   15
    5   30/
    start_min(i)/
    1   0
    2   3
    3   7
    4   9   
    5   12/
    end_max(i)/
    1   7
    2   10
    3   12
    4   14
    5   17/;
    
variable
    Z;
binary variable
    x(i,j,k);
    
integer variable
    u(i)
    service(i) 'choose the optimum time between min and max';

equations
    obj
    starting_constraint(k)
    ending_constraint(k)
    every_inner_nodes_are_visited_starting_constraint(r)
    every_inner_nodes_are_visited_ending_constraint(r)
    forward_and_backward_constraint(r)
    service_constraint(i,j,k)
    time_window_constraint(k)
    service_limit_constraint(i)
    service_limit_constraint_2(i)
    dummy_constraint(i)
    dummy_constraint_2(i)
    dummy_second_constraint(i,j,k);
    
    obj.. Z =e= sum((i,j,k)$(ord(i) ge 2 and ord(j) ge 2), s(i) * x(i,j,k));
    
    starting_constraint(k).. sum((j)$(ord(j) ge 2), x('1', j, k)) =e= 1;
    
    ending_constraint(k).. sum(i$(ord(i) le 4), x(i,'5',k)) =e= 1;
    
    every_inner_nodes_are_visited_starting_constraint(r).. sum((i, k)$(ord(i) le 4), x(i,r,k)) =l= 1;
    every_inner_nodes_are_visited_ending_constraint(r).. sum((j,k)$(ord(j) ge 2), x(r,j,k)) =l= 1;
    
    forward_and_backward_constraint(r).. sum((i,j)$(ord(i) le 4), x(i,r,k)) =e= sum((j,k)$(ord(j) ge 2), x(r,j,k));
    
    service_constraint(i,j,k).. service(i) + t(i,j) - service(j) =l= card(i) * (1 - x(i,j,k));
    
    time_window_constraint(k).. sum((i, j)$(ord(i) le 4 and ord(j) ge 2), t(i,j) * x(i,j,k)) =l= 60;
    
    service_limit_constraint(i).. start_min(i) =l= service(i);
    service_limit_constraint_2(i).. service(i) =g= end_max(i);
    
    dummy_constraint(i)$(ord(i) ge 2).. u(i) =l= 5;
    dummy_constraint_2(i)$(ord(i) ge 2).. 2 =l= u(i);
    
    dummy_second_constraint(i,j,k)$(ord(i) ge 2 and ord(j) ge 2).. u(i) - u(j) + 1 =l= 4*(1-x(i,j,k));
    
model my_model /all/;
solve my_model using mip minimizing Z;
display x.l, service.l, Z.l;