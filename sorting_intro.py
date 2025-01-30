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
window.title("Sorting Instructions")
window.geometry("960x600")
window.configure(background="#EDE1D2")
window.resizable(False, False)

# buttons
def on_enter(event):
    event.widget.config(background="#ccccc4")

def on_leave(event):
    event.widget.config(background="#f0f0f0")

label1 = tk.Label(window, text="Instructions:", font=("helvetica",35, "bold"))
label1.configure(label1.configure(anchor="center", background="#EDE1D2"))
label1.place(relx=0.36, rely=0.15)

label = tk.Label(window, text="""
1. Type 30 integers inside the bar provided that each integer is separated by space.
2. Submit the list of integers. Make sure that it is exactly 30 or else it won't work.
3. Choose the method of sorting that you wanted to apply then submit.
4. Wait for the sorting process to finish and the results will immediately be displayed.
5. To start another sorting process, just enter another set of integers in the "input" tab
and repeat the procedures listed above. Enjoy!
""", 
font=("Helvetica", 14, "bold"))
label.configure(anchor="center", background="#EDE1D2", justify="left")
label.place(relx=0.08, rely=0.3)

def ttt():
    try:
        subprocess.run(["python", "sorting.py"])  
    except FileNotFoundError:
        print("Error: sorting.py not found.")

image = Image.open("sorting.png")
resized_image = image.resize((300, 300))
img = ImageTk.PhotoImage(resized_image)
sorting = tk.Label(window, image=img)
sorting.image = img
sorting.configure(background="#EDE1D2")
sorting.place(relx=0.71, rely=0.52)

image = Image.open("sorting.png")
resized_image = image.resize((300, 250))
img = ImageTk.PhotoImage(resized_image)
sorting2 = tk.Label(window, image=img)
sorting2.image = img
sorting2.configure(background="#EDE1D2")
sorting2.place(rely=0.565)

button = tk.Button(window, text="PROCEED", font=("Helvetica",16, "bold"), command=lambda:[ttt(), window.destroy()])
button.configure(width=20)
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)
button.place(relx=0.37, rely=0.8)


center_window(window)
window.mainloop()