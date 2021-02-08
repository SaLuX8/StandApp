from tkinter import *
import time
from tkinter import messagebox
import tkinter as tk
# from crontab import CronTab
# pip install python-crontab
# https://stackabuse.com/scheduling-jobs-with-python-crontab/
# https://pypi.org/project/python-crontab/

root = Tk()

class Clock:
    def __init__(self):
        self.time = time.strftime('%H:%M:%S')
        self.root = root
        self.root.configure(bg='black')
        self.root.title('AlarmClock')
        self.root.geometry("400x250+200+100")

        self.watch = Label(self.root, text=self.time,  font=("Helvetica", 48), fg="green", bg="black") 
        self.watch.pack(pady=20)

        self.sit = Label(root, text="", font=("Helvetica", 18, "bold"), fg="green", bg="black")
        self.sit.pack()

        self.sleep = Label(root, text="", font=("Helvetica", 22, "bold"), fg="red", bg="black")
        self.sleep.pack()

        self.changeLabel() #first call it manually

    def changeLabel(self): 
        self.time2 = time.strftime('%H:%M:%S')
        self.watch.configure(text=self.time2)
        self.root.after(1000, self.changeLabel) #it'll call itself continuously

        self.stand = "SEISO"
        self.sit.configure(text=self.stand)

        self.goSleep = "fsdf"
        self.sleep.configure(text=self.goSleep)

obj1 = Clock()
root.mainloop()



