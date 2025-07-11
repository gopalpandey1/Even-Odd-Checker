import tkinter as tk
from tkinter import messagebox



def pop():
    
    entry.delete(0, tk.END)
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)
    entry5.delete(0, tk.END)
    entry6.delete(0, tk.END)
    entry7.delete(0, tk.END)
    entry8.delete(0, tk.END)
    entry9.delete(0, tk.END)
    entry10.delete(0, tk.END)
    entry11.delete(0, tk.END)
    entry12.delete(0, tk.END)
    entry13.delete(0, tk.END)
    result.config(text="")
    messagebox.showinfo("Succesfull","Data inserted successfully  !")




root=tk.Tk()
root.title("Student form")
root.configure(background="lightblue")
root.geometry('890x470')
root.resizable(False,False)





label=tk.Label(root,text="Name :",font=('Arial',12),bg='lightblue')
label.grid(row=0,column=0,padx=70,pady=12)
entry=tk.Entry(root, width=20 , font=('Arial',13))
entry.grid(row=0,column=1)

label1=tk.Label(root,text="Address :",font=('Arial',12),bg='lightblue')
label1.grid(row=1,column=0,padx=12,pady=12)
entry1=tk.Entry(root, width=20 , font=('Arial',13))
entry1.grid(row=1,column=1)

label2=tk.Label(root,text="Contact :",font=('Arial',12),bg='lightblue')
label2.grid(row=2,column=0,padx=12,pady=12)
entry2=tk.Entry(root, width=20 , font=('Arial',13))
entry2.grid(row=2,column=1)

label3=tk.Label(root,text="Email :",font=('Arial',12),bg='lightblue')
label3.grid(row=3,column=0,padx=12,pady=12)
entry3=tk.Entry(root, width=20 , font=('Arial',13))
entry3.grid(row=3,column=1)

label4=tk.Label(root,text="State :",font=('Arial',12),bg='lightblue')
label4.grid(row=4,column=0,padx=12,pady=12)
entry4=tk.Entry(root, width=20 , font=('Arial',13))
entry4.grid(row=4,column=1)

label5=tk.Label(root,text="Qualification :",font=('Arial',12),bg='lightblue')
label5.grid(row=5,column=0,padx=12,pady=12)
entry5=tk.Entry(root, width=20 , font=('Arial',13))
entry5.grid(row=5,column=1)

label6=tk.Label(root,text="Passing Year :",font=('Arial',12),bg='lightblue')
label6.grid(row=6,column=0,padx=12,pady=12)
entry6=tk.Entry(root, width=20 , font=('Arial',13))
entry6.grid(row=6,column=1)


label7=tk.Label(root,text="Father Name :",font=('Arial',12),bg='lightblue')
label7.grid(row=0,column=7,padx=40,pady=12)
entry7=tk.Entry(root, width=20 , font=('Arial',13))
entry7.grid(row=0,column=8)

label8=tk.Label(root,text="Mother Name :",font=('Arial',12),bg='lightblue')
label8.grid(row=1,column=7,padx=40,pady=12)
entry8=tk.Entry(root, width=20 , font=('Arial',13))
entry8.grid(row=1,column=8)

label9=tk.Label(root,text="Collage Name :",font=('Arial',12),bg='lightblue')
label9.grid(row=2,column=7,padx=40,pady=12)
entry9=tk.Entry(root, width=20 , font=('Arial',13))
entry9.grid(row=2,column=8)


label10=tk.Label(root,text="Branch :",font=('Arial',12),bg='lightblue')
label10.grid(row=3,column=7,padx=40,pady=12)
entry10=tk.Entry(root, width=20 , font=('Arial',13))
entry10.grid(row=3,column=8)


label11=tk.Label(root,text="Joining Year :",font=('Arial',12),bg='lightblue')
label11.grid(row=4,column=7,padx=40,pady=12)
entry11=tk.Entry(root, width=20 , font=('Arial',13))
entry11.grid(row=4,column=8)

label12=tk.Label(root,text="Mother Tounge :",font=('Arial',12),bg='lightblue')
label12.grid(row=5,column=7,padx=40,pady=12)
entry12=tk.Entry(root, width=20 , font=('Arial',13))
entry12.grid(row=5,column=8)

label13=tk.Label(root,text="Country :",font=('Arial',12),bg='lightblue')
label13.grid(row=6,column=7,padx=40,pady=12)
entry13=tk.Entry(root, width=20 , font=('Arial',13))
entry13.grid(row=6,column=8)

check_button= tk.Button(root,text="Submit",command=pop,font=('Arial',12),bg='lightblue',borderwidth=(5))
check_button.grid(row=15,column=5,pady=18)



result=tk.Label(root,text="",font=('Arial',14),bg='lightblue')
result.grid(pady=10)

root.mainloop()




