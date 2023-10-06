
'''
#checkbutton:
from tkinter import Tk,Frame,Checkbutton
from tkinter import BooleanVar, BOTH

class example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("CheckButton")
        self.pack(fill=BOTH, expand=True)
        self.var = BooleanVar()

        cb = Checkbutton(self, text="Show title", variable=self.var, command=self.onClick)
        cb.select()
        cb.place(x=50, y=50)

    def onClick(self):
        if self.var.get() == True:
            self.master.title("Checkbutton")
        else:
            self.master.title("")

root = Tk()
root.geometry("250x150+300+300")
app = example(root)
root.mainloop()
'''

'''
#Label:
from PIL import Image, ImageTk
from tkinter import Tk, Frame, Label

class example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent= parent
        self.initUI()

    def initUI(self):
        self.parent.title("Label")

        self.img = Image.open("example.jpg")
        exp = ImageTk.PhotoImage(self.img)
        label = Label(self, image=exp)

        label.image = exp

        label.pack()
        self.pack()

    def setGeometry(self):
        w, h = self.img.size
        self.parent.geometry(("%dx%d+300+300") % (w, h))

root = Tk()
app = example(root)
app.setGeometry()
root.mainloop()
'''

'''
#Scale:
from tkinter import Tk, BOTH, IntVar, LEFT
from tkinter.ttk import Frame, Label, Scale, Style

class example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent= parent
        self.initUI()

    def initUI(self):
        self.parent.title("Scale")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=1)

        scale = Scale(self, from_=0, to=100, command=self.onScale)
        scale.pack(side=LEFT, padx =15)

        self.var = IntVar()
        self.label = Label(self, text=0, textvariable=self.var)
        self.label.pack(side=LEFT)

    def onScale(self, val):
        v= int(float(val))
        self.var.set(v)

root = Tk()
ex = example(root)
root.geometry("250x100+300+300")
root.mainloop()
'''

#'''
#ListBox:
from tkinter.ttk import Frame, Label
from tkinter import Tk, BOTH, Listbox, StringVar, END

class example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent= parent
        self.initUI()

    def initUI(self):
        self.parent.title("ListBox")
        self.pack(fill=BOTH, expand=1)
        acts = ["Kem", "Banh ran", "Nuoc ngot", "Banh bao"]

        lb = Listbox(self)

        for i in acts:
            lb.insert(END,i)

        lb.bind("<<ListBoxSelect>>", self.onSelect)

        lb.pack(pady=15)

        self.var = StringVar()
        self.label = Label(self, text=0, textvariable=self.var)
        self.label.pack()
    
    def onSelect(self, val):
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)

        self.var.set(value)

root = Tk()
ex = example(root)
root.geometry("300x250+300+300")
root.mainloop()
#'''

'''
#AutoScaleImage
from PIL import Image, ImageTk
from tkinter import Tk, Frame, Label, N, S, E, W

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Label")

        # Load the original image
        self.original_img = Image.open("example.jpg")
        self.exp = ImageTk.PhotoImage(self.original_img)

        # Create a label to display the image
        self.label = Label(self, image=self.exp)
        self.label.grid(sticky=(N, S, E, W))

        # Configure grid row and column to expand with window resize
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Bind the window resize event to the on_resize method
        self.parent.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        new_width = event.width
        new_height = event.height

        # Resize the image based on the new window dimensions
        self.resized_img = self.original_img.resize((new_width, new_height), Image.ANTIALIAS)
        self.exp = ImageTk.PhotoImage(self.resized_img)

        # Update the image in the label
        self.label.config(image=self.exp)

if __name__ == "__main__":
    root = Tk()
    app = Example(root)
    root.mainloop()
'''