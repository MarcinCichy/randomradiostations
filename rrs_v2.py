"""
	When you cannot make a decision or more people in your office cannot choose which radio to listen to together
	A little script for randomly selecting radio stations to listen to could be helpful.
	Selected radio station you can listen to, for example, radiofm-online.com
	
	Click once on the picture to start the draw, click again to end the draw.
"""

import random
import pathlib
from tkinter import *
from tkinter import messagebox

path = pathlib.Path.cwd() / "img_radio_stations"
radios_list = []

if not path.exists() or len(list(path.iterdir())) <= 0:
	messagebox.showerror("Choose A Random Radio Station - UWAGA", "Dane nie istnieją. Nie można dokonać losowania")
	exit()


class Application(Frame):
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.btn_random = Button(root)
		self.btn_random_clicks = 0
		self.pack()
		self.create_widgets()
		
	def create_widgets(self):
		# create button for the draw
		self.btn_random['text'] = "LOSOWANIE \n Naciśnij mnie dwa razy :-)"
		self.btn_random['image'] = None
		self.btn_random['height'] = "160"
		self.btn_random['width'] = "160"
		self.btn_random['command'] = self.update_clicks
		self.btn_random.pack(anchor=CENTER)

	def update_clicks(self):
		self.btn_random_clicks += 1
		# print(self.btn_random_clicks)  # to check myself
		self.change_img()

	def change_img(self):
		self.choose_radio()
		if self.btn_random_clicks % 2 != 0:
			self.after(80, self.change_img)

	def choose_radio(self):
		for picture in path.glob("*.png"):
			radios_list.append(picture)
		station = random.choice(radios_list)
		# print(station) # to check myself
		global image
		image = PhotoImage(file=station)
		self.btn_random['image'] = image


root = Tk()
app = Application(root)
root.title('Random Radio Station')
root.geometry('170x170')
root.iconbitmap(pathlib.Path.cwd() / "radio.ico")
root.minsize(170, 170)
root.maxsize(170, 170)
root.mainloop()
