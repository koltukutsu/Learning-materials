def main():
    np.set_printoptions(threshold=np.inf)
    
    print(*grid, sep="\n") 
    engine()
    
def filler():
    array = grid[:]

def engine():
    drawer = 0
    drawer2 = 0
    while drawer2 < 16:
        grid[drawer2][drawer] = 1
        drawer += 1
        if drawer == 16:
            drawer2 += 1
            drawer = 0
        print(grid)
        # time.sleep(0.06)
    
if __name__ == "__main__":
    from matplotlib import pyplot as plt
    import numpy as np
    import time
    grid = np.zeros((16, 16))
    x_range = 16
    y_range = 16
    main()
    