Sets
i jobs /1*4/
k positions /1*4/;

variables
x(i, k)
c(k)
t(k)
z;
binary variables
x;
positive variables
t;
parameters
process_time(i)
/1 16
 2 7
 3 10
 4 18/
due_time(i)
/1 20
 2 15
 3 14
 4 23/;
 
equations
completion_time(k)
tardiness(k)
objective
jobs(i)
positions(k);

completion_time(k).. c(k)=e=c(k-1)+sum(i,process_time(i)*x(i,k));
tardiness(k).. c(k)-sum(i,due_time(i)*x(i,k))=l=t(k);
objective.. z=e=sum(k,t(k));
jobs(i).. sum(k, x(i,k))=e=1;
positions(k).. sum(i, x(i,k))=e=1;

model schedule /all/
solve schedule using mip minimizing z
display
x.l,z.l,t.l


