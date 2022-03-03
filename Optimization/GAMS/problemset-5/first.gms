SETS
    i jobs /1*4/
    k positions /1*4/ ;


PARAMETERS
    de(i) delivery time /1 20, 2 15, 3 14, 4 23/
    pr(i) processing time /1 16, 2 7, 3 10, 4 18/;


VARIABLES
    pos(i, k) assigned positions
    tardiness(k)
    completion(k)
    Z;


BINARY VARIABLES
    pos;
POSITIVE VARIABLES
    tardiness;

    
EQUATIONS obj, completion_t(k), tardiness_t(k), jobs(i), positions(k);

    obj.. Z =E= sum(k, tardiness(k));
    completion_t(k).. completion(k) =E= completion(k-1) + sum(i, pr(i) * pos(i, k)); 
    tardiness_t(k).. completion(k) - sum(i, de(i) * pos(i, k)) =L= tardiness(k);
    jobs(i).. sum(k, pos(i, k)) =E= 01;
    positions(k).. sum(i, pos(i, k)) =E= 1;
    

MODEL delay_model /all/;
SOLVE delay_model using mip minimizing Z;
DISPLAY 'objective function when minimized: ', Z.l;