import random
import string
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

def generate_password():
    try:
        length = int(entry_length.get())
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(length))
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except:
        messagebox.showerror("Error", "Please enter a valid number")

tk.Label(root, text="Enter Password Length:").pack(pady=5)
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=5)

entry_password = tk.Entry(root, width=40)
entry_password.pack(pady=10)

root.mainloop()

