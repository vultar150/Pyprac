from tkinter import *
from pyfiglet import Figlet

class App(Frame):
	def __init__(self, master=None, Title="Application", **kwargs):
		Frame.__init__(self, master, **kwargs)
		self.master.rowconfigure(0, weight=1)
		self.master.columnconfigure(0, weight=1)
		self.master.title(Title)
		self.grid(sticky="NEWS")
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)

		self.E1 = Entry(self)
		self.E1.grid(sticky="NEWS")

		self.B = Button(self, text = "Button")
		self.B.grid(sticky = "NEWS")
		self.B.bind('<Button>', self.f)

		self.L = Label(self, font="fixed")
		self.L.grid()

	def f(self, *args, **kwargs):
		text = Figlet(font='slant')
		self.L["text"] = text.renderText(self.E1.get())


A = App()
A.mainloop()
