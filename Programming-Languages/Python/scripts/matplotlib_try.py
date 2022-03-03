from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from matplotlib.widgets import Button

from PIL import Image, ImageDraw
import math

class Index:
    ind = 0
    
    def move(self, event):
        self.ind += 1

    def back(self, event):
        self.ind -= 1
        
    def next(self, event):
        self.ind += 1 

index = 0

def move1(event):
        global index 
        index += 1
        
def back1(event):
        global index 
        index -= 1
        
def next1(event):
        global index 
        index += 1
         
choice = 0

if choice == 1: 
    BLUE = (16, 92, 130)
    WHITE = (255, 255, 255)
    
    width, height = 728, 728
    shape = [(width / 2, height / 2), (width - 10, height - 10)]

    # creating new image
    img = Image.new(mode="RGB", size=(width, height), color=WHITE)

    # use draw for the img
    img_drawn = ImageDraw.Draw(img)

    # create rectangle image
    img_drawn.rectangle(shape, fill=BLUE, outline="blue")
    img.save("saved.png")
    
else:
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.3)
    
    img = mpimg.imread("saved.png")

    
    # index_assign = Index()
    ax_back = plt.axes([0.30, 0.05, 0.1, 0.075])
    ax_move = plt.axes([0.45, 0.05, 0.1, 0.075])
    ax_next = plt.axes([0.60, 0.05, 0.1, 0.075])
    
    button_back = Button(ax_back, "Back")
    button_back.on_clicked(back1)
    
    button_move = Button(ax_move, "Move")
    button_move.on_clicked(move1)
    
    button_next = Button(ax_next, "Next")
    button_next.on_clicked(next1)
        
    plt.bar(range(10), range(10))
    plt.show()
    
    print(index)