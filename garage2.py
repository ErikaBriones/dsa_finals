import tkinter as tk
import subprocess 
from PIL import Image, ImageTk

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
window.geometry("960x600")
window.configure(bg="#A2CFFE")
window.resizable(False, False)

# functions

def on_enter(event):
    event.widget.config(background="#ccccc4")

def on_leave(event):
    event.widget.config(background="#f0f0f0")

def entry():
    try:
        subprocess.run(["python", "garage2_enter.py"])  
    except FileNotFoundError:
        print("Error: garage2_enter.py not found.")

# labels
welcome_label = tk.Label(text="Welcome to Q Garage!", font=("Helvetica", 24, "bold"), background="#A2CFFE", fg="#003366")
welcome_label.place(relx=0.33, rely=0.2)
welcome_label.configure()

label1 = tk.Label(text="What can I do for you?", font="Helvetica, 15", background="#A2CFFE", fg="#003366")
label1.place(relx=0.4, rely=0.28)

click = tk.Label(text="↓↓↓ Click here before continuing", font=("Helvetica", 15,"bold"), background="#A2CFFE", fg="#003366")
click.place(relx=0.35, rely=0.8)

image = Image.open("garage.png")
resized_image = image.resize((300, 300))
img = ImageTk.PhotoImage(resized_image)
garage_label = tk.Label(window, image=img)
garage_label.image = img
garage_label.configure(background="#A2CFFE")
garage_label.place(rely=0.3)

image = Image.open("garage.png")
resized_image = image.resize((300, 300))
img = ImageTk.PhotoImage(resized_image)
garage_label = tk.Label(window, image=img)
garage_label.image = img
garage_label.configure(background="#A2CFFE")
garage_label.place(relx=0.7, rely=0.3)

# buttons
park_button = tk.Button(window, text="Enter Parking", font=("Helvetica", 16, "bold"), command=entry)
park_button.place(relx=0.35, rely=0.5)
park_button.configure(height=1, width=23)
park_button.bind("<Enter>", on_enter)
park_button.bind("<Leave>", on_leave)

def leave():
    try:
        subprocess.run(["python", "garage2_exit.py"])  
    except FileNotFoundError:
        print("Error: garage2_exit.py not found.")

leave_button = tk.Button(window, text="Exit Parking", font=("Helvetica", 16, "bold"), command=leave)
leave_button.place(relx=0.35, rely=0.58)
leave_button.configure(height=1, width=23)
leave_button.bind("<Enter>", on_enter)
leave_button.bind("<Leave>", on_leave)

def records_queue():
    try:
        subprocess.run(["python", "records_queue.py"])  
    except FileNotFoundError:
        print("Error: records_queue.py not found.")

records_button = tk.Button(window, text="Know Records", font=("Helvetica", 16, "bold"), command=records_queue)
records_button.place(relx=0.35, rely=0.66)
records_button.configure(height=1, width=23)
records_button.bind("<Enter>", on_enter)
records_button.bind("<Leave>", on_leave)


def on_leave_slot(event):
    event.widget.config(background="#A2CFFE")

def update():
    line_count = 0
    with open("parking_slot2.txt", 'r') as file:
        for line in file:
            line_count += 1
    num = 10 - line_count
    slot_label.configure(text=num)

slot_label = tk.Label(text="10", font=("Helvetica", 24, "bold"),background="#A2CFFE", fg="#003366")
slot_label.place(relx=0.63, rely=0.87)

check_slot = tk.Button(window, text="Check Number of Slot/s:", font=("Helvetica", 16, "bold"), 
                       background="#A2CFFE", command=update)
check_slot.place(relx=0.31, rely=0.87)
check_slot.configure(height=1, width=23, relief="flat")
check_slot.bind("<Enter>", on_enter)
check_slot.bind("<Leave>", on_leave_slot)

center_window(window)
window.mainloop()