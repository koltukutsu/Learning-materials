Sets
i magazalar /1*6/
j sayilar /1*3/;

Variables
x(i,j) eger i. magazadan j tane acilirsa
z toplam gelir;
binary variables
x;

parameters
alan(i) i.magaza icin gerekli alan
/1 400
 2 300
 3 50
 4 200
 5 500
 6 1000/;
 
table kar(i,j) i.magazadan j tane acilmasi durumunda olusan kar
    1   2   3
1   120 200 210
2   80  120 120
3   50  60  0
4   75  110 120
5   100 140 0
6   250 0   0;

Equations
alankisiti toplam alan 3000m2'den az olmali
magazasayisi(i) acilacak magaza sayisi
amac toplam gelir maximum;

alankisiti..        sum((i,j), x(i,j) * alan(i)*ord(j)) =l= 3000;
amac..              z =e= sum((i,j), x(i,j) * kar(i,j));
magazasayisi(i)..   sum(j, x(i,j)) =e= 1;

model avm /all/
solve avm using mip maximizing z;
display x.l, z.l;