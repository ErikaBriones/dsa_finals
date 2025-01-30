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
window.title("Binary Search Tree Instructions")
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
1. Enter 30 integers in the input box. Make sure that the numbers are exactly 30.
2. Press 'Done' once finished.
3. See its traversals in the 'Traversal' section.
4. See its corresponding binary tree just below the previous section.
5. Re-enter another set of integers in the inout box to run another traversal and tree.
6. Exit the program once done. Enjoy!
""", 
font=("Helvetica", 14, "bold"))
label.configure(anchor="center", background="#EDE1D2", justify="left")
label.place(relx=0.08, rely=0.3)

def bst():
    try:
        subprocess.run(["python", "searchtree.py"])  
    except FileNotFoundError:
        print("Error: searchtree.py not found.")

image = Image.open("bst.png")
resized_image = image.resize((300, 300))
img = ImageTk.PhotoImage(resized_image)
bst_label = tk.Label(window, image=img)
bst_label.image = img
bst_label.configure(background="#EDE1D2")
bst_label.place(relx=0.71, rely=0.52)

image = Image.open("bst2.png")
resized_image = image.resize((400, 300))
img = ImageTk.PhotoImage(resized_image)
bst_label2 = tk.Label(window, image=img)
bst_label2.image = img
bst_label2.configure(background="#EDE1D2")
bst_label2.place(relx=-0.02, rely=0.58)

button = tk.Button(window, text="CONTINUE", font=("Helvetica",16, "bold"), command=lambda:[bst(), window.destroy()])
button.configure(width=20)
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)
button.place(relx=0.37, rely=0.8)


center_window(window)
window.mainloop()