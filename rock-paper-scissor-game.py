import random
import tkinter as tk
from tkinter import PhotoImage
import os

# Initialize high score
high_score = 0

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(player_choice):
    global high_score
    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    
    if result == "You win!":
        update_high_score()

def update_high_score():
    global high_score
    high_score += 1
    high_score_label.config(text=f"High Score: {high_score}")

def reset_high_score():
    global high_score
    high_score = 0
    high_score_label.config(text=f"High Score: {high_score}")

def show_start_screen():
    global start_window
    start_window = tk.Tk()
    start_window.title("Rock Paper Scissors")
    start_window.geometry("400x300")
    start_window.configure(bg="#ADD8E6")
    
    tk.Label(start_window, text="Rock Paper Scissors", font=("Arial", 20, "bold"), bg="#ADD8E6").pack(pady=20)
    
    tk.Button(start_window, text="Enter Game", font=("Arial", 16), command=start_game).pack(pady=20)
    
    start_window.mainloop()

def start_game():
    start_window.destroy()
    create_gui()

def create_gui():
    global result_label, high_score_label
    
    root = tk.Tk()
    root.title("Rock Paper Scissors")
    root.geometry("500x600")

    # Check if background image exists
    bg_image_path = "background.png"
    if os.path.exists(bg_image_path):
        bg_image = PhotoImage(file=bg_image_path)
        background_label = tk.Label(root, image=bg_image)
        background_label.place(relwidth=1, relheight=1)
    else:
        root.configure(bg="#ADD8E6")  # Use a light blue background if no image
    
    # Title
    title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 24, "bold"), bg="#ADD8E6")
    title_label.pack(pady=20)
    
    # High Score Display
    high_score_label = tk.Label(root, text=f"High Score: {high_score}", font=("Arial", 18), bg="#ADD8E6")
    high_score_label.pack(pady=10)
    
    # Buttons for choices
    button_frame = tk.Frame(root, bg="#ADD8E6")
    button_frame.pack()
    
    rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 16), command=lambda: play_game("rock"))
    rock_button.grid(row=0, column=0, padx=10, pady=10)
    
    paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 16), command=lambda: play_game("paper"))
    paper_button.grid(row=0, column=1, padx=10, pady=10)
    
    scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 16), command=lambda: play_game("scissors"))
    scissors_button.grid(row=0, column=2, padx=10, pady=10)
    
    # Reset High Score Button
    reset_button = tk.Button(root, text="Reset High Score", font=("Arial", 16), command=reset_high_score)
    reset_button.pack(pady=10)
    
    # Result Display
    result_label = tk.Label(root, text="Choose an option to play!", font=("Arial", 18), bg="#ADD8E6")
    result_label.pack(pady=30)
    
    root.mainloop()

if __name__ == "__main__":
    show_start_screen()

