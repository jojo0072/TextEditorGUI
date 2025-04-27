import tkinter as tk
from tkinter import messagebox, filedialog

root=tk.Tk()
title_str=tk.StringVar()
title_str.set("Untitled - Editor")
root.title(title_str.get())

root.geometry("400x300")

menubar=tk.Menu(root)
file=tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file)

def new():
    global file_path
    if messagebox.askyesno("Exit application","Do you want to save changes?"):
        save()
    text_field.delete(1.0, tk.END)
    file_path=None
    title_str.set("Untitled - Editor")
    root.title(title_str.get())  

file.add_command(label="New", command=new)

def openf(*args):  
    global file_path
    file_path=filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])   
    if file_path:
        with open(file_path, "r") as f:
            content=f.read()
            text_field.delete(1.0, tk.END)
            text_field.insert(1.0 , content)
            title_str.set(file_path.rsplit("/", 1)[1])
            root.title(title_str.get())

file.add_command(label="Open", command=openf)

def save(*args):
    if title_str.get()=="Untitled - Editor":
        save_as()
    else:
        with open(file_path, "w") as f:
            f.write(text_field.get(1.0, tk.END))    
        messagebox.showinfo("Information", "File is saved!")    

file.add_command(label="Save", command=save)

def save_as(*args):
    global file_path
    file_path=filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as f:
            f.write(text_field.get(1.0, tk.END))
            title_str.set(file_path.rsplit("/", 1)[1])
            root.title(title_str.get())

file.add_command(label="Save as", command=save_as)

def exit():
    if messagebox.askyesno("Exit application","Do you want to save changes?"):
        save()
    root.destroy()

file.add_command(label="Exit", command=exit)

text_field=tk.Text(root, font=("Times New Roman", 12), highlightcolor="blue")
text_field.pack(padx=15, pady=15, side=tk.TOP)

root.config(menu=menubar)
root.mainloop()