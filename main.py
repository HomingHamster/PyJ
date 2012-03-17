from Tkinter import *

class GUI(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.createMainWindow()
        self.config(menu=self.menuBar())
    def createMainWindow(self):
        mainFrame = Frame(self)
        buttonFrame = self.createButtonFrame(mainFrame)
        buttonFrame.pack(side=LEFT, fill=Y)
        mainCanvas = Canvas(self)
        mainCanvas.config(bg='gray')
        mainCanvas.pack(side=RIGHT, fill=BOTH, expand=1)
        mainFrame.pack(fill=BOTH, expand=1)
    def createButtonFrame(self, parent):
        buttonFrame = Frame(parent)
        newClassButton = Button(buttonFrame, text="New Class")
        newClassButton.pack(fill=X)
        newRelButton = Button(buttonFrame, text="New Relationship")
        newRelButton.pack(fill=X)
        clearCanvasButton = Button(buttonFrame, text="Clear Canvas")
        clearCanvasButton.pack(fill=X)
        generateJavaCodeButton = Button(buttonFrame, text="Generate Java Code")
        generateJavaCodeButton.pack(fill=X)
        editLinkButton = Button(buttonFrame, text="Edit/Delete a Relationship")
        editLinkButton.pack(fill=X)
        editClassButton = Button(buttonFrame, text="Edit/Delete a Class")
        editClassButton.pack(fill=X)
        return buttonFrame
        
    def menuBar(self):
        menubar = Menu(self)
        
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=self.quit)
        filemenu.add_command(label="Save", command=self.save)
        filemenu.add_command(label="open", command=self.open)
        
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.undo)
        editmenu.add_command(label="redo", command=self.redo)
        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label="Edit", menu=editmenu)
        return menubar
        
    def save(self):
        pass
        
    def open(self):
        pass
        
    def undo(self):
        pass
        
    def redo(self):
        pass

if __name__=='__main__':
    app = GUI()
    app.mainloop()
