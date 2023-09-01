import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os

class Notepad:
    def __init__(self, **kwargs):
        self.root = Tk()
        self.width = 400
        self.height = 400
        self.text = Text(self.root)
        self.menubar = Menu(self.root)
        self.file = Menu(self.menubar, tearoff=0)
        self.edit = Menu(self.menubar, tearoff=0)
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.scrollbar = Scrollbar(self.text)
        self.fileb = None

        try:
            self.root.wm_iconbitmap("Notepad.ico")
        except:
            pass

        try:
            self.width = kwargs['width']
        except KeyError:
            pass
        try:
            self.height = kwargs['height']
        except KeyError:
            pass
        self.root.title("untitled")
        screenwidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()
        left = (screenwidth/2) - (self.width/2)
        top = (screenHeight/2) - (self.height/2)
        self.root.geometry('%dx%d+%d+%d' % (self.width, self.height, left, top))
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.text.grid(sticky=N+E+S+W)
        
        self.file.add_command(label="New", command=self.newfile)
        self.file.add_command(label="Open", command=self.openfile)
        self.file.add_command(label="Save", command=self.savefile)
        self.file.add_separator()
        self.file.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(label="File", menu=self.file)
        self.edit.add_command(label="Cut", command=self.cut)
        self.edit.add_command(label="Copy", command=self.copy)
        self.edit.add_command(label="Paste", command=self.paste)
        self.menubar.add_cascade(label="Edit", menu=self.edit)
        self.helpmenu.add_command(label="About", command=self.showabout)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.scrollbar.set)
        
        self.root.config(menu=self.menubar)

    def quit(self):
        self.root.destroy()

    def showabout(self):
        showinfo("notepad", "mrinal verma")

    def newfile(self):
        self.root.title("untitled")
        self.fileb = None
        self.text.delete(1.0, END)

    def openfile(self):
        self.fileb = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if self.fileb == "":
            self.fileb = None
        else:
            self.root.title(os.path.basename(self.fileb) + " - Notepad")
            self.text.delete(1.0, END)
            with open(self.fileb, "r") as file:
                self.text.insert(1.0, file.read())

    def savefile(self):
        if self.fileb is None:
            self.fileb = asksaveasfilename(initialfile='untitled.txt', defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
            if self.fileb == "":
                self.fileb = None
            else:
                with open(self.fileb, "w") as file:
                    file.write(self.text.get(1.0, END))
                self.root.title(os.path.basename(self.fileb) + " - Notepad")
        else:
            with open(self.fileb, "w") as file:
                file.write(self.text.get(1.0, END))

    def cut(self):
        self.text.event_generate("<<Cut>>")

    def copy(self):
        self.text.event_generate("<<Copy>>")

    def paste(self):
        self.text.event_generate("<<Paste>>")

    def run(self):
        self.root.mainloop()

note = Notepad(width=600, height=600)
note.run()
