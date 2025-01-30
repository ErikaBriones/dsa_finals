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
window.title("Towers of Hanoi Instructions")
window.geometry("960x600")
window.configure(background="#EDE1D2")
window.resizable(False, False)

def on_enter(event):
    event.widget.config(background="#ccccc4")

def on_leave(event):
    event.widget.config(background="#f0f0f0")

label1 = tk.Label(window, text="How to Play Towers of Hanoi:", font=("helvetica",35, "bold"))
label1.configure(label1.configure(anchor="center", background="#EDE1D2"))
label1.place(relx=0.15, rely=0.15)

label = tk.Label(window, text="""
1. Choose your level of difficulty based on the disks available. More disks, more difficult.
2. Only one disk can be moved at a time.
3.Each move consists of taking the upper disk from one of the stacks and placing it on top 
of another stack or on an empty rod.
4. No larger disk may be placed on top of a smaller disk.""", font=("Helvetica", 14, "bold"))

label.configure(anchor="center", background="#EDE1D2", justify="left")
label.place(relx=0.08, rely=0.3)


image = Image.open("hanoi.png")
resized_image = image.resize((300, 220))
img = ImageTk.PhotoImage(resized_image)
hanoi_label = tk.Label(window, image=img)
hanoi_label.image = img
hanoi_label.configure(background="#EDE1D2")
hanoi_label.place(relx=0.35, rely=0.58)

image = Image.open("hanoi2.png")
resized_image = image.resize((300, 300))
img = ImageTk.PhotoImage(resized_image)
hanoi_label2 = tk.Label(window, image=img)
hanoi_label2.image = img
hanoi_label2.configure(background="#EDE1D2")
hanoi_label2.place(relx=0.69, rely=0.52)

image = Image.open("disks.png")
resized_image = image.resize((300, 300))
img = ImageTk.PhotoImage(resized_image)
hanoi_label3 = tk.Label(window, image=img)
hanoi_label3.image = img
hanoi_label3.configure(background="#EDE1D2")
hanoi_label3.place(rely=0.52)

def play():
    try:
        subprocess.run(["python", "hanoi.py"])  
    except FileNotFoundError:
        print("Error: hanoi.py not found.")

button = tk.Button(window, text="PLAY", font=("Helvetica",16, "bold"), command=lambda:[play(), window.destroy()])
button.configure(width=20)
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)
button.place(relx=0.37, rely=0.85)

center_window(window)
window.mainloop()