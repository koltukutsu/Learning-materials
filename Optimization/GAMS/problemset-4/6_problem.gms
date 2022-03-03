option mip = cplex;
option lp = cplex;
option optcr = 0;
option reslim = 5000;
option iterlim = 5000;

Sets
i/1*10/;
alias(i,j,k);

table c(i,j)

         1       2       3       4       5       6       7       8       9       10
1        0       12      11      10      0       0       0       0       0       0
2        12      0       0       0       9       10      0       0       0       0
3        11      0       0       0       0       10      0       0       0       0
4        10      0       0       0       0       9       0       9       6       0
5        0       9       0       0       0       0       8       7       0       0
6        0       10      10      9       0       0       0       0       0       0
7        0       0       0       0       8       0       0       0       0       10
8        0       0       0       9       7       0       0       0       0       12
9        0       0       0       6       0       0       0       0       0       11
10       0       0       0       0       0       0       10      12      11      0;

scalar n/10/;
variable z;
binary variable x(i,j);

equations
k1
k2
k3
obj;

k1(i)$(ord(i)=1).. sum(j$(ord(j)>=2 and c(i,j)>0),x(i,j))=e=1;

k2(j)$(ord(j)=n).. sum(i$(ord(i)<=n-1 and c(i,j)>0),x(i,j))=e=1;

k3(k)$(ord(k)<>1 and ord(k)<>n).. sum(i$(c(i,k)>0),x(i,k))-sum(j$(c(k,j)>0),x(k,j))=e=0;

obj.. z=e=sum((i,j)$(c(i,j)>0),c(i,j)*x(i,j));

model shortest/all/;
solve shortest using MIP minimizing z;
