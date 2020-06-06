from tkinter import *
import os
import subprocess
import sys
from tkinter import filedialog as fd


def open_file():
    file_name = fd.askopenfilename()
    output = subprocess.check_output(["xxd", "-g1", file_name])
    text.delete(1.0, END)
    text.insert(1.0, output)


def save_text():
    s = text.get(1.0, END)
    f = open("tmp.txt", "w")
    f.write(s)
    f.close()
    output = subprocess.check_output(["xxd", "-r", "tmp.txt"])
    f = open("text.txt", "wb")
    f.write(output)
    f.close()


def save_text_as():
    file_name = fd.asksaveasfilename()
    s = text.get(1.0, END)
    f = open("tmp.txt", "w")
    f.write(s)
    f.close()
    output = subprocess.check_output(["xxd", "-r", file_name])
    f = open(file_name, "wb")
    f.write(output)
    f.close()



root = Tk()

text = Text(width=60, height=20)
text.pack(side=LEFT)

scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)

text.config(yscrollcommand=scroll.set)
 
frame = Frame()
frame.pack()

 
b_open = Button(frame, text="Open", width=10, command=open_file)
b_open.grid(row=0, column=0)

b_save = Button(frame, text="Save", width=10, command=save_text)
b_save.grid(row=0, column=1)

# e2 = Entry(frame, width=20)
# e2.grid(row=2,column=0)

b_save_as = Button(frame, text="Save as", width=10, command=save_text_as)
b_save_as.grid(row=0, column=2)
 
root.mainloop()