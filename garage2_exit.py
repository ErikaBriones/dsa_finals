import tkinter as tk 
from tkinter import messagebox
import os

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
window.title("Garage Parking - Exiting (Queue Version)")
window.geometry("600x450")
window.configure(bg="#A2CFFE")
window.resizable(False, False)

# label
register_label = tk.Label(window, text="Plate Number: ", font=("Helvetica", 16, "bold"), background="#A2CFFE")
register_label.place(relx=0.135, rely=0.3)

# entry

entry = tk.Entry(window, width=20)
entry.place(relx=0.38, rely=0.3)
entry.configure(font="Helvetica", justify="center", relief="flat")

# functions
def on_enter(event):
    event.widget.config(background="#ccccc4")

def on_leave(event):
    event.widget.config(background="#f0f0f0")

def check_plate():
    plate_number = entry.get()
    try:
        with open("parking_slot2.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if plate_number in line:
                    return messagebox.showinfo("Success", "Car is now registered to leave.")
            return messagebox.showerror("Error", "Plate number not found")  
    except FileNotFoundError:
        return False 


def exit_car():
    selected_item = entry.get()
    with open("parking_slot2.txt", "r") as file:
        global lines
        lines = file.readlines()
        for i, line in enumerate(lines):
            if selected_item in line:
                return i
    return -1  


def car_leave():
    selected_index = exit_car()
    if selected_index != -1 and selected_index > 0:
        for i in range(selected_index):
            with open("queue_parking.txt", "a") as file:
                file.write(f"{lines[i].strip()}\n")

            with open("queue_exit.txt", "a") as file:
                file.write(f"{lines[i].strip()}\n") 

            with open("parking_slot2.txt", "a") as file:
                file.write(f"{lines[i].strip()}\n")
    else:
        pass


def delete_lines_before_target():
    
    try:
        target_item = entry.get()
        with open('parking_slot2.txt', 'r') as f:
            lines = f.readlines()

        target_index = -1
        for i, line in enumerate(lines):
            if target_item in line:
                target_index = i
                break

        if target_index != -1:
            #Efficient way to keep lines after the target.
            new_lines = lines[target_index:]

            with open('parking_slot2.txt', 'w') as f:
                f.writelines(new_lines)
        else:
            pass

    except FileNotFoundError:
        print(f"Error: File not found.")


def remove_car():
    item_to_remove = entry.get()
    with open("parking_slot2.txt", 'r') as file:
        lines = file.readlines()

    with open("queue_exit.txt", 'a') as file:
        file.write(f"{item_to_remove}\n")

    modified_lines = [line for line in lines if item_to_remove not in line]

    with open("parking_slot2.txt", 'w') as file:
        file.writelines(modified_lines)

# buttons
register_button = tk.Button(window, text="Leave", font=("Helvetica", 10, "bold"), 
                            command=lambda: [check_plate(), exit_car(), car_leave(),
                                             delete_lines_before_target(), 
                                             remove_car(), 
                                             window.destroy()])
register_button.configure(height=1, width=10, relief="groove")
register_button.bind("<Enter>", on_enter)
register_button.bind("<Leave>", on_leave)
register_button.place(relx=0.495, rely=0.365)

center_window(window)
window.mainloop()
