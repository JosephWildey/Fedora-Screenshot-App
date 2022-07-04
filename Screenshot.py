import tkinter
import os

window = tkinter.Tk()
window.title('Take a screenshot')

def screenshot():
    cmd = 'gnome-screenshot -a'
    os.system(cmd)

button = tkinter.Button(window, text="Take screenshot!", command = screenshot)

button.pack()
window.mainloop()
