'''
Created on 26-Mar-2019

@author: RAR
'''
import tkinter as tk
from tkinter import messagebox
class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()
    
    
    
    
    
    def new_window(self):
        #self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2.alertMessage(self)

class Demo2:
        def alertMessage(self):
            messagebox.showinfo("Title", "a Tk MessageBox")


def main(): 
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()

        