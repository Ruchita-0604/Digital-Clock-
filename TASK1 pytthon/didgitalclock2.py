import tkinter as tk 
from time import strftime

root = tk.Tk()
root.title('Digital clock')
def time():
    current_time = strftime('%H:%M:%S:%p')
    time_label.config(text=current_time)
    time_label.after(1000, time)
    current_date = strftime('%A, %B , %D, %Y')
    date_label.config(text=current_date)
    date_label.after(1000, time)

time_label = tk.Label(root, font=('calibri', 50, 'bold'),background='pink', foreground='black')
time_label.pack(anchor='center')
date_label = tk.Label(root, font=('calibri', 20, 'bold'),background='pink', foreground='black')
date_label.pack(anchor='center')

time()

root.mainloop()