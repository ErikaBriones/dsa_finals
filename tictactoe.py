import tkinter as tk
import random

def center_window(window):
    window.update_idletasks() 
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"+{x}+{y}")

class TicTacToe:
    def __init__(self):
        self.app = tk.Tk()
        self.app.title("Tic Tac Toe")
        self.app.geometry('960x600')
        self.app.configure(background='#CBB89D')
        self.buttons = []
        self.current_player = 'X'
        self.winner = None
        self.create_board()

    def create_board(self):
        frame = tk.Frame(self.app, bg='#CBB89D')
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(frame, text='', font=('Arial', 24), width=6, height=3, command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)

    def on_button_click(self, row, col):
        if self.buttons[row][col]['text'] == '' and not self.winner:
            self.buttons[row][col]['text'] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
                self.show_winner_window()
            else:
                self.switch_player()

    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != '':
                return True
            if self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != '':
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != '':
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != '':
            return True
        return False

    def show_winner_window(self):
        winner_window = tk.Toplevel(self.app)
        winner_window.title("Winner")
        winner_window.geometry('500x500')
        winner_window.configure(background='#CBB89D')

        winner_window.update_idletasks()
        width = winner_window.winfo_width()
        height = winner_window.winfo_height()
        x = (self.app.winfo_rootx() + (self.app.winfo_width() // 2)) - (width // 2)
        y = (self.app.winfo_rooty() + (self.app.winfo_height() // 2)) - (height // 2)
        winner_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        tk.Label(winner_window, text=f"Player {self.winner} Wins!", font=('Arial', 20), bg='#CBB89D').pack(pady=20)
        canvas = tk.Canvas(winner_window, width=300, height=200, bg='#CBB89D', highlightthickness=0)
        canvas.pack()
        self.animate_confetti(canvas)

        tk.Button(winner_window, text="Play Again", 
                  command=lambda:[self.reset_game(), winner_window.destroy()], bg="white", 
                  font=("Arial", 14, "bold")).pack()
        
        tk.Button(winner_window, text="Close Game", 
                  command=lambda:[winner_window.destroy(), self.app.destroy()], bg="white", font=("Arial", 14, "bold")).pack()
        
    
    def animate_confetti(self, canvas):
        confetti_colors = ["red", "light blue", "light green", "light yellow", "purple", "orange"]

        def create_confetti():
            x = random.randint(0, 300)
            y = random.randint(0, 200)
            size = random.randint(5, 15)
            color = random.choice(confetti_colors)
            return canvas.create_oval(x, y, x + size, y + size, fill=color, outline=color)

        def move_confetti():
            for confetti in canvas.find_all():
                x_move = random.randint(-2, 2)
                y_move = random.randint(3, 6)
                canvas.move(confetti, x_move, y_move)
                coords = canvas.coords(confetti)
                if coords[3] > 200:
                    canvas.delete(confetti)
            canvas.after(50, move_confetti)

        for _ in range(50):
            create_confetti()
        move_confetti()

    def reset_game(self):
        self.current_player = 'X'
        self.winner = None
        for row in self.buttons:
            for button in row:
                button['text'] = ''

    def mainloop(self):
        self.app.mainloop()

if __name__ == '__main__':
    game = TicTacToe()
    center_window(game.app)
    game.mainloop()
