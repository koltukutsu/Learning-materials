import numpy as np


def myconv(x: list, n: int, y: list, m: int) -> tuple:
    times = len(x) + len(y) - 1
    # result = np.array([])
    result = []
    chosen = x[:] if len(x) < len(y) else y[:]
    second = y[:] if len(x) < len(y) else x[:]
    chosen = chosen[::-1]
    first_index = 1
    second_index = 1

    for i in range(times):
        if i < len(chosen):
            temp = np.array(chosen[len(chosen) - i - 1:])
            result.append((temp * second[:i + 1]).sum())
            # result = np.append(result, (temp * second[:i + 1]).sum())
        elif i < len(second):
            result.append((second[first_index:first_index + len(chosen)] * chosen).sum())
            # result = np.append(result, (second[first_index:first_index + len(chosen)] * chosen).sum())
            first_index += 1
        else: # the chosen matrix is going out of the bound
            temp = np.array(chosen[:-(second_index)])  #chosen[:times - i] is removed
            second_reverted = second[::-1][:len(chosen) - second_index]
            second_reverted = second_reverted[::-1]
            result.append((second_reverted * temp).sum())
            # result = np.append(result, (second_reverted * temp).sum())
            second_index += 1

    pos = n if n < m else m
    result = np.array(result)
    return (result, n)


if __name__ == "__main__":
    from matplotlib import pyplot as plt
    import sys
    # X = np.array(list(map(int, input("Give me the values for X:\n>>").split())))
#     N = int(input("Give n: "))
    # Y = np.array(list(map(int, input("Give me the values for Y:\n>>").split())))
    # M = int(input("Give m: "))
    # arr, pos = myconv(X, N, Y, M)
    # print(f"{pos}.th value at x = 0, its value: {arr[pos]}\nArray: {arr}")


    X = np.random.randint(20, size=(12))
    Y = np.random.randint(20, size=(3))
    N = 2
    M = 0

    arr, pos = myconv(X, N, Y, M)
    np_arr = np.convolve(X, Y)

    print(f"X ARRAY: {N}.th value at x = 0, its value: {X[N]}\nArray: {X}")
    print(f"Y ARRAY: {M}.th value at x = 0, its value: {Y[M]}\nArray: {Y}")
    print(f"MyConv ARRAY: {pos}.th value at x = 0, its value: {arr[pos]}\nArray: {arr}")
    #of library
    print(f"Numpy Library Convolution: {pos}.th value at x = 0, its value: {np_arr[pos]}\nArray: {np_arr}")
    #plotting part
    figure, axis = plt.subplots(2, 2)
    #X
    before_zero = N
    after_zero = len(X) - 1 - before_zero
    position_arr = list(range(-1, -(before_zero + 1), -1))[::-1]
    position_arr.extend(list(range(after_zero + 1)))
    print(position_arr)
    print(X)
    axis[0, 0].stem(position_arr, X)
    axis[0, 0].set_title("X array")

    #Y
    before_zero = M
    after_zero = len(Y) - 1 - before_zero
    position_arr = list(range(-1, -(before_zero + 1), -1))[::-1]
    position_arr.extend(list(range(after_zero + 1)))
    axis[0, 1].stem(position_arr, Y)
    axis[0, 1].set_title("Y array")

    #myconv
    before_zero = pos
    after_zero = len(arr) - 1 - before_zero
    position_arr = list(range(-1, -(before_zero + 1), -1))[::-1]
    position_arr.extend(list(range(after_zero + 1)))
    axis[1, 0].stem(position_arr, arr)
    axis[1, 0].set_title("MyConv Result")

    #of library
    before_zero = pos
    after_zero = len(np_arr) - 1 - before_zero
    position_arr = list(range(-1, -(before_zero + 1), -1))[::-1]
    position_arr.extend(list(range(after_zero + 1)))
    axis[1, 1].stem(position_arr, np_arr)
    axis[1, 1].set_title("Numpy Library Convolution")
    
    figure.text(0.5, 0.04, 'X coordinate', ha='center', va='center')
    figure.text(0.06, 0.5, 'Y coordinate', ha='center', va='center', rotation='vertical')
    plt.show()
    # print(all(np_arr == arr))
    
    sys.exit(0)