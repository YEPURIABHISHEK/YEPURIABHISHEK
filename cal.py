import tkinter as tk
from math import sin, cos, tan, log, sqrt

memory = 0  # To store the memory value

def on_click(event):
    global memory
    text = event.widget.cget("text")
    
    # Basic operations
    if text == "=":
        try:
            result = eval(str(entry_var.get()))
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    elif text == "M+":
        memory += float(entry_var.get())
    elif text == "M-":
        memory -= float(entry_var.get())
    elif text == "MR":
        entry_var.set(memory)
    else:
        entry_var.set(entry_var.get() + text)

root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("400x600")
root.configure(bg="#222")

# Create a frame with a white border
border_frame = tk.Frame(root, bd=10, bg="white")
border_frame.place(relwidth=1, relheight=1, relx=0.5, rely=0.5, anchor="center")

# Entry widget
entry_var = tk.StringVar()
entry = tk.Entry(border_frame, textvar=entry_var, font=("Arial", 24), justify="right", bd=10, relief=tk.FLAT, bg="#333", fg="white")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10)

buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+"),
    ("M+", "M-", "MR", "sin"),
    ("cos", "tan", "sqrt", "log"),
    ("**", "(", ")", "")
]

btn_bg = "#444"
btn_fg = "white"
btn_active_bg = "#666"
btn_font = ("Arial", 16, "bold")

# Create buttons and add them to the grid
for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        btn = tk.Button(border_frame, text=text, font=btn_font, padx=15, pady=15, bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, relief=tk.FLAT, borderwidth=3)
        btn.grid(row=i+1, column=j, sticky="nsew", padx=5, pady=5)
        btn.bind("<Button-1>", on_click)

# Center align the entire frame in the window
border_frame.grid_rowconfigure(0, weight=1)
border_frame.grid_rowconfigure(1, weight=1)
border_frame.grid_rowconfigure(2, weight=1)
border_frame.grid_rowconfigure(3, weight=1)
border_frame.grid_rowconfigure(4, weight=1)
border_frame.grid_rowconfigure(5, weight=1)
border_frame.grid_columnconfigure(0, weight=1)
border_frame.grid_columnconfigure(1, weight=1)
border_frame.grid_columnconfigure(2, weight=1)
border_frame.grid_columnconfigure(3, weight=1)

root.mainloop()
