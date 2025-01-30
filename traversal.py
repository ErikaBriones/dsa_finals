import tkinter as tk
from tkinter import messagebox
import math

def center_window(window):
    window.update_idletasks() 
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"+{x}+{y}")

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, values):
        if not values:
            return None

        self.root = Node(values[0])
        queue = [self.root]
        index = 1

        while queue:
            current = queue.pop(0)
            if index < len(values):
                current.left = Node(values[index])
                queue.append(current.left)
                index += 1
            if index < len(values):
                current.right = Node(values[index])
                queue.append(current.right)
                index += 1

    def inorder(self, node):
        return self.inorder(node.left) + [node.value] + self.inorder(node.right) if node else []

    def preorder(self, node):
        return [node.value] + self.preorder(node.left) + self.preorder(node.right) if node else []

    def postorder(self, node):
        return self.postorder(node.left) + self.postorder(node.right) + [node.value] if node else []


def get_tree_level():
    try:
        level = int(user_input.get())
        if level < 1 or level > 5:
            raise ValueError
        return level
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer between 1 and 5.")
        return None


def draw_tree(canvas, tree, root, x, y, width, level, max_level):
    if root is None:
        return

    offset = width // 1.8

    if root.left:
        canvas.create_line(x, y, x - offset, y + 50, arrow=tk.LAST, tags="lines")
        draw_tree(canvas, tree, root.left, x - offset, y + 60, width // 2, level + 1, max_level)

    if root.right:
        canvas.create_line(x, y, x + offset, y + 50, arrow=tk.LAST, tags="lines")
        draw_tree(canvas, tree, root.right, x + offset, y + 60, width // 2, level + 1, max_level)

    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="#fffbf1", width=1, tags="nodes")
    canvas.create_text(x, y, text=str(root.value), font=("Helvetica", 12), tags="nodes")


def generate_tree():
    level = get_tree_level()
    if level is None:
        return

    tree = BinaryTree()
    num_nodes = 2 ** level - 1  # max nodes for level
    values = list(range(1, num_nodes + 1))

    tree.insert(values)

    inorder_result = tree.inorder(tree.root)
    preorder_result = tree.preorder(tree.root)
    postorder_result = tree.postorder(tree.root)

    label_inorder.config(text=f"Inorder: {inorder_result}")
    label_preorder.config(text=f"Preorder: {preorder_result}")
    label_postorder.config(text=f"Postorder: {postorder_result}")

    canvas.delete("all")
    draw_tree(canvas, tree, tree.root, 400, 50, 350, 1, level)

# W I N D O W
root = tk.Tk()
root.title("Binary Tree")
root.geometry("880x590")
root.resizable(False,False)

# I N P U T
frame_input = tk.Frame(root, background="#c7b9a6", height=50, width=820, borderwidth=5, padx=5, pady=5)
frame_input.grid(row=0, sticky="w", padx=20, pady=10)

label_level = tk.Label(frame_input, text="Enter tree level from one (1) to five (5):", background="#c7b9a6", font=("Helvetica", 12))
label_level.pack(side=tk.LEFT)

user_input = tk.Entry(frame_input, font=("Helvetica", 12), justify="center", width=52)
user_input.pack(side=tk.LEFT)

button_done = tk.Button(frame_input, background="#e3ded1", text="Done", height=1, font=("Helvetica", 12), command=generate_tree)
button_done.pack(side=tk.LEFT, padx=10)

# O U T P U T
output_frame = tk.Frame(root, background="#e3ded1", height=120, width=832, borderwidth=5, padx=5, pady=5)
output_frame.grid(row=1, sticky="w", padx=20)
output_frame.grid_propagate(False)

title = tk.Label(output_frame, background="#e3ded1", text="TRAVERSALS", justify="left", font=("Helvetica", 12, "bold"))
title.grid(row=0, sticky="w")

label_inorder = tk.Label(output_frame, background="#e3ded1", text="Inorder: ", font=("Helvetica", 12))
label_inorder.grid(row=1, sticky="w")

label_preorder = tk.Label(output_frame, background="#e3ded1", text="Preorder: ", font=("Helvetica", 12))
label_preorder.grid(row=2, sticky="w")

label_postorder = tk.Label(output_frame, background="#e3ded1", text="Postorder: ", font=("Helvetica", 12))
label_postorder.grid(row=3, sticky="w")

canvas = tk.Canvas(root, width=820, height=350, bg="#ede1d2", bd=5)
canvas.grid(row=2, sticky="w", padx=20, pady=10)


def exit_message():
    exit = messagebox.askyesno("Exit", "Are you sure you want to close the program?")

    if exit:
        root.destroy()
        
                
center_window(root) 
root.protocol("WM_DELETE_WINDOW", exit_message)
root.mainloop()
