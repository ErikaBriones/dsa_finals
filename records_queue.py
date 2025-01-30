import tkinter as tk

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
window.title("Records for Q Garage")
window.geometry("960x600")
window.configure(background="#A2CFFE")
window.resizable(False, False)

# buttons
def on_enter(event):
    event.widget.config(background="#ccccc4")

def on_leave(event):
    event.widget.config(background="#f0f0f0")

# label

label = tk.Label(window, text="Wanna know your records?", font=("Helvetica", 25, "bold"))
label.configure(background="#A2CFFE")
label.place(relx=0.28, rely=0.2)

label1 = tk.Label(window, text="Type your Car's Plate below:", font=("Helvetica", 13))
label1.configure(background="#A2CFFE")
label1.place(relx=0.39, rely=0.33)

label2 = tk.Label(window, text="Entry Counts: ", font=("Helvetica", 20, "bold"))
label2.configure(background="#A2CFFE")
label2.place(relx=0.28, rely=0.56)

label3 = tk.Label(window, text=" ", font=("Helvetica", 20, "bold"))
label3.configure(background="#A2CFFE")
label3.place(relx=0.55, rely=0.56)


label4 = tk.Label(window, text="Exit Counts: ", font=("Helvetica", 20, "bold"))
label4.configure(background="#A2CFFE")
label4.place(relx=0.28, rely=0.62)

label5 = tk.Label(window, text=" ", font=("Helvetica", 20, "bold"))
label5.configure(background="#A2CFFE")
label5.place(relx=0.55, rely=0.62)

# entry

entry = tk.Entry(window, width=36)
entry.place(relx=0.28, rely=0.38)
entry.configure(font="Helvetica", justify="center", relief="flat")

# button

def update_entry():
    count = 0
    target_item = entry.get()
    with open('queue_parking.txt', 'r') as file:
        for line in file:
            items = line.strip().split(',')  
            if target_item in items: 
                count += items.count(target_item) 
            elif target_item == line.strip():
                count +=1
    num = count
    label3.configure(text=num)

def update_exit():
    count = 0
    target_item = entry.get()
    with open('queue_exit.txt', 'r') as file:
        for line in file:
            items = line.strip().split(',')  
            if target_item in items: 
                count += items.count(target_item) 
            elif target_item == line.strip():
                count +=1
    num = count
    label5.configure(text=num)

button = tk.Button(window, text="Enter", font=("helvetica", 12, "bold"), 
                   command=lambda:[update_entry(), update_exit()])
button.configure(width=11)
button.place(relx=0.44, rely=0.428)

center_window(window)
window.mainloop()