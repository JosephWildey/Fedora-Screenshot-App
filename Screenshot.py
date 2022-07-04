import tkinter
import os
from PIL import Image, ImageTk
import re

window = tkinter.Tk()
window.title('Take a screenshot')

def screenshot():
    cmd = 'gnome-screenshot -a'
    os.system(cmd)

button = tkinter.Button(window, text="Take screenshot!", command = screenshot)

pattern = "Screenshot"

image_dir = "/home/joe/Pictures/"

images = os.listdir(image_dir)

for image in images:
    if not re.search(pattern, image):
        images.remove(image)

last_image = ImageTk.PhotoImage(Image.open(image_dir + images[-1]))

def show_screenshot():

    img_label = tkinter.Label(window, image=last_image)
    img_label.pack()

show_image_button = tkinter.Button(window, text="Show last screenshot", command = show_screenshot)


button.pack()
show_image_button.pack()
window.mainloop()
