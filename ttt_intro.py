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
window.title("Tic Tac Toe Instructions")
window.geometry("960x600")
window.configure(background="#EDE1D2")
window.resizable(False, False)

# buttons
def on_enter(event):
    event.widget.config(background="#ccccc4")

def on_leave(event):
    event.widget.config(background="#f0f0f0")

label1 = tk.Label(window, text="How to Play Tic Tac Toe:", font=("helvetica",35, "bold"))
label1.configure(label1.configure(anchor="center", background="#EDE1D2"))
label1.place(relx=0.15, rely=0.15)

label = tk.Label(window, text="""
1. Two players take turns. One player is "X" and the other is "O".
2. Players take turns placing their mark (X or O) in an empty square on the grid.
3. X always goes first.
4. The goal is to get three of your marks in a row—horizontally, vertically, or diagonally.
5. The first player to get three of their marks in a row wins the game.
6. If all nine squares are filled and neither player has three in a row, the game is a draw.""", 
font=("Helvetica", 14, "bold"))
label.configure(anchor="center", background="#EDE1D2", justify="left")
label.place(relx=0.08, rely=0.3)


image = Image.open("ttt.png")
resized_image = image.resize((210, 210))
img = ImageTk.PhotoImage(resized_image)
ttt_label = tk.Label(window, image=img)
ttt_label.image = img
ttt_label.configure(background="#EDE1D2")
ttt_label.place(relx=0.75, rely=0.02)

def ttt():
    try:
        subprocess.run(["python", "tictactoe.py"])  
    except FileNotFoundError:
        print("Error: tictactoe.py not found.")

button = tk.Button(window, text="PLAY", font=("Helvetica",16, "bold"), command=lambda:[ttt(), window.destroy()])
button.configure(width=20)
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)
button.place(relx=0.37, rely=0.8)


center_window(window)
window.mainloop()