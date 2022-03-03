option mip=cplex;
option lp=cplex;
option optcr=0;
option reslim=5000;
option iterlim=5000;

sets i/1*5/
k/1*25/;

alias (i,j);

scalar m/65/;

variable z;
binary variable x(i,j,k);

equations
amac
k1
k2
k3
k4
k5
k6

;

amac..
z=e=sum((i,j,k),x(i,j,k));

k1(k)..
sum((i,j),x(i,j,k))=e=1;

k2(i,j)..
sum((k),x(i,j,k))=e=1;

k3(i)..
sum((j,k),ord(k)*x(i,j,k))=e=m;

k4(j)..
sum((i,k),ord(k)*x(i,j,k))=e=m;

k5..
sum(i,sum(j$(ord(j)=ord(i)),sum(k,ord(k)*x(i,j,k))))=e=m;

k6..
sum((i,j)$(ord(i)+ord(j)=6),sum(k,ord(k)*x(i,j,k)))=e=m;


model sihirlikare /all/;
solve sihirlikare using MIP maximizing z;
display z.l,x.l;