Sets
    i parts/1*5/
    j products/1*3/;

Parameters
    stock(i) / 1 450, 2 250, 3 800, 4 450, 5 600/
    profit(j) /1 75, 2 50, 3 35/
    
    lcd(i) /1 1, 2 1, 3 2, 4 1, 5 2/
    m_player(i) /1 1, 2 0, 3 2, 4 1, 5 1/
    speaker(i) /1 0, 2 0, 3 1, 4 0, 5 1/;

Variable
    Z;
positive variable amount(i);

Equations
    obj;
    obj.. Z=E= sum(j, amount(j) * profit(j))
