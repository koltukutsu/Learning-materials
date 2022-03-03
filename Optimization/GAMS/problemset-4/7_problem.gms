option mip = cplex;
option lp = cplex;
option optcr = 0;
option reslim = 5000;
option iterlim = 5000;


Sets
i/1*3/
;

alias(i,j,k);

parameter p(j)/
1        1
2        1
3        3/;

parameter d(j)/
1        2
2        3
3        3/;

parameter r(j)/
1        12
2        6
3        3/;

scalar
M/1000/;


variable z;

binary variable y(j,k) j i�i k. s�raya atan�rsa 1 di�er durumda 0  ;

positive variables
C(j)   j isin tamamlanma zamani
W(j)   i i�i tamamland���nda j i�inin haz�r olmas� i�in beklenmesi gereken s�re
T(j)   j isinin gecikme zamani

equations
k1
k2
k3
k4
k5
k6

amac;

amac..
z=e=sum(j,T(j));

k1(j)..
C(j)=g=p(j)+r(j);

k2(i,j,k)$(ord(i)<>ord(j) and ord(k)>1)..
C(j)-C(i)+M*(2-y(j,k)-y(i,k-1))=g=p(j)-C(j);

k3(i,j,k)$(ord(i)<>ord(j) and ord(k)>1)..
W(j)+M*(2-y(j,k)-y(i,k-1))=g=r(j)-C(j);

k4(k)..
sum(j,y(j,k))=e=1;

k5(j)..
sum(k,y(j,k))=e=1;

k6(j)..
T(j)=g=C(j)-d(j);

model tekmakina/all/;
solve tekmakina using mip minimizing z;

