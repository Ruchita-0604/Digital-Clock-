import tkinter as tk
from time import strftime

#create the main window

root = tk.Tk()
root.title("Digital clock")

#Define font and color

text_font = ("Arial", 60, "bold")
background_color = "#342a4f"
foreground_color = "purple"
#create label to display

label = tk.Label(root, font=text_font, bg=background_color, fg=foreground_color)
label.pack(anchor="center")

#function to update the display 

def update_time():
    current_time = strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000 , update_time)          #every 1 sec time will change 

    #clock will start 

update_time()

#loop will run

root.mainloop()

