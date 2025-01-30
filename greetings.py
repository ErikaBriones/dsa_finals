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
window.title("Welcome!")
window.geometry("960x600")
window.configure(background="#D7CCC8")
window.resizable(False, False)

#labels
line_label = tk.Label(window, text="____________________________________________________________________________", 
                      font=("Lexend", 16, "bold"), background="#D7CCC8", fg="#990000")
line_label.place(relx=0.025, rely=0.04)

dsa_label = tk.Label(window, text="DSA GROUP 10", font=("Lexend", 16, "bold"), background="#D7CCC8", fg="#990000")
dsa_label.place(relx=0.025, rely=0.025)

welcome_label = tk.Label(window, text="WELCOME!", font=("Lexend", 40, "bold"), background="#D7CCC8", fg="#990000")
welcome_label.place(relx=0.35, rely=0.2)

text_label = tk.Label(window, text="GROUP 10 CASE STUDIES", 
                      font=("Lexend", 13, "bold"), background="#D7CCC8", fg="#990000")
text_label.place(relx=0.388, rely=0.325)

directory_label = tk.Label(window, text="Head to our directory ↓↓↓", font=("Lexend", 16, "bold"),
                           background="#D7CCC8", fg="#990000")
directory_label.place(relx= 0.12, rely=0.5)
                           
credits_label = tk.Label(window, text="Credits Page ↓↓↓", font=("Lexend", 16, "bold"),
                           background="#D7CCC8", fg="#990000")
credits_label.place(relx= 0.67, rely=0.5)

line_label = tk.Label(window, text="____________________________________________________________________________", 
                      font=("Lexend", 16, "bold"), background="#D7CCC8", fg="#990000")
line_label.place(relx=0.025, rely=0.9)

c_label = tk.Label(window, text="© 2025 - Aguylo, Alipio, Briones, Quibo", 
                   font=("Lexend", 9, "italic"), background="#D7CCC8", fg="#990000")
c_label.place(relx=0.025, rely=0.95)

# buttons

def on_enter(event):
    event.widget.config(background="#ccccc4")

def on_leave(event):
    event.widget.config(background="#f0f0f0")

def open_directory():
    try:
        subprocess.run(["python", "intro.py"])  
    except FileNotFoundError:
        print("Error: intro.py not found.")

directory_button = tk.Button(window, text="List of Projects", command=lambda:[open_directory(), window.destroy()])
directory_button.place(relx= 0.1, rely=0.57)
directory_button.bind("<Enter>", on_enter)
directory_button.bind("<Leave>", on_leave)
directory_button.configure(font=("Lexend", 16, "bold"), width=21, height=1, foreground="#990000")

def open_credits():
    try:
        subprocess.run(["python", "credit_page.py"])  
    except FileNotFoundError:
        print("Error: credit_page.py not found.")

credits_button = tk.Button(window, text="Credits", command=lambda:[open_credits()])
credits_button.place(relx= 0.6, rely=0.57)
credits_button.bind("<Enter>", on_enter)
credits_button.bind("<Leave>", on_leave)
credits_button.configure(font=("Lexend", 16, "bold"), width=21, height=1, foreground="#990000")

center_window(window)
window.mainloop()