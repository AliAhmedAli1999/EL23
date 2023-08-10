import tkinter as tk
import tkinter.messagebox
   
root = tk.Tk()
root.withdraw()
dataBase = {
    "Ahmed" : 1349,
    "Ali" : 6078,
    "Amr" : 9345
}

userName = input("Enter your user name : ")
Password = int(input("Enter your password : "))

if userName  in dataBase and dataBase[userName] == Password  :
    tk.messagebox.showinfo("","Hello")  
else :
    tk.messagebox.showwarning("","incorrect entry")  