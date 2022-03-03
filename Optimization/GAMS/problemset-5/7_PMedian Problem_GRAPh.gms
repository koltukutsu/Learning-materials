Set
    i represents all the letters from A to B /1*8/;
    
Alias(i,j);

Parameters
    demand(i) /1 3, 2 3, 3 2, 4 3, 5 5, 6 4, 7 4, 8 2/;
Scalars n, p;
    n = 8;
    p = 2;
table costs(i, j)
    1   2   3   4   5   6   7   8
1   0   16  12  29  14  34  28  48
2   16  0   28  33  18  34  12  32
3   12  28  0   18  26  33  40  50
4   29  33  18  0   15  15  30  32
5   14  18  26  15  0   20  15  35
6   34  34  26  15  20  0   22  17
7   28  12  40  30  15  22  0   20
8   48  32  50  32  35  17  20  0   ;

variables
        Z;
binary variables
    x(i, j) whether the facility is assigned to a customer
    y(j) whter the facility is opened;

Equations

    obj, const1(i), const2(i,j), const3;
    
    obj.. Z =E= sum((i,j), costs(i,j) * x(i, j) * demand(i));
    const1(i).. sum(j, x(i,j ))=e=1;
    const2(i,j).. x(i,j) =L= y(j);
    const3.. sum(j, y(j))=e=p;
    
    
model first /all/;
solve first using mip minimizing Z;