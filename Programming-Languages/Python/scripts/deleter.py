from glob import glob
import random
import os
import sys
print("\n the file is working" + sys.argv[0] + "...\n")
_counted = [item for item in glob("*[!A-z.]")]


#####
itype = input("give the image type:\n>")
dict_amounts = {}
for i in _counted:
    dict_amounts[str(i)] = len(glob(f"{i}/*.{itype}"))

x = list(dict_amounts.keys())
y = list(dict_amounts.values())

del x;del y
descending_sorted = sorted(dict_amounts.items(), key=lambda x: x[1])
# print(*descending_sorted, sep="\n")
x = []
y = []

for _x, _y in descending_sorted:
    x.append(_x)
    y.append(_y)

x.reverse()
y.reverse()
under_limit = min(y)

###
new_dir_name = input(" give the name of the new directory\n which you wanted to move the excessive materials:\n>") 
try:
    os.mkdir(new_dir_name)
except FileExistsError:
    pass
print("file has been initiated")
    
for dirr, amount in zip(x, y):
    randomly_deleted = amount - under_limit
    if randomly_deleted > 0:
        all_images = glob(f"{dirr}/*.{itype}")
        print(randomly_deleted)
        print(len(all_images))
        to_delete = random.sample(all_images, k=randomly_deleted)
        # print(to_delete)
        try:
            os.mkdir(new_dir_name + "/" + dirr)
        except FileExistsError:
            pass
        for _from in to_delete:
            to = new_dir_name + "/" + dirr + "/" + _from.split("/")[-1]
            os.rename(_from, to)
    else:
        continue
