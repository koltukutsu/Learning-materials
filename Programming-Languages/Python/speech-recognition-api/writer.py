from glob import glob

ma_list = list(glob("*.txt"))
ma_list = sorted(ma_list, key=lambda x:int(x.rstrip(".txt")))
print(ma_list)
with open("/home/semih/Documents/teknofest_yazi", "w") as final_txt:
    for item in ma_list:
        with open(item, "r") as txt:
            a = txt.readline()
            final_txt.write(" "+ a)
            
