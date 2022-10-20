# Finn's period calculator 
# Tigers are motherfucking cool
# hey fedor
from tkinter import *
from datetime import datetime
dt = datetime.now()
wkday = dt.weekday()
time = int(dt.strftime("%H%M"))
def minutes_until(hour, minute):
    #get the current time
    now = datetime.now()
    #get the current hour
    current_hour = now.hour
    #get the current minute
    current_minute = now.minute
    #get the current second
    current_second = now.second
    #get the current microsecond
    current_microsecond = now.microsecond
    #get the time until the specified hour
    time_until_hour = hour - current_hour
    #get the time until the specified minute
    time_until_minute = minute - current_minute
    #get the time until the specified second
    time_until_second = 60 - current_second
    #get the time until the specified microsecond
    time_until_microsecond = 1000000 - current_microsecond
    #get the total time until the specified time
    total_time = time_until_hour * 3600 + time_until_minute * 60 + time_until_second + time_until_microsecond / 1000000
    #get the total time in minutes
    total_time_in_minutes = total_time / 60
    #return the total time in minutes
    return total_time_in_minutes
if wkday == 0:
    if time < 855:
        left = (f"The current period has {round(minutes_until(8, 55))} minutes left.")
    elif time < 950:
        left = (f"The current period has {round(minutes_until(9, 50))} minutes left.")
    elif time < 1045:
        left = (f"The current period has {round(minutes_until(10, 45))} minutes left.")
    elif time < 1205:
        left = (f"The current period has {round(minutes_until(12, 00))} minutes left.")
    elif time < 1300:
        left = (f"The current period has {round(minutes_until(1300))} minutes left.")
    elif time < 1430:
        x = 1430 - time
        left = (f"The current period has {round(minutes_until(14, 30))} minutes left.")
    elif time < 1525:
        x = 1525 - time
        left = (f"The current period has {round(minutes_until(15, 25))} minutes left.")
    else:
        left = ("You are currently not in school... enjoy that.")
elif wkday == 1:
    if time < 940:
        left = (f"The current period has {round(minutes_until(9, 40))} minutes left.")
    elif time < 1035:
        left = (f"The current period has {round(minutes_until(10, 35))} minutes left.")
    elif time < 1150:
        left = (f"The current period has {round(minutes_until(11, 50))} minutes left.")
    elif time < 1245:
        x = 1245 - time
        left = (f"The current period has {round(minutes_until(12, 45))} minutes left.")
    elif time < 1420:
        x = 1420 - time
        left = (f"The current period has {round(minutes_until(14, 20))} minutes left.")
    elif time < 1515:
        x = 1515 - time
        left = (f"The current period has {round(minutes_until(15, 15))} minutes left.")
    else:
        left = ("You are currently not in school... enjoy that.")
elif wkday == 2:
    if time < 940:
        x = 940 - time
        left = (f"The current period is has {round(minutes_until(9, 40))} minutes left.")
    elif time < 1035:
        x = 1035 - time
        left = (f"The current period is has {round(minutes_until(10, 35))} minutes left.")
    elif time < 1150:
        x = 1150 - time
        left = (f"The current period has {round(minutes_until(11, 50))} minutes left.")
    elif time < 1245:
        x = 1245 - time
        left = (f"The current period has {round(minutes_until(12, 45))} minutes left.")
    elif time < 1420:
        x = 1420 - time
        left = (f"The current period has {round(minutes_until(14, 20))} minutes left.")
    elif time < 1515:
        x = 1515 - time
        left = (f"The current period has {round(minutes_until(15, 15))} minutes left.")
    else:
        left = ("You are currently not in school... enjoy that.")
elif wkday == 3:
    if time < 940:
        x = 940 - time
        left = (f"The current period has {round(minutes_until(9, 40))} minutes left.")
    elif time < 1035:
        x = 1035 - time 
        left = (f"The current period has {round(minutes_until(10, 35))} minutes left.")
    elif time < 1150:
        x = 1150 - time
        left = (f"The current period has {round(minutes_until(11, 50))} minutes left.")
    elif time < 1240:
        x = 1240 - time
        left = (f"The current period  has {round(minutes_until(12, 40))} minutes left.")
    elif time < 1415:
        x = 1415 - time
        left = (f"The current period has {round(minutes_until(14, 15))} minutes left.")
    elif time < 1510:
        x = 1510 - time
        left = (f"The current period has {round(minutes_until(15, 10))} minutes left.")
    else:
        left = ("You are currently not in school... enjoy that.")
elif wkday == 4:
    if time < 855:
        x = 855 - time
        left = (f"The current period has {round(minutes_until(8, 55))} minutes left.")
    elif time < 950:
        x = 950 - time
        left = (f"The current period has {round(minutes_until(9, 50))} minutes left.")
    elif time < 1045:
        x = 1045 - time
        left = (f"The current period has {round(minutes_until(10, 45))} minutes left.")
    elif time < 1205:
        x = 1205 - time
        left = (f"The current period has {round(minutes_until(12, 00))} minutes left.")
    elif time < 1300:
        x = 1300 - time
        left = (f"The current period has {round(minutes_until(13, 00))} minutes left.")
    elif time < 1430:
        x = 1430 - time
        left = (f"The current period is  has {round(minutes_until(14, 30))} minutes left.")
    elif time < 1525:
        x = 1525 - time
        left = (f"The current period has {round(minutes_until(15, 25))} minutes left.")    
    else:
        left = ("You are currently not in school... enjoy that.")

screen = Tk()
def secondscreen():
    screen.destroy()
    secondscreen = Tk()
    secondscreen.geometry("500x200")
    secondscreen.title("'You're welcome.' - Finn")
    text = Label(secondscreen, text=f"{left}", bg = "grey", bd = 100, fg = "white", font = "Euphemia")
    text.pack()
screen.title("How long is left in the period?")
screen.geometry("500x480")
howlong = Button(text="Click Me!", height = "29", width = "67", command = secondscreen)
howlong.place(x = 10, y = 20)
screen.configure(bg="grey")
screen.mainloop()