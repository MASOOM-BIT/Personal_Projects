from logging import root
from tkinter import messagebox
from tkinter import *

def on_start():
    open_next_page()

def open_next_page():
    next_page = Toplevel(root)
    next_page.title("Dashboard")
    next_page.geometry("1000x600")
    next_page.configure(bg="#2E2E2E")
    
    Label(next_page, text="Dashboard", font=("Arial", 18), bg="#2E2E2E", fg="white").pack(pady=20)
    
    Button(next_page, text="Option 1", font=("Arial", 12), bg="#555", fg="white").pack(pady=10)
    Button(next_page, text="Option 2", font=("Arial", 12), bg="#555", fg="white").pack(pady=10)
    Button(next_page, text="Option 3", font=("Arial", 12), bg="#555", fg="white").pack(pady=10)
    
    Button(next_page, text="Close", font=("Arial", 12), bg="#555", fg="white", command=next_page.destroy).pack(pady=20)
