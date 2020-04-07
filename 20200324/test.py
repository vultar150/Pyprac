from tkinter import *

class App(Frame):
	def __init__(self, master=None, Title="Application", **kwargs):
		Frame.__init__(self, master, **kwargs)
		self.master.rowconfigure(0, weight=1)
		self.master.columnconfigure(0, weight=1)
		self.master.title(Title)
		self.grid(sticky="NEWS")
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)

		self.S = StringVar()
		self.S.set("QWEasd")
		self.E1 = Entry(self, textvariable=self.S)
		self.E1.grid(sticky="NEWS")

		self.E2 = Entry(self, textvariable=self.S)
		self.E2.grid(sticky="NEWS")

		self.S2 = StringVar()
		self.L = Label(self, textvariable=self.S2)
		self.L.grid(sticky="NEWS")

		self.E1.bind('<Button>', self.f)

	def f(self, *args, **kwargs):
		self.S2.set(self.E1.selection_get())


A = App()
#A.mainloop()