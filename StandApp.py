from tkinter import *
import time, sched
from tkinter import messagebox
import tkinter as tk
import datetime


# from crontab import CronTab
# pip install python-crontab
# https://stackabuse.com/scheduling-jobs-with-python-crontab/
# https://pypi.org/project/python-crontab/

root = Tk()

class Clock:
    try:

        def __init__(self):
            self.time = time.strftime('%H:%M:%S')
            self.root = root
            self.root.configure(bg='black')
            self.root.title('AlarmClock')
            self.root.geometry("400x250+200+100")
            self.stand = ""
            self.goSleep = ""
            self.sleepingTime = '22:00'         # enter time to go to sleep in format HH:MM
            self.standingTimeMin = 30           # enter standing time in one hour in minutes

            # set scheduler
            self.s = sched.scheduler(time.time, time.sleep)

            self.watch = Label(self.root, text=self.time,  font=("Helvetica", 48), fg="green", bg="black") 
            self.watch.pack(pady=20)

            self.sit = Label(root, text="", font=("Helvetica", 18, "bold"), fg="green", bg="black")
            self.sit.pack()

            self.sleep = Label(root, text="", font=("Helvetica", 22, "bold"), fg="red", bg="black")
            self.sleep.pack()

            # self.sleepingTimeLabel = Label(root, text="Time to go to sleep: "+ self.sleepingTime, font=("Helvetica", 10), fg="red", bg="black")
            # self.sleepingTimeLabel.pack(side = LEFT, pady=10, padx=10)

            self.changeLabel() 

        def changeLabel(self): 
            self.time2 = time.strftime('%H:%M:%S')
            self.watch.configure(text=self.time2)
            self.root.after(1000, self.changeLabel)
            self.sit.configure(text=self.stand)
            self.sleep.configure(text=self.goSleep)

            # Call scheduler      
            self.s.enter(5,1,self.job())   # called every 5 seconds, priority 1

        def job(self):
            now = datetime.datetime.now().time()

            if now.minute > self.standingTimeMin and now.minute <= 59:
                self.stand = "ISTU"
            else:
                self.stand = "SEISO"

            if now > datetime.datetime.strptime(self.sleepingTime, '%H:%M').time():
                self.goSleep = "MENE NUKKUMAAN"

    except (Exception):
        print("something went wrong.. but what?")
        print(sys.exc_info()[0])

obj1 = Clock()


root.mainloop()



