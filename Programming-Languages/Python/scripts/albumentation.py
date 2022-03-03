import albumentations as A
import cv2, glob
import seaborn
import matplotlib.pyplot as plt
import sys

print("\n the file is working" + sys.argv[0] + "...\n")
transform = A.Compose(
    # konmak istenenler buraya konabilir
    [   
        A.Rotate(10),
        A.RandomBrightnessContrast(p=0.4),
        
    ]
)

# simdi once oku ve kac tane olduklarini bul
dict_amounts = {}
itype = input("give the image type:\n> ")
for i in range(91):
    dict_amounts[str(i)] = len(glob.glob(f"{i}/*.{itype}"))

x = list(dict_amounts.keys())
y = list(dict_amounts.values())

del x;del y
descending_sorted = sorted(dict_amounts.items(), key=lambda x: x[1])
x = []
y = []

for _x, _y in descending_sorted:
    x.append(_x)
    y.append(_y)

x.reverse()
y.reverse()
limit = max(y)

dict_amounts = {int(key):value for key, value in zip(x, y)}
total = 0
_count = 1
for dir, amount in dict_amounts.items():
    print(f"at {_count}.")
    dir = str(dir)
    times = round(limit / amount) # I have how many times I am to do it
    _count += 1
    if amount == limit:
        continue
    for image in glob.glob(dir + "/*.{{itype}}"):
        img = cv2.imread(image)
        for n in range(times):
            total += 1
            transformed = transform(image=img)
            transformed_img = transformed['image']
            cv2.imwrite(f"{dir}/{n}" + image.strip(f"{dir}/"), transformed_img)
            # print(f"{dir}/{n}" + image.strip(f"{dir}/"))
    
    
print(total, "many times it has been done")
