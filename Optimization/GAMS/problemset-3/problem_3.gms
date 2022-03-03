scalar M /1000/;
scalar N;

sets
    i/1*5/;

alias(i, j);

N = card(i);

table c(i,j)
    1   2   3   4   5
1       13  22  16  6   
2   13      29  29  8
3   22  29      11  30
4   16  20  11      20
5   6   8   30  20  
;

c(i,j)$(ord(i)=ord(j)) = M;

parameters
    a(i)/
    1   1
    2   2
    3   3
    4   4
    5   5/
    b(j)/
    1   1
    2   2
    3   3
    4   4
    5   5/;

variable
    Z;
binary variable
    x(i,j);

positive variable
    u(i) 'dummy variable'
    uu(j);
    
equations
    obj
    each_city_be_arrived_constraint(j)
    from_eacy_city_depature_constraint(i)
    single_tour_covering_constraint
    ;
    
    obj.. Z =e= sum((i, j), c(i, j) * x(i, j));
    
    each_city_be_arrived_constraint(j)..    sum(i, x(i,j)) =e= 1;
    
    from_eacy_city_depature_constraint(i).. sum(j, x(i,j)) =e= 1;
    
    single_tour_covering_constraint(i,j)$(ord(i)<>ord(j)).. u(i) - uu(j) + N * x(i,j) =l= N-1;
    

model my_model /all/;
solve my_model minimizing Z using mip ;
display Z.l, x.l, u.l;