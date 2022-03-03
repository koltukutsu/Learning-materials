# north, east, south, west

N, M = list(map(int, input().split()))

taken = [list(map(int, input().split())) for _ in range(N)]

for lst in taken:
    for item in lst:
        binary = bin(item)[2:]
        l_bin = len(binary)
        binary = "0" * (4 - l_bin) + binary if (l_bin < 4) else binary
        print(binary, end=" ")
    print("\n")
