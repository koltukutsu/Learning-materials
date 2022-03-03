Set
    i /women-c, men-c, jeweler, shoes, cafe, market/
    j amounts /1*3/;
scalar total_needed_area;
        total_needed_area = 3000;
        
parameters
    store_and_area(i) /women-c 400, men-c 300, jeweler 50, shoes 200, cafe 500, market 1000/
    minimums(i) /women-c 1, men-c 1, jeweler 0, shoes 1, cafe 1, market 0/
    maximums(i) /women-c 3, men-c 3, jeweler 2, shoes 3, cafe 2, market 1/;
    
table profit_for_stores(i, j)
            1       2       3
women-c     120     100     70
men-c       80      60      40
jeweler     50      30      0
shoes       75      55      40
cafe        100     70      0
market      250     0       0;

variable
    Z;
binary variable
    x(i, j);

Equations
    obj
    area_limit
    store_amount(i);
    
    obj.. Z =E= sum((i,j), x(i,j) * profit_for_stores(i, j));
    area_limit.. sum((i,j), store_and_area(i) * ord(j) * x(i,j)) =L= total_needed_area;
$onText
Isn't there a problem with deciding the minimum and the maximum amount of the stores,
or interestingly the program can handle it???

As we can claerly see from the result, there is no varying options in terms of store number opened
$offText
    store_amount(i).. sum(j, x(i,j)) =E= 1;

model mall_problem_model /all/;
solve mall_problem_model using mip minimizing Z;
display x.l, z.l, store_amount.l;