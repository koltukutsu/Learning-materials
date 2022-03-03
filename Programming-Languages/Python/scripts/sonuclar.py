from glob import glob
import sys
import seaborn as sns 
import matplotlib.pyplot as plt
print("\n the file is working" + sys.argv[0] + "...\n")
def included():
	pass


_counted = [item for item in glob("*[!A-z.]")]
print("Directories are:")
import time; time.sleep(1.5)
print(*_counted, sep="\n")
print("\n")
itype = input("COMMON Image type are: ")

counted = {}
for i in _counted:
    counted[int(i)] = len(glob(f"{int(i)}/*.{itype}"))
first = list(counted.keys())
second = list(counted.values())

plt.figure(figsize=(30,30))
sns.barplot(x=first, y=second)
plt.xticks(rotation=90)
plt.savefig(input("Give the name of plot: \n>") + ".png")
