from plotting import plot_it
import math
def bisection(f,a,b,N):
    '''Approximate solution of f(x)=0 on interval [a,b] by bisection method.

    Parameters
    ----------
    f : function
        The function for which we are trying to approximate a solution f(x)=0.
    a,b : numbers
        The interval in which to search for a solution. The function returns
        None if f(a)*f(b) >= 0 since a solution is not guaranteed.
    N : (positive) integer
        The number of iterations to implement.

    Returns
    -------
    x_N : number
        The midpoint of the Nth interval computed by the bisection method. The
        initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0 for some
        midpoint m_n = (a_n + b_n)/2, then the function returns this solution.
        If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
        iteration, the bisection method fails and return None.

    Examples
    --------
    >>> f = lambda x: x**2 - x - 1
    >>> bisection(f,1,2,25)
    1.618033990263939
    >>> f = lambda x: (2*x - 1)*(x - 3)
    >>> bisection(f,0,1,10)
    0.5
    '''
    if f(a)*f(b) >= 0:
        print("Bisection method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Bisection method fails.")
            return None
        print('~~~~~~~~~~~~~~~~~~~~~')
        print("Iteration{",n,"}")
        print(f"Below >> {a_n} \nUp >> {b_n}")
    print("~~~~~~~~~~~~~~")
    return (a_n + b_n)/2

f = lambda x: x**10 - 1
result = bisection(f,0, 1.3, 1000)
print("X >> ", result)
print("f(X) >> ", f(result))
print(f((0.377 - (0.5) * (-.459)) / (f(0.5)- f(1))))
# print(f(2.375))
E = 10**(-3) ## limit value
# plot_it()
# for N in range(50):
    
    # print(f"This is {N} iteration {bisection(f,1,2, N)} and:", abs(f(bisection(f,1,2, N))) <= E, f"result {f(bisection(f,1,2, N))}")