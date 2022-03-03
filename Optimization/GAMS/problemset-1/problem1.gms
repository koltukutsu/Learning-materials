sets
    i 'i and j are the cities' /1*6/
    k 'vehicles' /1,2/;
    
alias(i, j);

scalar M 'big number' /1000/;

table c(i ,j) 'the distance from i to j'
    1   2   3   4   5   6
1       5   4   6   8   4
2   5       12  4   6   2
3   4   12      3   5   8
4   6   4   3       7   1
5   8   6   5   7       9
6   4   2   8   1   9
;

c(i,j)$(ord(i)=ord(j)) = M;

parameters
    v(k) 'capacities of the vehicles' /
    1   250
    2   250/
    d(j) 'demands of the cities' /
    3   110
    4   45
    5   200
    6   90/;
    
variable
    Z;
binary variable
    x(i,j,k);
positive variable
    u(i,k);

equations
    obj
    reach_to_demanders_constraint(j)
    subtour_constraint(j, i, k)
    forward_and_backward_constraint(i, k)
    split_of_vehicles_constraint(k)
    vehicle_capacity_and_demand_constraint(k);
    
    obj.. Z =e= sum((i,j,k), x(i,j,k)*c(i,j));
    
*$'this constraint makes us sure that every vehicle reaches to the demanding cities'
    reach_to_demanders_constraint(j)$(ord(j) ge 3).. sum((i, k), x(i,j,k)) =e= 1; 
    
*$'this constraint makes us sure that every vehicle'
    subtour_constraint(i, j, k)$(ord(i) ge 3 and ord(j) ge 3).. u(i,k)-u(j,k) + card(i) * x(i,j,k) =l= card(i) - 1;
    
*$'this ocnstraint makes us sure that every vehicle turns back from the path that it once went'
    forward_and_backward_constraint(i, k).. sum(j, x(i,j,k)) =e= sum(j, x(j,i,k));
    
*$'this constraint makes us sure that for one demanding point, the resources of the vehicles can be split up'
    split_of_vehicles_constraint(k).. sum((i,j)$(ord(i) le 2 and ord(j) ge 3), x(i,j,k)) =l= 1;
    
    vehicle_capacity_and_demand_constraint(k).. sum((i, j)$(ord(j) ge 3), x(i,j,k)*d(j)) =l= v(k);
    
model my_model /all/;
solve my_model using mip minimizing Z;
display x.l, u.l, Z.l;
    

    