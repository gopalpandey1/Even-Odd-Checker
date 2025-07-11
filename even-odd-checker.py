import tkinter as tk
from tkinter import messagebox

def check(event=None):
    num=entry.get()
    if not num.strip().isdigit():
        messagebox.showerror("Invalid input","Please enter a valid integer")
        return
    number = int(num)
    if number%2==0:
        result_label.config(text=f"{number} is Even ",fg="green")
    else:
        result_label.config(text=f"{number} is Odd ",fg="red")

root=tk.Tk()
root.title("Even Odd Check")
root.configure(bg="skyblue")
root.geometry("500x200")
root.resizable(False,False)


label=tk.Label(root,text="Enter a number :",font=('Arial',18),bg='skyblue')
label.pack(pady=10)

entry= tk.Entry(root, font=('Arial',12),justify='center',borderwidth=(5),bg='lightblue')
entry.pack(pady=5)
entry.focus_set()

check_button= tk.Button(root,text="Check",command=check,font=('Arial',12),bg='lightblue')
check_button.pack(pady=10)

result_label=tk.Label(root,text="",font=('Arial',14),bg='skyblue')
result_label.pack(pady=10)

root.bind("<Return>",check)

root.mainloop()
