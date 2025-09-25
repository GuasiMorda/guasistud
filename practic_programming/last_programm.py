import tkinter as tk
from tkinter import messagebox
import random
import time

class ShellGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Угадай где шарик")
        self.root.geometry("400x300")
        
        self.score = 0
        self.rounds = 0
        self.ball_position = 0
        self.game_phase = "show"
        
        self.setup_ui()
        self.new_round()
        self.root.mainloop()
    
    def setup_ui(self):
        self.score_label = tk.Label(self.root, text="Счёт: 0", font=("Arial", 14))
        self.score_label.pack(pady=10)
        
        self.canvas = tk.Canvas(self.root, width=400, height=150, bg="lightblue")
        self.canvas.pack(pady=10)
        
        self.shells = []
        self.draw_shells()
        
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        for i in range(3):
            btn = tk.Button(button_frame, text=f"Стаканчик {i+1}", font=("Arial", 12),
                           command=lambda idx=i: self.guess(idx), width=10, state=tk.DISABLED)
            btn.pack(side=tk.LEFT, padx=5)
            self.shells.append(btn)
        
        self.start_btn = tk.Button(self.root, text="Начать раунд", font=("Arial", 12),
                                  command=self.start_round)
        self.start_btn.pack(pady=5)
    
    def draw_shells(self, show_ball=False):
        self.canvas.delete("all")
        for i in range(3):
            x = 50 + i * 120
            self.canvas.create_rectangle(x, 50, x+80, 120, fill="brown", outline="black", width=2)
            self.canvas.create_text(x+40, 35, text=str(i+1), font=("Arial", 14, "bold"))
            
            if show_ball and i == self.ball_position:
                self.canvas.create_oval(x+25, 85, x+55, 115, fill="red")
    
    def new_round(self):
        self.ball_position = random.randint(0, 2)
        self.game_phase = "show"
        self.start_btn.config(state=tk.NORMAL, text="Начать раунд")
        for btn in self.shells:
            btn.config(state=tk.DISABLED)
        self.draw_shells(show_ball=False)
    
    def start_round(self):
        self.start_btn.config(state=tk.DISABLED)

        self.draw_shells(show_ball=True)
        self.root.update()
        self.root.after(1500, self.shuffle_shells)
    
    def shuffle_shells(self):

        self.draw_shells(show_ball=False)
        
        for i in range(10):
            self.root.update()
            time.sleep(0.1)
            self.ball_position = random.randint(0, 2)

        self.game_phase = "guess"
        for btn in self.shells:
            btn.config(state=tk.NORMAL)
    
    def guess(self, shell_index):
        if self.game_phase != "guess":
            return
            
        for btn in self.shells:
            btn.config(state=tk.DISABLED)

        self.draw_shells(show_ball=True)
        self.root.update()
        
        if shell_index == self.ball_position:
            self.score += 10
            messagebox.showinfo("Результат", "Поздравляем! Вы нашли шарик!")
        else:
            messagebox.showinfo("Результат", f"Шарик был под напёрстком {self.ball_position+1}!")
        
        self.rounds += 1
        self.score_label.config(text=f"Счёт: {self.score} | Раундов: {self.rounds}")
        
        self.root.after(2000, self.new_round)

ShellGame()