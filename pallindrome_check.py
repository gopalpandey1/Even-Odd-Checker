import tkinter as tk 
from tkinter import messagebox

def pallindrome(event=None):
    try:
      num=entry.get()
      if not num.strip().isdigit():
        messagebox.showerror("Invalid input","Please enter a valid integer")
        return
      if str(num) == str(num)[::-1]:
         result.config(text=f"{num} is a pallindrome number !",fg='green')
      else:
         result.config(text=f"{num} is not a pallindrome number !",fg='red')
    except ValueError:
       result.config(text="Invalid input ",fg='red')



def refresh():
   entry.delete(0, tk.END)
   result.config(text="")

          
  


root=tk.Tk()
root.title("Pallindrome Check")
root.configure(bg="skyblue")
root.geometry("500x300")
root.resizable(False,False)


label=tk.Label(root,text="Pallindrome number checker ! ",font=('Arial',18),bg='skyblue', fg='blue')
label.pack(pady=10)

label2=tk.Label(root,text="Enter the number :-",font=('Arial',12),bg="skyblue")
label2.pack(pady=3)

entry= tk.Entry(root, font=('Arial',12),justify='center',borderwidth=(5),bg='lightblue')
entry.pack(pady=5)

entry.focus_set()#########

check_button= tk.Button(root,text="Check",command=pallindrome,font=('Arial',12),bg='lightblue',borderwidth=(5))
check_button.pack(pady=10)


refresh_button=  tk.Button(root, text="Refresh",command=refresh,font=('Arial',12),bg='lightblue',borderwidth=(5))
refresh_button.pack(pady=10)


result=tk.Label(root,text="",font=('Arial',14),bg='skyblue')
result.pack(pady=10)



root.bind("<Return>",pallindrome)




root.mainloop()
