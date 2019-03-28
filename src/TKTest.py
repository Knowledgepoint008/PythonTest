'''
Created on 27-Mar-2019

@author: RAR
'''
import tkinter as tk

from doctest import master
from cgitb import text
from tkinter import mainloop, StringVar
from Tools.demo.sortvisu import WIDTH
from turtledemo.nim import Stick

class MainWindow:
    
    def __init__(self, master):
        self.master = master
        master.title("TK Test")
        
        self.frame = tk.Frame(master, width=500, height=400, bd=1)        
        #self.frame = tk.Frame(self.master, width = 202, height = 32, highlightbackground="black", highlightcolor="black", highlightthickness=1, bd=0)
        
        
        
        self.lblURL = tk.Label(self.frame, text = "URL", width = 6, borderwidth=2, relief="groove")
        self.lblURL.grid(row = 0, column = 0, padx = 2, pady = 2)
        
        self.txtURL = StringVar()
        self.txtURL = tk.Entry(self.frame)#, height = 1, width = 40, borderwidth=2, relief="groove")
        self.txtURL.grid(row = 0, column = 1, padx = 2, pady = 2)
        
        self.msgReqBody = tk.Text(self.frame, height = 5, width = 47, borderwidth=2, relief="groove")
        self.msgReqBody.grid(row = 1, column = 0, columnspan = 2, padx = 2, pady = 2)
        
        self.btnProcess = tk.Text(self.frame, text = Send, borderwidth=2, relief="groove")
        self.btnProcess.grid(row = 2, column = 1, padx = 2, pady = 2, sticky = "w")
        
        self.frame.pack()
        
def main():
    root = tk.Tk()
    app = MainWindow(root)
    mainloop()
    
if __name__ == '__main__':
    main()
    