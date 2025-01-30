import tkinter as tk
from PIL import ImageTk, Image


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
window.title("Credits")
window.geometry("960x600")
window.configure(background="#FFB6C1")
window.resizable(False, False)

label1 = tk.Label(window, text="Here are the programmers of the project:", 
                  font=("Helvetica", 18, "bold"), background="#FFB6C1", fg="#723748")
label1.place(relx=0.02, rely=0.02)

image = Image.open("alyssa.png")
resized_image = image.resize((210, 210))
img = ImageTk.PhotoImage(resized_image)
alyssa_label = tk.Label(window, image=img)
alyssa_label.image = img
alyssa_label.configure(background="#FFB6C1")
alyssa_label.place(relx=0.18, rely=0.1)

label3 = tk.Label(window, text="Alyssa Alipio", font=("Helvetica", 18, "bold"), 
                  background="#FFB6C1", fg="#723748")
label3.place(relx=0.21, rely=0.45)

image = Image.open("nana.png")
resized_image = image.resize((210, 210))
img = ImageTk.PhotoImage(resized_image)
nana_label = tk.Label(window, image=img)
nana_label.image = img
nana_label.configure(background="#FFB6C1")
nana_label.place(relx=0.58, rely=0.1)

label4 = tk.Label(window, text="Eaila Mae Nana Aguylo", font=("Helvetica", 18, "bold"), 
                  background="#FFB6C1", fg="#723748")
label4.place(relx=0.55, rely=0.45)

image = Image.open("erika.png")
resized_image = image.resize((210, 210))
img = ImageTk.PhotoImage(resized_image)
erika_label = tk.Label(window, image=img)
erika_label.image = img
erika_label.configure(background="#FFB6C1")
erika_label.place(relx=0.18, rely=0.55)

label5 = tk.Label(window, text="Erika Briones", font=("Helvetica", 18, "bold"), 
                  background="#FFB6C1", fg="#723748")
label5.place(relx=0.2, rely=0.9)

image = Image.open("kate.png")
resized_image = image.resize((210, 210))
img = ImageTk.PhotoImage(resized_image)
kate_label = tk.Label(window, image=img)
kate_label.image = img
kate_label.configure(background="#FFB6C1")
kate_label.place(relx=0.58, rely=0.55)

label6 = tk.Label(window, text="Kate Anne Trisha Quibo", font=("Helvetica", 18, "bold"), 
                  background="#FFB6C1", fg="#723748")
label6.place(relx=0.55, rely=0.9)


center_window(window)
window.mainloop()