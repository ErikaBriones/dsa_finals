import tkinter as tk 
import subprocess
from tkinter import messagebox
from tkinter import PhotoImage

def center_window(window):
    window.update_idletasks() 
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"+{x}+{y}")

window = tk.Tk()
window.title("Garage Parking (Queue Version)")
window.geometry("600x450")
window.configure(bg="#A2CFFE")
window.resizable(False, False)

# label
register_label = tk.Label(window, text="Register Car's Plate: ", 
                          font=("Helvetica", 16, "bold"), background="#A2CFFE")
register_label.place(relx=0.1, rely=0.3)

# entry
    
entry = tk.Entry(window, width=20)
entry.place(relx=0.47, rely=0.3)
entry.configure(font="Helvetica", justify="center", relief="flat")

def check_plate(plate_number):

    try:
        with open("parking_slot2.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if plate_number in line:
                    return True
            return False  
    except FileNotFoundError:
        return False 

value = entry.get()
plate_number = value
run = check_plate(plate_number)

def register_car():

    plate_number = entry.get()
    run = check_plate(plate_number)

    if run:
        messagebox.showerror("Error", "This car's plate is already registered.")
    else:
        with open("parking_slot2.txt", "r") as file:
            lines = file.readlines()
        if len(lines) >= 10:
            messagebox.showwarning("Warning", "Garage is full. Please exit a car first.")
        else:
            with open("parking_slot2.txt", "a") as file:
                file.write(f"{plate_number}\n")
                messagebox.showinfo("Success", f"Car with plate number [{plate_number}] registered successfully!")

            with open("queue_parking.txt", "a") as file1:
                file1.write(f"{plate_number}\n")


# buttons
def on_enter(event):
    event.widget.config(background="#ccccc4")

def on_leave(event):
    event.widget.config(background="#f0f0f0")

register_button = tk.Button(window, text="Register", font=("Helvetica", 10, "bold"), 
                            command=lambda: [register_car(), window.destroy()])
register_button.configure(height=1, width=10, relief="groove")
register_button.bind("<Enter>", on_enter)
register_button.bind("<Leave>", on_leave)
register_button.place(relx=0.58, rely=0.365)

center_window(window)
window.mainloop()
