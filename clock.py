import tkinter as tk
import time

def update_clock():
    current_time = time.strftime('%I:%M:%S %p')  # %p gives AM or PM
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("250x100")

# Create a label to display the clock
clock_label = tk.Label(root, font=('calibri', 30, 'bold'), bg='black', fg='white')
clock_label.pack(expand=True)

# Update the clock initially and start the clock update process
update_clock()

# Start the tkinter event loop
root.mainloop()
