from tkinter import *
from functions import on_start
from functions import open_next_page
# Create the main window
root = Tk()
root.title("Bookkeeping App")
root.geometry("1000x600")
root.configure(bg="#2E2E2E")  # Setting a dark background

# Menu Bar
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

# Welcome Label
welcome_label = Label(root, text="Welcome to Bookkeeping App", font=("Arial", 14), bg="#2E2E2E", fg="white")
welcome_label.pack(pady=20)

# Start Button
start_button = Button(root, text="Start", font=("Arial", 18), command=on_start, bg="#555", fg="white")
start_button.pack(pady=50)
start_button.place(relx=0.5, rely=0.5, anchor=CENTER)

# Copyright Label
copyright_label = Label(root, text="© 2025 Bookkeeping App by @M.R.Ansari", font=("Arial", 10), bg="#2E2E2E", fg="white")
copyright_label.pack(side="bottom", pady=10)

# Run the Tkinter event loop
root.mainloop()
