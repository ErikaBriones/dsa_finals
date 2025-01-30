import tkinter as tk
from tkinter import messagebox
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

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if key < root.val:
                root.left = self.insert(root.left, key)
            else:
                root.right = self.insert(root.right, key)
        return root

    def inorder(self, root):
        return self.inorder(root.left) + [root.val] + self.inorder(root.right) if root else []

    def preorder(self, root):
        return [root.val] + self.preorder(root.left) + self.preorder(root.right) if root else []

    def postorder(self, root):
        return self.postorder(root.left) + self.postorder(root.right) + [root.val] if root else []

    def display_tree(self, root, canvas, x, y, dx, level=1, max_level=1):
        modx = dx // 0.5
        if root:
            if root.left:
                canvas.create_line(x, y, x - modx, y + 60, arrow=tk.LAST, tags="lines")
                self.display_tree(root.left, canvas, x - modx, y + 60, dx // 1.2, level + 2, max_level)
            if root.right:
                canvas.create_line(x, y, x + modx, y + 60, arrow=tk.LAST, tags="lines")
                self.display_tree(root.right, canvas, x + modx, y + 60, dx // 1.2, level + 2, max_level)

            canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="#fffbf1", tags="nodes")
            canvas.create_text(x, y, text=str(root.val), font=("Helvetica", 12), tags="nodes")

    def get_tree_depth(self, root):
        if not root:
            return 0
        left_depth = self.get_tree_depth(root.left)
        right_depth = self.get_tree_depth(root.right)
        return max(left_depth, right_depth) + 1

    def get_max_width(self, root):
        if not root:
            return 0
        left_width = self.get_max_width(root.left)
        right_width = self.get_max_width(root.right)
        return left_width + right_width + 1


class BSTApp:
    def __init__(self, root):
        self.bst = BinarySearchTree()
        self.root = root

        self.canvas_frame = tk.Frame(root, bg="#ede1d2", width=960, height=370,)
        self.canvas_frame.grid(row=2, sticky="w", padx=20, pady=10)
        self.canvas_frame.grid_propagate(False)

        self.canvas = tk.Canvas(self.canvas_frame, width=930, height=340, bg="#ede1d2", bd=5)
        self.canvas.grid(row=0, column=0)
        self.canvas.grid_propagate(False)

        self.v_scrollbar = tk.Scrollbar(self.canvas_frame, orient="vertical", command=self.canvas.yview, width=14)
        self.v_scrollbar.grid(row=0, column=1, sticky="ns")
        self.canvas.config(yscrollcommand=self.v_scrollbar.set)

        self.h_scrollbar = tk.Scrollbar(self.canvas_frame, orient="horizontal", command=self.canvas.xview, width=14)
        self.h_scrollbar.grid(row=1, column=0, sticky="ew")
        self.canvas.config(xscrollcommand=self.h_scrollbar.set)

        # I N P U T
        self.input_frame = tk.Frame(root, background="#c7b9a6", height=50, width=900, borderwidth=5, padx=5, pady=5)
        self.input_frame.grid(row=0, sticky="w", padx=20, pady=10)

        self.label = tk.Label(self.input_frame, font=("Helvetica", 12),
                              text="Enter up to 30 integers (separated by comma):", background="#c7b9a6")
        self.label.grid(row=0, column=0, padx=5)

        self.entry = tk.Entry(self.input_frame, font=("Helvetica", 12), width=50)
        self.entry.grid(row=0, column=1, padx=5)

        self.done_button = tk.Button(self.input_frame, background="#e3ded1", font=("Helvetica", 12), text="Done", command=self.add_integers, padx=5)
        self.done_button.grid(row=0, column=2, padx=5)

        self.clear_button = tk.Button(self.input_frame, background="#e3ded1", font=("Helvetica", 12), text="Clear", command=self.clear_tree, padx=5)
        self.clear_button.grid(row=0, column=3, padx=5)

        # O U T P U T
        self.output_frame = tk.Frame(root, background="#e3ded1", height=120, width=960, borderwidth=5, padx=5, pady=5)
        self.output_frame.grid(row=1, sticky="w", padx=20)
        self.output_frame.grid_propagate(False)

        self.title = tk.Label(self.output_frame, background="#e3ded1", text="TRAVERSALS", justify="left", font=("Helvetica", 12, "bold"))
        self.title.grid(row=0, sticky="w")

        self.inorder_label = tk.Label(self.output_frame, background="#e3ded1", text="Inorder:", justify="left", font=("Helvetica", 12))
        self.inorder_label.grid(row=1, sticky="w")

        self.preorder_label = tk.Label(self.output_frame, background="#e3ded1", text="Preorder:", justify="left", font=("Helvetica", 12))
        self.preorder_label.grid(row=2, sticky="w")

        self.postorder_label = tk.Label(self.output_frame, background="#e3ded1", text="Postorder:", justify="left", font=("Helvetica", 12))
        self.postorder_label.grid(row=3, sticky="w")

    def add_integers(self):
        input_text = self.entry.get().strip()
        try:
            numbers = [int(x) for x in input_text.split(",") if x.strip()]
            if len(numbers) > 30:
                messagebox.showerror("Error", "You can only enter a maximum of 30 integers.")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers separated by commas.")
            return

        self.bst.root = None  # clear
        for num in numbers:
            self.bst.root = self.bst.insert(self.bst.root, num)

        self.input_list = numbers
        self.display_tree()

    def show_traversals(self):
        inorder = self.bst.inorder(self.bst.root)
        preorder = self.bst.preorder(self.bst.root)
        postorder = self.bst.postorder(self.bst.root)

        self.inorder_label.config(text=f"Inorder: {inorder}")
        self.preorder_label.config(text=f"Preorder: {preorder}")
        self.postorder_label.config(text=f"Postorder: {postorder}")

    def display_tree(self):
        self.canvas.delete("all")

        tree_depth = self.bst.get_tree_depth(self.bst.root)  # depth
        max_width = self.bst.get_max_width(self.bst.root)

        canvas_width = max(950, max_width * 60)
        canvas_height = max(400, tree_depth * 80)

        self.canvas.config(scrollregion=(0, 0, canvas_width, canvas_height))
        self.bst.display_tree(self.bst.root, self.canvas, canvas_width // 2, 40, canvas_width // (max_width * 2))
        self.show_traversals()

    def clear_tree(self):
        self.canvas.delete("all")
        self.entry.delete(0, tk.END)
        self.inorder_label.config(text="Inorder:")
        self.preorder_label.config(text="Preorder:")
        self.postorder_label.config(text="Postorder:")
        self.input_list = []


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Binary Search Tree")
    root.geometry("1000x600")
    root.resizable(False, False)
    app = BSTApp(root)

    def exit_message():
        exit = messagebox.askyesno("Exit", "Are you sure you want to close the program?")

        if exit:
            root.destroy()
            
                   
    center_window(root) 
    root.protocol("WM_DELETE_WINDOW", exit_message)
    root.mainloop()
