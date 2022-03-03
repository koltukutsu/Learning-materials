import math

# Implementing Newton Raphson Method

def newtonRaphson(f, g, h, x0, e, N):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break
        
        x1 = x0 - (f(x0) * g(x0)) / (g(x0)**2 - (f(x0) * h(x0)))
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1
        
        if step > N:
            flag = 0
            break
        
        condition = abs(f(x1)) > e
    
    if flag==1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')


# Input Section
x0 = input('Enter Guess: ')
e = input('Tolerable Error: ')
N = input('Maximum Step: ')

# Converting x0 and e to float
x0 = float(eval(x0))
e = float(eval(e))

# Converting N to integer
N = int(N)

# Defining Function
f = lambda x: (x-3) * (x-1) * (x-1)
# Defining derivative of function
g = lambda x: 3*x**2 - 10*x + 1 
h = lambda x: 6 * x - 10


#Note: You can combine above three section like this
# x0 = float(input('Enter Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Maximum Step: '))

# Starting Newton Raphson Method
newtonRaphson(f, g, h,x0, e, N)