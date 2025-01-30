import tkinter as tk
from tkinter import ttk, messagebox
import time

def center_window(window):
    window.update_idletasks() 
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"+{x}+{y}")

class SortingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("30 Integers Sorting Application")
        self.root.geometry("960x600")
        self.root.configure(bg="#CBB89D")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both')

        self.integers = []
        self.chosen_method = None

        self.create_input_tab()
        self.create_selection_tab()
        self.create_sorting_tab()
        self.create_result_tab()

    def create_input_tab(self):
        self.input_tab = ttk.Frame(self.notebook, style="Pink.TFrame")
        self.notebook.add(self.input_tab, text="Input")

        label = tk.Label(self.input_tab, text="Enter 30 integers separated by spaces:", font=("Arial", 14), bg="#CBB89D")
        label.pack(pady=20)

        self.input_entry = tk.Entry(self.input_tab, width=50, font=("Arial", 12))
        self.input_entry.pack(pady=10)

        submit_button = tk.Button(self.input_tab, text="Submit", command=self.process_input, bg="white", font=("Arial", 12))
        submit_button.pack(pady=20)

    def create_selection_tab(self):
        self.selection_tab = ttk.Frame(self.notebook, style="Pink.TFrame")
        self.notebook.add(self.selection_tab, text="Choose Method")

        label = tk.Label(self.selection_tab, text="Select a sorting method:", font=("Arial", 14), bg="#CBB89D")
        label.pack(pady=20)

        self.sorting_method = tk.StringVar(value="Bubble Sort")

        methods = ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Shell Sort", "Quick Sort", "Heap Sort"]
        for method in methods:
            radio = tk.Radiobutton(self.selection_tab, text=method, variable=self.sorting_method, value=method, font=("Arial", 12), bg="#CBB89D")
            radio.pack(anchor='w', padx=20)

        submit_button = tk.Button(self.selection_tab, text="Submit", command=self.process_selection, bg="white", font=("Arial", 12))
        submit_button.pack(pady=20)

    def create_sorting_tab(self):
        self.sorting_tab = ttk.Frame(self.notebook, style="Pink.TFrame")
        self.notebook.add(self.sorting_tab, text="Sorting")

        self.canvas = tk.Canvas(self.sorting_tab, width=500, height=300, bg="#CBB89D", highlightthickness=0)
        self.canvas.pack(pady=20)

        sort_button = tk.Button(self.sorting_tab, text="Sort", command=self.perform_sorting, bg="white", font=("Arial", 14, "bold"))
        sort_button.place(relx=0.5, y=20, anchor="n")

    def create_result_tab(self):
        self.result_tab = ttk.Frame(self.notebook, style="Pink.TFrame")
        self.notebook.add(self.result_tab, text="Result")
        self.result_title = tk.Label(self.result_tab, text="Sorted Integers:", font=("Arial", 16, "bold"), bg="#CBB89D")
        self.result_title.pack(pady=10)

        self.result_label = tk.Label(self.result_tab, text="", font=("Arial", 14), bg="#CBB89D", wraplength=500, justify="center")
        self.result_label.pack(pady=10)

    def process_input(self):
        try:
            user_input = self.input_entry.get()
            self.integers = list(map(int, user_input.split()))
            if len(self.integers) != 30:
                raise ValueError("You must enter exactly 30 integers.")
            messagebox.showinfo("Success", "Integers successfully submitted.")
            self.notebook.select(self.selection_tab)
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def process_selection(self):
        self.chosen_method = self.sorting_method.get()
        messagebox.showinfo("Selection", f"You chose {self.chosen_method}.")
        self.notebook.select(self.sorting_tab)

    def perform_sorting(self):
        if self.chosen_method == "Bubble Sort":
            self.bubble_sort()
        elif self.chosen_method == "Selection Sort":
            self.selection_sort()
        elif self.chosen_method == "Insertion Sort":
            self.insertion_sort()
        elif self.chosen_method == "Merge Sort":
            self.integers = self.merge_sort(self.integers)
        elif self.chosen_method == "Shell Sort":
            self.shell_sort()
        elif self.chosen_method == "Quick Sort":
            self.quick_sort(self.integers, 0, len(self.integers) - 1)
        elif self.chosen_method == "Heap Sort":
            self.heap_sort()

        self.display_result()
        self.notebook.select(self.result_tab)

    def bubble_sort(self):
        n = len(self.integers)
        for i in range(n):
            for j in range(0, n-i-1):
                self.animate_sorting(j, j+1)
                if self.integers[j] > self.integers[j+1]:
                    self.integers[j], self.integers[j+1] = self.integers[j+1], self.integers[j]

    def selection_sort(self):
        n = len(self.integers)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                self.animate_sorting(min_idx, j)
                if self.integers[j] < self.integers[min_idx]:
                    min_idx = j
            self.integers[i], self.integers[min_idx] = self.integers[min_idx], self.integers[i]

    def insertion_sort(self):
        for i in range(1, len(self.integers)):
            key = self.integers[i]
            j = i-1
            while j >= 0 and key < self.integers[j]:
                self.animate_sorting(j, j+1)
                self.integers[j+1] = self.integers[j]
                j -= 1
            self.integers[j+1] = key

    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            self.merge_sort(L)
            self.merge_sort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                self.animate_sorting(k, None)
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                self.animate_sorting(k, None)
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                self.animate_sorting(k, None)
                arr[k] = R[j]
                j += 1
                k += 1
        return arr

    def shell_sort(self):
        n = len(self.integers)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = self.integers[i]
                j = i
                while j >= gap and self.integers[j - gap] > temp:
                    self.animate_sorting(j - gap, j)
                    self.integers[j] = self.integers[j - gap]
                    j -= gap
                self.integers[j] = temp
            gap //= 2

    def quick_sort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                self.animate_sorting(i, j)
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        self.animate_sorting(i + 1, high)
        return i + 1

    def heap_sort(self):
        n = len(self.integers)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(self.integers, n, i)
        for i in range(n-1, 0, -1):
            self.integers[i], self.integers[0] = self.integers[0], self.integers[i]
            self.animate_sorting(0, i)
            self.heapify(self.integers, i, 0)

    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.animate_sorting(i, largest)
            self.heapify(arr, n, largest)

    def animate_sorting(self, index1, index2):
        self.canvas.delete("all")
        max_value = max(self.integers)
        bar_width = 15
        bar_spacing = 5
        x_offset = 10

        for i, value in enumerate(self.integers):
            bar_height = (value / max_value) * 200
            x1 = x_offset + i * (bar_width + bar_spacing)
            y1 = 300 - bar_height
            x2 = x1 + bar_width
            y2 = 300

            color = "white"
            if i == index1 or i == index2:
                color = "#858666"

            self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="#858666")

        self.root.update()
        time.sleep(0.1)

    def display_result(self):
        self.result_label.config(text=" ".join(map(str, self.integers)))

if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.configure("Pink.TFrame", background="#CBB89D")

    app = SortingApp(root)
    center_window(root)
    root.mainloop()