import tkinter as tk 
from tkinter import messagebox

def vote(event=None):
    age=entry.get()
    if not age.strip().isdigit():
        messagebox.showerror("Invalid input","Please enter a valid age (in digits)")
        return
    number = int(age)
    if number>=18:
        result_label.config(text=f"Your age is {number}\n  You can vote! . ",fg="green")
    else:
        result_label.config(text=f"You are not 18 above , your age is {number} \n You can not vote ! . ",fg="red")


root=tk.Tk()
root.title("Vote Egilibility")
root.configure(bg="skyblue")
root.geometry("500x250")
root.resizable(False,False)

label=tk.Label(root,text="Enter your age :",font=('Arial',18),bg='skyblue')
label.pack(pady=10)

entry= tk.Entry(root, font=('Arial',12),justify='center',borderwidth=(5),bg='lightblue')
entry.pack(pady=5)
entry.focus_set()


check_button= tk.Button(root,text="Check",command=vote,font=('Arial',12),bg='lightblue')
check_button.pack(pady=10)


result_label=tk.Label(root,text="",font=('Arial',14),bg='skyblue')
result_label.pack(pady=10)


root.bind("<Return>",vote)


root.mainloop()
