from tkinter import *
from tkinter import ttk
import time
import os
import pyautogui

#cas auto vypnuti 15min = 900s
time.sleep(900)
pyautogui.doubleClick(700,350)

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
root.geometry('320x50')

def vypnout():
    print("off")
    root.destroy()
    os.system("sudo shutdown -h now")
    
def ne():
    root.destroy()

def countdown(count):
    # change text in label        
    label['text'] = count

    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, count-1)
        
    if count == 0:
        print("off")
        os.system("sudo shutdown -h now")
        root.destroy()

label = ttk.Label(root)
label.place(x=110, y=14)

# call countdown first time    
countdown(60)
# root.after(0, countdown, 5)

root.eval('tk::PlaceWindow . center')
ttk.Label(frm, text="Vypnuti TV za:       ").grid(column=0, row=0)
ttk.Button(frm, text="ANO", command=vypnout).grid(column=1, row=0)
ttk.Button(frm, text="NE", command=ne).grid(column=2, row=0)
root.mainloop()


