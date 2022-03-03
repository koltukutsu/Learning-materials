from glob import glob
from os import mkdir, stat
from time import sleep
from PIL import Image
import PIL
import csv


IMG_TYPE = "jpg"
TXTS_PATH = "/home/semih/Documents/VERILER/YENI_VALID (copy)"
TXTS_PATH = TXTS_PATH if TXTS_PATH[-1] != "/" else TXTS_PATH[:-1]
OUTPUT_PATH = TXTS_PATH + "/OUTPUTS/"
POP_FILES = [TXTS_PATH + "/" + txt for txt in ["classes.txt"]]
TXTS = glob(TXTS_PATH + "/*.txt")

print("\nTOTAL COUNTED TXT FILES: ",len(TXTS), "\n")
# pop from the glob list the unwanted
for txt in TXTS[:]:
    if txt in POP_FILES:
        TXTS.remove(txt)
        print("\nAFTER EXLUSION, THE REMANING TEXT FILES: ",len(TXTS) - len(POP_FILES), "\n")

counter = 0
problem_flags = {"blanks":0,
                 "not_found_imgs":0,
                 "problematic_imgs":0,    
                 "problematic_txts":0,
                }

# output folder
try:
    mkdir(OUTPUT_PATH)
except FileExistsError:
    print(OUTPUT_PATH + " DIRECTORY IS PRESENT")

# give a chance for the user to see the console
sleep(1.2)


# opening csv file to write    
with open(OUTPUT_PATH + "DETALIED_OUTPUT.csv", "w", newline="") as csvfile\
    , open(OUTPUT_PATH + "BLANK_TXTS.txt", "w") as blanks\
    , open(OUTPUT_PATH + "NOT_FOUND_IMGS.txt", "w") as not_found_imgs\
    , open(OUTPUT_PATH + "PROBLEMATIC_TXTS.txt", "w") as problematic_txts\
    , open(OUTPUT_PATH + "PROBLEMATIC_IMGS.txt", "w") as problematic_imgs\
    , open(OUTPUT_PATH + "READING_ORDER.txt", "w") as reading_order:
    FIELDNAMES = ["class", "x_position", "y_position", "image_position", "width", "height", "area", "real_img_width", "real_img_height", "real_img_area", "ratio"]
    csv.register_dialect("settings", delimiter=";")
    writer = csv.DictWriter(csvfile, dialect="settings", fieldnames=FIELDNAMES)
    
    writer.writeheader()
    for txt in TXTS:
        if stat(txt).st_size==0:
            print("TXT: ", txt, " added to BLANK_TXTS.txt")
            problem_flags["blanks"] += 1
            blanks.write(txt+"\n")
            continue
        
        img_path = txt.rstrip("txt") + IMG_TYPE
        
        try: 
            # PIL is quite faster than the cv2.imread in loading
            with Image.open(img_path) as img:
                WIDTH, HEIGHT= img.size # for PIL.Image.open -> width, height

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
                    # control whether it has 5 separate info
                    if len(datas_in) != 5:
                        print("TXT: ", txt, " added to PROBLEMATIC_TXTS.txt")
                        problem_flags["problematic_txts"] += 1
                        problematic_txts.write(txt + "\n")
                        continue
                    
                    # Seperated datas from the file
                    a_over_W = float(datas_in[1])
                    b_over_H = float(datas_in[2])
                    w_over_W = float(datas_in[3])
                    h_over_H = float(datas_in[4])
                    
                    # variables for the image in the boundingbox
                    class_no = datas_in[0]
                    x_position = a_over_W * WIDTH
                    y_position = b_over_H * HEIGHT
                    width = w_over_W * WIDTH
                    height = h_over_H * HEIGHT
                    area = width * height
                    
                    img_position = None
                    
                    # variables for the image
                    """
                    WIDTH
                    HEIGHT are also assigned as the real images variables
                    """
                    real_img_area = WIDTH * HEIGHT
                    
                    # ratio of the real and bounded image
                    ratio = (area / real_img_area) * 1e2  # gives the percentage
                          
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
                     "class":class_no,
                     "x_position":x_position,
                     "y_position":y_position,
                     "image_position":img_position,
                     "width":width,
                     "height":height,
                     "area":area,
                     "real_img_width":WIDTH,
                     "real_img_height":HEIGHT, 
                     "real_img_area":real_img_area,
                     "ratio":ratio
                     })
                        
        except PIL.UnidentifiedImageError:
            print("IMAGE: ", img_path, " added to PROBLEMATIC_IMGS.txt")
            problem_flags["problematic_imgs"] += 1
            problematic_imgs.write(img_path + "\n")
        
        except FileNotFoundError:
            print("IMAGE: ", img_path, " NOT FOUND, added to NOT_FOUND_IMGS.txt")
            problem_flags["not_found_imgs"] += 1
            not_found_imgs.write(img_path + "\n")
            
        else:
            reading_order.write(txt + "\n")
        finally:
            counter += 1
            print(counter)
        
with open(OUTPUT_PATH + "PROBLEM_FLAGS.txt", "w") as p_flags:
    print(problem_flags, file=p_flags)
    
print("\nINFORMATION is INSERTED at: " + OUTPUT_PATH)
