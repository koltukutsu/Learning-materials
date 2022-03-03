$set startcity 1

sets
    i /1
    2
    3
    4
    5
    6/;
    
alias(i, j);

table c(i,j)
    1   2   3   4   5   6
1       477 450 155 950 680
2           586 330 900 450
3               388 490 485
4                   810 546
5                       612
6
;
c(i,j)$(ord(i)=ord(j)) = 1000;
c(i,j)$(ord(i)<>ord(j)) = max(c(i,j), c(j,i));

table t(i,j)
    1   2   3   4   5   6
1       384 322 174 625 540
2           420 208 616 340
3               230 300 370
4                   550 390
5                       450
6
;

t(i,j)$(ord(i)=ord(j)) = 1000;
t(i,j)$(ord(i)<>ord(j)) = max(t(i,j), t(j,i));

scalars P 'number of cities to visit'
    M 'number of salesman' /1/
    ;
P = card(i);

set arcs(i,j);
arcs(i,j)$c(i,j) = yes;
set i0(i) /%startcity%/;
set i2(i);
i2(i)$(not i0(i)) = yes;

parameters
    tw(i)/
    1   0
    2   60
    3   75
    4   30
    5   45
    6   15/;
    
variable
    Z
    tt;
positive variable
    u(i) 'dummy variable';
binary variable
    x(i, j);

equations
    obj
    start_constraint
    end_constraint
    to_each_city_constraint(i)
    from_each_city_constraint(j)
    total_time_constraint
    subtour_elimination_constraint(i, j);
    
    obj.. Z =e= sum(arcs, c(arcs) * x(arcs));
    total_time_constraint.. tt =e= sum((i, j), x(i,j) * t(i,j)) + sum(i, tw(i));
    
    start_constraint..  sum(i2(j), x('%startcity%', j)) =e= M;
    end_constraint..    sum(i2(i), x(i, '%startcity%')) =e= M;
    
    to_each_city_constraint(i)..    sum(arcs(i,j), x(i,j)) =e= 1;
    from_each_city_constraint(j)..  sum(arcs(i,j), x(i, j)) =e= 1;
    
    subtour_elimination_constraint(arcs(i, j))$(i2(i) and i2(j)).. u(i) - u(j) + P*x(i,j) =l= P-1
    

model my_model /all/;
solve my_model minimizing Z using mip;
solve my_model minimizing tt using mip;

display Z.l, tt.l, x.l;
display i2;


    
