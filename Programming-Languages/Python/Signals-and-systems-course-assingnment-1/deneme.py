from convolution import myconv
import numpy as np
from sys import exit as ext

#I have written this code to compare whether myconv and numpys' one produce the same result
Y_function = np.array([1])
Y_function = np.append(Y_function, np.zeros((398)))
Y_function = np.append(Y_function, 0.4)
Y_function = np.append(Y_function, np.zeros(399))
Y_function = np.append(Y_function, 0.4)
print(Y_function)
print(len(Y_function))
print(Y_function[0])
print(Y_function[399])
print(Y_function[799])
print(len(Y_function))
# ext()

first = np.random.randint(4000, size=(300000))
second= np.random.randint(4000, size=(3))

res_1, _ = myconv(first, 0, second, 0)
res_2 = np.convolve(first, second)

print(all(res_1 == res_2))

res_1, _ = myconv(second, 0, first, 0)
res_2 = np.convolve(first, second)

print(all(res_1 == res_2))

res_1, _ = myconv(first, 0, second, 0)
res_2 = np.convolve(second, first)

print(all(res_1 == res_2))

res_1, _ = myconv(second, 0, first, 0)
res_2 = np.convolve(second, first)

print(all(res_1 == res_2))
ext()