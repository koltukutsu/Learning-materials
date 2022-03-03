import numpy as np

#1
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

    pos = n if n > m else m
    result = np.array(result)
    return (result, pos)


if __name__ == "__main__":
    from matplotlib import pyplot as plt
    import sys
    import wave
    import sounddevice as sd
    import time
    from scipy.io.wavfile import write
    
    
    print("Ilk kisim convolution\n")
    X = np.array(list(map(int, input("X Dizisini Verin:\n>>").split())))
    N = int(input("N Degerini Verin (1. eleman icin 0): "))
    Y = np.array(list(map(int, input("Y Dizisini Verin:\n>>").split())))
    M = int(input("M Degerini Verin (1. eleman icin 0): "))

    # X = np.random.randint(20, size=(12))
    # Y = np.random.randint(20, size=(3))
    # N = 2
    # M = 0

    arr, pos = myconv(X, N, Y, M)
    np_arr = np.convolve(X, Y)

    print(f"X ARRAY: {N}. deger x = 0, degeri: {X[N]}\nArray: {X}")
    print(f"Y ARRAY: {M}. deger x = 0, degeri: {Y[M]}\nArray: {Y}")
    print(f"MyConv ARRAY: {pos}. deger x = 0, degeri: {arr[pos]}\nArray: {arr}")
    #of library
    print(f"Numpy Library Convolution: {pos}. deger x = 0, degeri: {np_arr[pos]}\nArray: {np_arr}")
    
    #2
    #plotting part
    figure, axis = plt.subplots(2, 2)
    #X
    before_zero = N
    after_zero = len(X) - 1 - before_zero
    position_arr = list(range(-1, -(before_zero + 1), -1))[::-1]
    position_arr.extend(list(range(after_zero + 1)))
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
    axis[1, 0].set_title("MyConv Sonuc")

    #of library
    before_zero = pos
    after_zero = len(np_arr) - 1 - before_zero
    position_arr = list(range(-1, -(before_zero + 1), -1))[::-1]
    position_arr.extend(list(range(after_zero + 1)))
    axis[1, 1].stem(position_arr, np_arr)
    axis[1, 1].set_title("Numpy Library Convolution")
    
    figure.text(0.5, 0.04, 'X kordinati', ha='center', va='center')
    figure.text(0.06, 0.5, 'Y kordinati', ha='center', va='center', rotation='vertical')
    plt.show()
    # print(all(np_arr == arr))
    
    
    #3 record the sound
    print("Simdi 5snlik ve 10snlik sesler kaydedilecek...")
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    
    FS = 44100
    print("5snlik ses kaydediliyor...")
    record_5sn = sd.rec(int(FS * 5), samplerate=FS, channels=2, dtype="int16") # ne olur ne olmaz 2 cahnnel ile kayit yapiyorum
    sd.wait()
    print("5snlik kayit 5snlik.wav olarak kaydediliyor...\n")
    write("5snlik.wav", FS, record_5sn)
    # sd.play(record_5sn, FS)
    time.sleep(5)
    
    print("10snlik ses kaydediliyor...\n")
    record_10sn = sd.rec(int(FS * 10), samplerate=FS, channels=2, dtype="int16")
    sd.wait()
    print("10snlik kayit 10snlik.wav olarak kaydediliyor...")
    write("10snlik.wav", FS, record_10sn)    
    ## Open the sounds
    print("\n'Convolution Uygulama ve Sesleri Dinleme Kismi'\n")
    print("Convolutionlar hesaplaniyor...")
    
    #4
    #read the sounds
    with wave.open("5snlik.wav", "r") as sn_5:
        data_sn5 = np.frombuffer(sn_5.readframes(-1), np.int16)  # -1 access all the data
        FS = sn_5.getframerate() # it is common for all of the sounds, I recoreded them as 44100 hz

    with wave.open("10snlik.wav", "r") as sn_10:
        data_sn10 = np.frombuffer(sn_10.readframes(-1), np.int16)  # -1 access all the data

    data_sn5.shape = -1, 2
    data_sn5 = data_sn5.T
    data_sn5_first_channel = data_sn5[0]

    data_sn10.shape = -1, 2
    data_sn10 = data_sn10.T
    data_sn10_first_channel = data_sn10[0]

    Y_function = np.array([1])
    Y_function = np.append(Y_function, np.zeros((398)))
    Y_function = np.append(Y_function, 0.4)
    Y_function = np.append(Y_function, np.zeros(399))
    Y_function = np.append(Y_function, 0.4)

    My_Y1, _ = myconv(data_sn5_first_channel, 0, Y_function, 0)
    My_Y2, _ = myconv(data_sn10_first_channel, 0, Y_function, 0)
    Y1 = np.convolve(data_sn5_first_channel, Y_function)
    Y2 = np.convolve(data_sn10_first_channel, Y_function)

    ## PLOTTING
    #figure, ((first, second), (my_5sn, my_10sn), (np_5sn, np_10sn)) = plt.subplots(3, 2)

    #first.stem(range(len(data_sn5_first_channel)), data_sn5_first_channel)
    #second.stem(range(len(data_sn10_first_channel)), data_sn10_first_channel)
    #my_5sn.stem(range(len(My_Y1)), My_Y1)
    #my_10sn.stem(range(len(My_Y2)), My_Y2)
    #np_5sn.stem(range(len(Y1)), Y1)
    #np_10sn.stem(range(len(Y2)), Y2)
    #print("is has been plotted now")
    #plt.show()
    ##

    # print(all(My_Y1 == Y1))
    # sys.exit(0)

    #5
    ## SOUNDING
    time.sleep(0.5)
    print("5snlik normal ses")
    sd.play(data_sn5_first_channel, FS)
    time.sleep(len(data_sn5_first_channel) / FS)
    print("10snlik normal ses")
    sd.play(data_sn10_first_channel, FS)
    time.sleep(len(data_sn10_first_channel) / FS)

    time.sleep(0.5)
    print("5snlik myconv uygulanmis convolutionlu ses")
    sd.play(My_Y1, FS)
    time.sleep(len(My_Y1) / FS)

    time.sleep(0.5)
    print("10snlik myconv uygulanmis convolutionlu ses")
    sd.play(Y1, FS)
    time.sleep(len(Y1) / FS)

    time.sleep(0.5)
    print("5snlik numpy.convolve uygulanmis convolutionlu ses")
    sd.play(My_Y2, FS)
    time.sleep(len(My_Y2) / FS)

    time.sleep(0.5)
    print("10snlik numpy.convolve uygulanmis convolutionlu ses")
    sd.play(Y2, FS)
    time.sleep(len(Y2) / FS)

    sys.exit(0)