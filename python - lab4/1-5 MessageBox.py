
'''
#Message Box:
from tkinter.ttk import Frame, Button
from tkinter import Tk, BOTH
import tkinter.messagebox as mbox

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Message Boxes")
        self.pack()

        error = Button(self, text="Error", command=self.onError)
        error.grid(padx=5, pady=5)
        warning = Button(self, text="Warning", command=self.onWarn)
        warning.grid(row=1, column=0)
        question = Button(self, text="Question", command=self.onQuest)
        question.grid(row=0, column=1)
        inform = Button(self, text="Information", command=self.onInfo)
        inform.grid(row=1, column=1)

    def onError(self):
        mbox.showerror("Error", "Could not open file")

    def onWarn(self):
        mbox.showwarning("Warning", "Deprecated function call")

    def onQuest(self):
        mbox.askquestion("Question", "Are you sure to quit?")

    def onInfo(self):
        mbox.showinfo("Information", "Download completed")

root = Tk()
ex = Example(root)
root.geometry("300x150+300+300")
root.mainloop()
'''
'''
#Color chooser:
from tkinter import Tk, Frame, Button, BOTH, SUNKEN
from tkinter.colorchooser import askcolor

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        
        self.parent = parent
        self.initUI()
        
    def initUI(self):
        self.parent.title("Color Chooser")
        self.pack(fill=BOTH, expand =1 )
        
        self.btn = Button(self, text="Choose Color", command=self.onChoose)
        self.btn.place(x=30, y=30)
        
        self.frame = Frame(self, border = 1, relief = SUNKEN, width = 100 , height = 100)
        self.frame.place(x=160, y=30)
        
    def onChoose(self):
        (rgb, hx) = askcolor()
        self.frame.config(bg = hx)
        
root = Tk()
ex = Example(root)
root.geometry("300x150+300+300")
root.mainloop()
'''
#File Dialog:

from tkinter import Frame, Tk, BOTH, Text, Menu, END
from tkinter.filedialog import Open

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("File dialog")
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        menubar.add_cascade(label="File", menu=fileMenu)

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)

    def onOpen(self):
        ftypes = [('Python files', '*.py'), ('All files', '*')]
        dlg = Open(self, filetypes = ftypes)
        fl = dlg.show()
        if fl != '':
            text = self.readFile(fl)
            self.txt.insert(END, text)
    
    def readFile(self, filename):
        f = open(filename, "r")
        text = f.read()
        return text

root = Tk()
ex = Example(root)
root.geometry("300x250+300+300")
root.mainloop()  