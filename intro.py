import tkinter as tk
import subprocess

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
window.title("DSA Case Studies Directory")
window.geometry("960x600")
window.configure(background="#D2DDE3")
window.resizable(False, False)

# buttons
def on_enter(event):
    event.widget.config(background="#ccccc4")

def on_leave(event):
    event.widget.config(background="#f0f0f0")

def ttt():
    try:
        subprocess.run(["python", "ttt_intro.py"])  
    except FileNotFoundError:
        print("Error: ttt_intro.py not found.")

button1 = tk.Button(window, text="Tic Tac Toe", command=ttt)
button1.place(relx=0.5, rely=0.12, anchor="center", bordermode="outside")
button1.bind("<Enter>", on_enter)
button1.bind("<Leave>", on_leave)
button1.configure(font="Helvetica", height=2, width=30, activebackground="#acaca4", relief="ridge", highlightbackground="#659A7E")

def garage1():
    try:
        subprocess.run(["python", "garage1.py"])  
    except FileNotFoundError:
        print("Error: garage1.py not found.")

button2 = tk.Button(window, text="Garage Parking (Stack Version)", command=garage1)
button2.place(relx=0.5, rely=0.245, anchor="center", bordermode="outside")
button2.bind("<Enter>", on_enter)
button2.bind("<Leave>", on_leave)
button2.configure(font="Helvetica", height=2, width=30, activebackground="#acaca4", relief="ridge", highlightbackground="#659A7E")

def garage2():
    try:
        subprocess.run(["python", "garage2.py"])  
    except FileNotFoundError:
        print("Error: garage2.py not found.")

button3 = tk.Button(window, text="Garage Parking (Queue Version)", command=garage2)
button3.place(relx=0.5, rely=0.370, anchor="center", bordermode="outside")
button3.bind("<Enter>", on_enter)
button3.bind("<Leave>", on_leave)
button3.configure(font="Helvetica", height=2, width=30, activebackground="#acaca4", relief="ridge", highlightbackground="#659A7E")

def traversal():
    try:
        subprocess.run(["python", "levels_intro.py"])  
    except FileNotFoundError:
        print("Error: levels_intro.py not found.")

button4 = tk.Button(window, text="Levels of Binary Tree", command=traversal)
button4.place(relx=0.5, rely=0.495, anchor="center", bordermode="outside")
button4.bind("<Enter>", on_enter)
button4.bind("<Leave>", on_leave)
button4.configure(font="Helvetica", height=2, width=30, activebackground="#acaca4", relief="ridge", highlightbackground="#659A7E")

def bintree():
    try:
        subprocess.run(["python", "searchtree_intro.py"])  
    except FileNotFoundError:
        print("Error: searchtree_intro.py not found.")

button5 = tk.Button(window, text="Binary Search Tree", command=bintree)
button5.place(relx=0.5, rely=0.620, anchor="center", bordermode="outside")
button5.bind("<Enter>", on_enter)
button5.bind("<Leave>", on_leave)
button5.configure(font="Helvetica", height=2, width=30, activebackground="#acaca4", relief="ridge", highlightbackground="#659A7E")


def towersofhanoi():
    try:
        subprocess.run(["python", "hanoi_intro.py"])  
    except FileNotFoundError:
        print("Error: hanoi_intro.py not found.")

button6 = tk.Button(window, text="Towers of Hanoi", command=towersofhanoi)
button6.place(relx=0.5, rely=0.745, anchor="center", bordermode="outside")
button6.bind("<Enter>", on_enter)
button6.bind("<Leave>", on_leave)
button6.configure(font="Helvetica", height=2, width=30, activebackground="#acaca4", relief="ridge", highlightbackground="#659A7E")

def sorting():
    try:
        subprocess.run(["python", "sorting_intro.py"])  
    except FileNotFoundError:
        print("Error: sorting_intro.py not found.")

button7 = tk.Button(window, text="Sorting Integers", command=sorting)
button7.place(relx=0.5, rely=0.880, anchor="center", bordermode="outside")
button7.bind("<Enter>", on_enter)
button7.bind("<Leave>", on_leave)
button7.configure(font="Helvetica", height=2, width=30, activebackground="#acaca4", relief="ridge", highlightbackground="#659A7E")

def main():
    try:
        subprocess.run(["python", "greetings.py"])  
    except FileNotFoundError:
        print("Error: greetings.py not found.")

main_button = tk.Button(window, text="<- Back to Welcome Page", font="Helvetica, 10", 
                        command=lambda:[main(), window.destroy()])
main_button.place(rely=0.95)
main_button.bind("<Enter>", on_enter)
main_button.bind("<Leave>", on_leave)

def credits():
    try:
        subprocess.run(["python", "credit_page.py"])  
    except FileNotFoundError:
        print("Error: credit_page.py not found.")

credits_button = tk.Button(window, text="Go to Credits Page ->", font="Helvetica, 10", 
                           command=lambda:[credits()])
credits_button.place(relx=0.855, rely=0.95)
main_button.bind("<Enter>", on_enter)
main_button.bind("<Leave>", on_leave)

center_window(window) 
window.mainloop() 
