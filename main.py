import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from pypdf import PdfReader, PdfWriter
import os


def encrypt_pdf(input_path, password):
    reader = PdfReader(input_path)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(user_password=password, owner_password=password, use_128bit=True)

    with open(input_path, "wb") as f:
        writer.write(f)


# Tkinter GUI
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select PDF file",
    filetypes=[("PDF files", "*.pdf")]
)

if not file_path:
    messagebox.showinfo("Cancelled", "No file selected. Exiting.")
    exit()

password = simpledialog.askstring("Password", "Enter password for PDF:", show='*')
if not password:
    messagebox.showinfo("Cancelled", "No password entered. Exiting.")
    exit()

try:
    encrypt_pdf(file_path, password)
    messagebox.showinfo("Success", f"Your PDF is now password protected:\n{file_path}")
except Exception as e:
    messagebox.showerror("Error", f"Encryption failed:\n{e}")
