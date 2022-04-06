import random
import pathlib
from tkinter import *
from tkinter import messagebox
import time

path = pathlib.Path.cwd() / "img_radio_stations"
radios_list = []

if not path.exists() or len(list(path.iterdir())) <= 0:
	messagebox.showerror("Choose A Random Radio Station - UWAGA", "Dane nie istnieją. Nie można dokonać losowania")
	exit()


class Application(Frame):
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.btn_random = Button(root)
		self.pack()
		self.create_widgets()
		
	def create_widgets(self):
		# utwórz przycisk do losowania
		self.btn_random['text'] = "LOSOWANIE"
		self.btn_random['image'] = None
		self.btn_random['height'] = "160"
		self.btn_random['width'] = "160"
		self.btn_random['command'] = self.choose_radio
		self.btn_random.pack()
	
	def choose_radio(self):
		for picture in path.glob("*.png"):
			radios_list.append(picture)
			
		station = random.choice(radios_list)
		# print(station) # to check myself
		
		global image
		image = PhotoImage(file=station)
		self.btn_random['text'] = None
		self.btn_random['image'] = image





root = Tk()
root.title('Choose A Random Radio Station')
root.geometry('180x170')
root.minsize(180, 170)
root.maxsize(180, 170)
app = Application(root)
root.mainloop()
