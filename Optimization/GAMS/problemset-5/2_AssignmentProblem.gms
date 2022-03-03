SETS
    i /1*4/
    j /A, B, C, D/;


TABLE assignment_cost(j, i)
        1   2   3   4
    A   94  1   54  68
    B   74  10  88  82
    C   73  88  8   76
    D   11  74  81  21  ;
    

VARIABLES assigned_pos(i, j), Z;
BINARY VARIABLES assigned_pos;

EQUATIONS objective, assignment_1(i), assignment_2(j);
    objective.. Z =E= sum((i, j), assignment_cost(j, i) * assigned_pos(i, j));
    assignment_1(i).. sum(j, assigned_pos(i, j)) =E= 1;
    assignment_2(j).. sum(i, assigned_pos(i,j)) =E= 1;
    
MODEL assignment_model /all/;
SOLVE assignment_model using mip minimizing Z;
DISPLAY 'Result is: ', assigned_pos.l, Z.l;