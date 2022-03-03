sets
i/1*8/;

parameters
g(i) beklenen getiri

/ 1 500, 2 750, 3 1000, 4 600, 5 500, 6 500, 7 450, 8 500/

y(i) baslang�c yat�r�m� / 1 425, 2 450, 3 550, 4 300, 5 150, 6 250, 7 350, 8 325/;

scalar B b�t�e /1500000/;

variable
x(i)
z ;

binary variable
x(i);

equations
obj
const;

obj.. z=E=sum(i,x(i)*(g(i)-y(i)));
const..sum (i, x(i)*y(i))=L=B;

model butce /all/;
solve butce using MIP maximizing z;
