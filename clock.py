import tkinter as tk
import time

def update_clock():
    current_time = time.strftime(time_format.get())  
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

def set_12_hour_format():
    time_format.set('%I:%M:%S %p')

def set_24_hour_format():
    time_format.set('%H:%M:%S')


root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x150")


clock_label = tk.Label(root, font=('calibri', 30, 'bold'), bg='black', fg='white')
clock_label.pack(expand=True)


time_format = tk.StringVar()
time_format.set('%I:%M:%S %p') 


update_clock()


button_frame = tk.Frame(root)
button_frame.pack(pady=10)

button_12_hour = tk.Button(button_frame, text="12 Hour Format", command=set_12_hour_format)
button_12_hour.grid(row=0, column=0, padx=5)

button_24_hour = tk.Button(button_frame, text="24 Hour Format", command=set_24_hour_format)
button_24_hour.grid(row=0, column=1, padx=5)


root.mainloop()
