sets
    i 'destinations'/1*6/
    k 'vehicles'/1*4/
    p 'products'/1*3/
    ;
    
alias(i, j, r);

table d(i, j) 'distances'
    1   2   3   4   5   6
1       5   4   6   8   7
2   5       2   4   6   3
3   4   2       3   5   5
4   6   4   3       1   7
5   8   6   5   1       4
6   7   3   5   7   4
;
d(i,j)$(ord(j)=ord(i)) = 1000;

table q(i,p)
    1   2   3
1   0   0   0
2   0   0   0
3   35  5   10
4   90  10  10
5   15  5   5
6   30  15  20;

parameters
    cap(k) 'capacity'/
    1   20
    2   70
    3   30
    4   20/
    f(k) 'fixed cost'/
    1   650
    2   1000
    3   700
    4   650/
    v(k)'variable cost'/
    1   5
    2   7
    3   6
    4   6/
    
    e(i)'earlist time'/
    1   0
    2   0
    3   50
    4   116
    5   149
    6   34/
    l(i)'latest time'/
    1   230
    2   171
    3   60
    4   126
    5   159
    6   44/
    s(i)'service time'/
    1   0
    2   0
    3   10
    4   10
    5   10
    6   10/
    t(i,j)'time from i to j';

t(i,j)=10;
    
parameter c(i, j, k);
c(i, j, k)=d(i,j) * v(k);

variable Z;
binary variable
    x(i,j,k) 'vehicle positions'
    ;
integer variable
    u(i) 'dummy variable to satisfy the constraints'
;
positive variables
    b(i, k) 'moment at which service begins at customer i by vehicle k'
    y(i,k,p) 'split capacity coming from different vehicles for the demand'
;

equations
    obj
    starting_conditons_constraint(j)
    ending_conditions_constraint(i)
    
    inner_conditions_constraint(i, k)
    inner_conditions_constraint_2(j, k)
    
    go_turn_back_constraint(r, k)
    
    demand_and_capacity_constraint(k)
    
    dummy_time_constraint(i)
    dummy_time_constraint_2(i)
    
    time_constraint(i, j, k)
    
    split_supply_constraint(i,p)
    split_supply_and_position_constraint(i, k,p)
    
    the_constraint_that_I_do_not_know(i, j, k)
    earliest_optimum_latest(i, k)
    earliest_optimum_latest_2(i, k)
    ;
    
    obj.. Z =e= sum((i,j,k), c(i,j,k) * x(i,j,k)) + sum((i,j,k)$(ord(i)le 2 and ord(j)ge 3), f(k) * x(i,j,k));
    starting_conditons_constraint(j).. sum((i,k), x(i,j,k)) =g= 1;
    ending_conditions_constraint(i).. sum((j,k), x(i,j,k)) =g= 1;
    
    inner_conditions_constraint(i,k).. sum(j$(ord(j) ge 3), x(i,j,k)) =l= 1;
    inner_conditions_constraint_2(j,k).. sum(i$(ord(i) ge 3), x(i,j,k)) =l= 1;
    
    go_turn_back_constraint(r, k).. sum(i, x(i,r,k)) =e= sum(j, x(r, j, k));
    
    demand_and_capacity_constraint(k).. sum((i,p)$(ord(i)ge 3), q(i,p) * y(i, k, p)) =l= cap(k);
    
    dummy_time_constraint_2(i)$(ord(i)ge 3).. u(i) =l= 6;
    dummy_time_constraint(i)$(ord(i)ge 3).. u(i)=g=3;
    
    
    time_constraint(i, j, k)$(ord(i)ge 3 and ord(j) ge 3).. u(i) - u(j) + 1 =l= 5*(1-x(i,j,k));
    
    split_supply_constraint(i,p)$(ord(i)ge 3).. sum(k, y(i,k,p)) =e= 1;
    split_supply_and_position_constraint(i, k, p)$(ord(i)ge 3).. y(i,k,p) =l= sum(j, x(j,i,k));
    
    the_constraint_that_I_do_not_know(i,j,k)$(ord(i)ge 3 and ord(j)ge 3).. b(i,k) + s(i) + t(i,j) - (l(i)+t(i,j)-e(j)) * (1 - x(i,j,k)) =l= b(j,k);
    earliest_optimum_latest(i, k)$(ord(i)ge 3).. e(i)=l=b(i,k);
    earliest_optimum_latest_2(i, k)$(ord(i)ge 3).. b(i,k)=l=l(i);
    

model my_model /all/;
solve my_model using mip minimizing Z;
display Z.l, x.l, y.l, u.l, b.l;
