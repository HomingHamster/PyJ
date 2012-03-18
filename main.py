#!/usr/bin/env python
#PyJ authors Andy Cooper and Felix Farquharson
import re
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
        self.mainCanvas = CanvasArea(self)
        self.mainCanvas.pack(side=RIGHT, fill=BOTH, expand=1)
        mainFrame.pack(fill=BOTH, expand=1)
        
   
    def clearCanvas(self):
        self.mainCanvas.clear()    
        
    def drawRectangle(self):
        self.mainCanvas.create_rectangle(205,10,300,105, outline='black', fill='white')
                    
    def createButtonFrame(self, parent):
        buttonFrame = Frame(parent)
        newClassButton = Button(buttonFrame, text="New Class", command=self.drawRectangle)
        newClassButton.pack(fill=X)
        newRelButton = Button(buttonFrame, text="New Relationship")
        newRelButton.pack(fill=X)
        clearCanvasButton = Button(buttonFrame, text="Clear Canvas", command=self.clearCanvas)
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
        filemenu.add_command(label="Save", command=self.save)
        filemenu.add_command(label="open", command=self.open)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        
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

class CanvasArea(Canvas):
    def __init__(self, parent):
        Canvas.__init__(parent)
        self.config(bg="gray")
    def drawClasses(self, listDDClasses):
        for ddclass in listDDClasses:
            ddclass.draw()
    
    def clear(self):
        self.delete("all")
        
        
class DragAndDropClass:
    def __init__(self):
        self.x = 10
        self.y = 10
    def draw(self):
        pass

class ClassObject:
    def __init__(self, name):
        self.name=name
        self.links = [] #so we can use list.set later.

class Generator:
    def __init__(self):
        self.attributePattern = \
            "^([+\- ]|)\s{0,1}([a-z][a-zA-Z_]+):\s{0,1}([a-zA-Z_]+)$"
        self.methodPattern = \
            "^([+\- ]|)\s{0,1}([a-z][a-zA-Z_]+)\s{0,1}\(\
            (?:\s{0,1}([a-z][a-zA-Z]+)\s{0,1}:\s{0,1}([a-zA-Z_]+)\
            \s{0,1}(?:\s{0,1},|)|)+\)\s{0,1}:\s{0,1}([a-zA-Z_]+)$"
    def generateCode(self, classList):
        for class in classList:
            pass

if __name__=='__main__':
    app = GUI()
    app.mainloop()
