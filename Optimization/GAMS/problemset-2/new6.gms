sets
i depot and customers /ziraat, asagi, atalar, cavusoglu,
                      orhantepe, carsi, topselvi, hurriyet,
                      soganlik, cevizli, ugurmumcu/

k vehicles            /vehicle7/;


alias (i,j,r);

table d(i,j) distance travelled to j from i (kilometer)
           ziraat  asagi   atalar   cavusoglu   orhantepe   carsi   topselvi   hurriyet   soganlik   cevizli   ugurmumcu
ziraat     10000   9       4.3      9.4         3.5         7.6     7.1        8.7        5          2.5       6.8
asagi              10000   2.7      0.6         3.9         5.2     1.6        6.5        6.3        4.1       6.9
atalar                     10000    2.7         2           7       3.3        8          4.4        2.7       6.8
cavusoglu                           10000       4.2         4.8     1.1        6.1        5.9        5.5       6.5
orhantepe                                       10000       7.6     4.5        8.7        4.8        1.4       8
carsi                                                       10000   4.8        2.9        2.3        5.5       2.5
topselvi                                                            10000      4.5        4.7        4.8       5.3
hurriyet                                                                       10000      4.5        6.3       5.6
soganlik                                                                                  10000      3.6       3.2
cevizli                                                                                              10000     5.6
ugurmumcu                                                                                                      10000
;

d(i,j) = max(d(i,j),d(j,i));

table t(i,j) travel time between i and j (hour)
          ziraat asagi   atalar   cavusoglu   orhantepe   carsi   topselvi   hurriyet   soganlik   cevizli   ugurmumcu
ziraat    10000  0.23    0.15     0.2         0.1         0.15    0.12       0.15       0.12       0.07      0.16
asagi            10000   0.15     0.13        0.2         0.23    0.1        0.25       0.25       0.22      0.25
atalar                   10000    0.18        0.1         0.25    0.15       0.23       0.18       0.13      0.25
cavusoglu                         10000       0.2         0.18    0.05       0.18       0.2        0.2       0.2
orhantepe                                     10000       0.27    0.18       0.25       0.2        0.1       0.25
carsi                                                     10000   0.15       0.15       0.1        0.2       0.12
topselvi                                                          10000      0.13       0.15       0.17      0.15
hurriyet                                                                     10000      0.15       0.17      0.16
soganlik                                                                                10000      0.13      0.15
cevizli                                                                                            10000     0.16
ugurmumcu                                                                                                    10000;

t(i,j) = max(t(i,j),t(j,i));

parameters
q(i) demand at point i (tl) /
ziraat           0
asagi            221694
atalar           417194
cavusoglu        317319
orhantepe        286120
carsi            179131
topselvi         284393
hurriyet         261559
soganlik         395627
cevizli          243346
ugurmumcu        430101 /

a(k) capacity of vehicle (tl) /
vehicle7   10000000/

w(k) sabit maliyet /
vehicle7   1050/

e(i) earliest time to start to service /
ziraat       0
asagi        0
atalar       0
cavusoglu    0
orhantepe    0.5
carsi        1
topselvi     2
hurriyet     2.5
soganlik     1.5
cevizli      0
ugurmumcu    1.5/

l(i) latiest time to start to service /
ziraat       1000
asagi        3
atalar       3.5
cavusoglu    2.3
orhantepe    3
carsi        1.5
topselvi     4
hurriyet     3.5
soganlik     2.5
cevizli      1.5
ugurmumcu    2.5/

s(i) service time (minutes)/
ziraat       0
asagi        0.25
atalar       0.25
cavusoglu    0.25
orhantepe    0.25
carsi        0.25
topselvi     0.25
hurriyet     0.25
soganlik     0.25
cevizli      0.25
ugurmumcu    0.25/

scalar tk /1/;

scalar fp /4.5/;

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
cons5(r, k)

cons16(i)
cons17(k)
cons18(i,k)
cons19(i,j,k)
cons20(i,k)
cons21(i,k)
;

obj.. z =e= (fp*(sum((i,j,k),(0.08*d(i,j)*x(i,j,k))+(0.02*t(i,j)*tk*x(i,j,k))))+ sum(k,(w(k)*p(k))));
cons1(i,k).. sum(j, x('ziraat',j,k)) =e= p(k);
cons5(r, k).. sum(i,x(i,r,k))-sum(j,x(r,j,k))=e=0;

cons16(i2(i)).. sum(k,y(i,k))=g=1;
cons17(k).. sum(i2(i),q(i)*y(i,k))=l=a(k);
cons18(i2(i),k).. y(i,k)=l=sum(j,x(j,i,k));
cons19(i2(i),i3(j),k).. b(i,k)+s(i)+t(i,j)-(l(i)+t(i,j)-e(j))*(1-x(i,j,k))=l=b(j,k);
cons20(i2(i),k).. e(i)=l=b(i,k);
cons21(i2(i),k).. b(i,k)=l=l(i);

model buraktez /all/;
solve buraktez using mip minimizing z;

