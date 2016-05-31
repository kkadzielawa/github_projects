from Tkinter import *


class MyFirstGui:

	def __init__(self, master):
		
		self.master = master
		master.title("Simple GUI")

		self.label = Label(master, text="This is GUI")
		self.label.pack()

		self.greet_button = Button(master, text="Greet", command = self.greet)
		self.greet_button.pack()

		self.close_button = Button(master, text="Close", command = master.quit)
		self.close_button.pack()

	def greet(self):
		
		print "Greetings!"



root = Tk()

my_gui = MyFirstGui(root)

root.mainloop()
