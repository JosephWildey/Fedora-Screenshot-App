import tkinter
import os
from PIL import Image, ImageTk

window = tkinter.Tk()
window.title('Take a screenshot')

def screenshot():
    cmd = 'gnome-screenshot -a'
    os.system(cmd)

button = tkinter.Button(window, text="Take screenshot!", command = screenshot)

image_dir = "/home/user/Pictures/"

images = os.listdir(image_dir)

last_image = ImageTk.PhotoImage(Image.open(image_dir + images[-1]))

def show_screenshot():

    img_label = tkinter.Label(window, image=last_image)
    img_label.pack()

show_image_button = tkinter.Button(window, text="Show last screenshot", command = show_screenshot)


button.pack()
show_image_button.pack()
window.mainloop()
