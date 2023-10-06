
'''
#vi_du:
from tkinter import Frame, Tk, Menu

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Simple Menu")

        menuBar = Menu(self.parent)
        self.parent.config(menu=menuBar)

        fileMenu = Menu(menuBar)
        fileMenu.add_command(label="Exit", command=self.onExit)
        menuBar.add_cascade(label="File", menu=fileMenu)

    def onExit(self):
        self.quit()

root = Tk()
root.geometry("250x150+300+300")
app = Example(root)
root.mainloop()
'''

'''
#menu_con:
from tkinter import Tk, Frame, Menu

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Submenu")
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        fileMenu = Menu(menubar)
        submenu = Menu(fileMenu)
        submenu.add_command(label="New feed")
        submenu.add_command(label="Bookmarks")
        submenu.add_command(label="Mail")
        fileMenu.add_cascade(label='Import', menu=submenu)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)            

    def onExit(self):
            self.quit()

root = Tk()
root.geometry("250x150+300+300")
app = Example(root)
root.mainloop()
'''

#popup_menu:

from tkinter import Tk, Frame, Menu

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Popup menu")
        self.menu = Menu(self.parent, tearoff=0)
        self.menu.add_command(label="Beep", command=self.bell())
        self.menu.add_command(label="Exit", command=self.onExit)
        self.parent.bind("<Button-3>", self.showMenu)
        self.pack()

    def showMenu(self, e):
        self.menu.post(e.x_root, e.y_root)

    def onExit(self):
        self.quit()

root = Tk()
root.geometry("250x150+300+300")
app = Example(root)
root.mainloop()