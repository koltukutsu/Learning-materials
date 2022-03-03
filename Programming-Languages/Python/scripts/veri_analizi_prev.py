from glob import glob
from cv2 import imread
from os import mkdir
from time import sleep
import csv


TXTS_PATH = "/home/semih/Documents/configuration files/new_ones/train"
TXTS_PATH = TXTS_PATH if TXTS_PATH[-1] != "/" else TXTS_PATH[:-1]
OUTPUT_PATH = TXTS_PATH + "/OUTPUTS/"
IMG_TYPE = "jpg"
TXTS = glob(TXTS_PATH + "/*.txt")


print("\nTOTAL COUNTED TXT FILES: ", len(TXTS), "\n")
counter = 0

# output folder
try:
    mkdir(OUTPUT_PATH)
except FileExistsError:
    print(OUTPUT_PATH + " is present")

# give a chance for the user to see the console
sleep(1.2)

# opening csv file to write
with open(OUTPUT_PATH + "detailed_output.csv", "w", newline="") as csvfile\
    , open(OUTPUT_PATH + "problematic_imgs.txt", "w") as problematics\
    , open(OUTPUT_PATH + "taken_order.txt", "w") as taken_order:
    FIELDNAMES = ["class", "x_position", "y_position", "image_position", "width", "height", "area"]
    writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)

    writer.writeheader()

    for txt in TXTS:
        img_path = txt.rstrip("txt") + IMG_TYPE

        img = imread(img_path)

        try:
            HEIGHT, WIDTH, _ = img.shape
            with open(txt) as txt_file:
                for data_line in txt_file:
                    """
                    W means image WIDTG
                    H means image HEIGHT
                    w means ABSOLUTE WIDTH
                    h means ABSOLUTE HEIGHT
                    (a, b) = Absolute x, y coordinates
                    YOLO FORMAT = <Class Number> <a/W> <b/H> <w/W> <h/H>
                    image Pos = 1 2
                                3 4
                    """
                    datas_in = data_line.split()
                    # Seperated datas from the file
                    a_over_W = float(datas_in[1])
                    b_over_H = float(datas_in[2])
                    w_over_W = float(datas_in[3])
                    h_over_H = float(datas_in[4])

                    # variables
                    class_no = datas_in[0]
                    x_position = a_over_W * WIDTH
                    y_position = b_over_H * HEIGHT
                    width = w_over_W * WIDTH
                    height = h_over_H * HEIGHT
                    area = width * height
                    img_position = None

                    # deciding the position of label
                    if w_over_W >= 0.5 and h_over_H >= 0.5:
                        img_position = "2"
                    elif w_over_W >= 0.5 and h_over_H < 0.5:
                        img_position = "4"
                    elif w_over_W < 0.5 and h_over_H >= 0.5:
                        img_position = "1"
                    else:
                        img_position = "3"

                    # Writing data to output csv file
                    writer.writerow({
                     "class": class_no,
                     "x_position": x_position,
                     "y_position": y_position,
                     "image_position": img_position,
                     "width": width,
                     "height": height,
                     "area": area
                     })

        except AttributeError:
            print("IMAGE: ", txt, " added TO CONTROL LIST")
            problematics.write(img_path + "\n")
        finally:
            taken_order.write(txt + "\n")
            counter += 1
            print(counter)

print("\nINFORMATION is INSERTED at: "+OUTPUT_PATH)
