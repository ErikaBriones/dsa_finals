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
window.title("Levels of Binary Tree Instructions")
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
1. Type an integer between 1 to 5.
2. Press the 'Done' button to generate a random binary tree with the specified level.
3. Find its traversals in the "Traversals" Section.
4. Exit the program once done. Enjoy!
""", 
font=("Helvetica", 14, "bold"))
label.configure(anchor="center", background="#EDE1D2", justify="left")
label.place(relx=0.08, rely=0.3)

image = Image.open("level.png")
resized_image = image.resize((300, 350))
img = ImageTk.PhotoImage(resized_image)
tree_label = tk.Label(window, image=img)
tree_label.image = img
tree_label.configure(background="#EDE1D2")
tree_label.place(relx=0.7, rely=0.47)

image = Image.open("levels2.png")
resized_image = image.resize((500, 300))
img = ImageTk.PhotoImage(resized_image)
tree_label2 = tk.Label(window, image=img)
tree_label2.image = img
tree_label2.configure(background="#EDE1D2")
tree_label2.place(relx=-0.08, rely=0.52)

def levels():
    try:
        subprocess.run(["python", "traversal.py"])  
    except FileNotFoundError:
        print("Error: traversal.py not found.")

button = tk.Button(window, text="CONTINUE", font=("Helvetica",16, "bold"), command=lambda:[levels(), window.destroy()])
button.configure(width=20)
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)
button.place(relx=0.37, rely=0.8)


center_window(window)
window.mainloop()