import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    
    if mode == "decrypt":
        shift = -shift  # Reverse shift for decryption

    for char in text:
        if char.isalnum() or char in "!@#$%^&*()-_=+[{]};:'\",<.>/?":
            result += chr((ord(char) + shift) % 256)  # Shift within ASCII range
        else:
            result += char  # Keep spaces and other characters unchanged

    return result

def process_text(mode):
    text = entry_text.get()
    try:
        shift = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("Error", "Shift value must be an integer!")
        return

    result = caesar_cipher(text, shift, mode)
    output_label.config(text=f"Result: {result}")

# Create GUI window
root = tk.Tk()
root.title("Advanced Caesar Cipher")
root.geometry("450x300")

# Widgets
tk.Label(root, text="Enter Text:").pack(pady=5)
entry_text = tk.Entry(root, width=50)
entry_text.pack(pady=5)

tk.Label(root, text="Enter Shift Value:").pack(pady=5)
entry_shift = tk.Entry(root, width=10)
entry_shift.pack(pady=5)

encrypt_button = tk.Button(root, text="Encrypt", command=lambda: process_text("encrypt"))
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(root, text="Decrypt", command=lambda: process_text("decrypt"))
decrypt_button.pack(pady=5)

output_label = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"), wraplength=400)
output_label.pack(pady=10)

# Run the GUI
root.mainloop()
