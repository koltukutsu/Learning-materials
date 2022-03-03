sets
i depot and customers /ziraat, asagi, atalar, cavusoglu/

k vehicles            /vehicle1, vehicle2/;


alias (i,j);

table d(i,j) distance travelled to j from i (kilometer)
           ziraat  asagi   atalar   cavusoglu
ziraat     10000   9       4.3      9.4
asagi              10000   2.7      0.6
atalar                     10000    2.7
cavusoglu                           10000

;

d(i,j) = max(d(i,j),d(j,i));

table t(i,j) travel time between i and j (hour)
          ziraat asagi   atalar   cavusoglu
ziraat    10000  0.23    0.15     0.2
asagi            10000   0.15     0.13
atalar                   10000    0.18
cavusoglu                         10000
;

t(i,j) = max(t(i,j),t(j,i));

parameters
q(i) demand at point i (tl) /
ziraat           0
asagi            221694
atalar           417194
cavusoglu        317319  /

a(k) capacity of vehicle (tl) /
vehicle1   1000000
vehicle2   1000000/

w(k) sabit maliyet /
vehicle1   150
vehicle2   150/

e(i) earliest time to start to service /
ziraat       0
asagi        0
atalar       0
cavusoglu    0/

l(i) latiest time to start to service /
ziraat       1000
asagi        1000
atalar       1000
cavusoglu    1000/

s(i) service time (minutes)/
ziraat       0
asagi        0.25
atalar       0.25
cavusoglu    0.25 /



set i0(i) /ziraat/;

set i1(j) /ziraat/;

set i2(i);
i2(i)$(not i0(i)) = yes;

set i3(j);
i3(j)$(not i1(j)) = yes;

variables
z;
positive variables
b(i,k)
b(j,k)
y(i,k)
p(k);

binary variables
x(i,j,k)
x(j,i,k)
;

equations
obj
cons1(i,k)
cons5(k)
cons6(k)
cons7(k)
cons8(k)

cons16(i)
cons17(k)
cons18(i,k)
cons19(i,j,k)
cons20(i,k)
cons21(i,k)
;

obj.. z =e= (sum((i,j,k),(0.08*d(i,j)*x(i,j,k))+(0.02*t(i,j)*x(i,j,k)))+ sum(k,(w(k)*p(k))));
cons1(i,k).. sum(j, x('ziraat',j,k)) =e= p(k);
cons5(k).. sum(i,x(i,"ziraat",k))-sum(j,x("ziraat",j,k))=e=0;
cons6(k).. sum(i,x(i,"asagi",k))-sum(j,x("asagi",j,k))=e=0;
cons7(k).. sum(i,x(i,"atalar",k))-sum(j,x("atalar",j,k))=e=0;
cons8(k).. sum(i,x(i,"cavusoglu",k))-sum(j,x("cavusoglu",j,k))=e=0;

cons16(i2(i)).. sum(k,y(i,k))=g=1;
cons17(k).. sum(i2(i),q(i)*y(i,k))=l=a(k);
cons18(i2(i),k).. y(i,k)=l=sum(j,x(j,i,k));
cons19(i2(i),i3(j),k).. b(i,k)+s(i)+t(i,j)-(l(i)+t(i,j)-e(j))*(1-x(i,j,k))=l=b(j,k);
cons20(i2(i),k).. e(i)=l=b(i,k);
cons21(i2(i),k).. b(i,k)=l=l(i);

model lessdatatez /all/;
solve lessdatatez using mip minimizing z;

