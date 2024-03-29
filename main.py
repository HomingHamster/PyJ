#!/usr/bin/env python
#PyJ authors Andy Cooper and Felix Farquharson
import re
from Tkinter import *

class GUI(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("%dx%d+100+100" % (self.winfo_screenwidth()-350, self.winfo_screenheight()-450))
        self.minsize(600, 300)
        self.createMainWindow()
        self.title("PyJ")
        self.config(menu=self.menuBar())
    def createMainWindow(self):
        mainFrame = Frame(self)
        buttonFrame = self.createButtonFrame(mainFrame)
        buttonFrame.pack(side=LEFT, fill=Y)
        self.mainCanvas = CanvasArea(self)
        self.mainCanvas.pack(side=RIGHT, fill=BOTH, expand=1)
        mainFrame.pack(fill=BOTH, expand=1)   
        
   
    def fullScreen(self):
        self.geometry("%dx%d+0+0" % (self.winfo_screenwidth(), self.winfo_screenheight()))    
        self.overrideredirect(1)
        
    def exitFullScreen(self):
        self.geometry("%dx%d+0+0" % (self.winfo_screenwidth()-50, self.winfo_screenheight()-150))
        self.overrideredirect(0)    
   
    def clearCanvas(self):
        self.mainCanvas.clear()
        self.mainCanvas.classList=[]    
    def newClass(self):
        self.mainCanvas.newClass()
        self.mainCanvas.redraw()
    
    def createButtonFrame(self, parent):
        buttonFrame = Frame(parent)
        newClassButton = Button(buttonFrame, text="New Class", command=self.newClass)
        newClassButton.pack(fill=X)
        newRelButton = Button(buttonFrame, text="New Relationship")
        newRelButton.pack(fill=X)
        clearCanvasButton = Button(buttonFrame, text="Clear Canvas", 
                command=self.clearCanvas)
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
       
        windowmenu = Menu(menubar, tearoff=0)
        windowmenu.add_command(label="Fullscreen", command=self.fullScreen)
        windowmenu.add_command(label="Exit Fullscreen", command=self.exitFullScreen)
                                
        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label="Edit", menu=editmenu)
        menubar.add_cascade(label="Window", menu=windowmenu)
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
        Canvas.__init__(self)
        #migtht have to use double click to add properties and edit links etc.
        self.bind("<B1-Motion>", self.mouseMoved)
        self.bind("<Button-1>", self.mousePressed)
        #self.bind("<Double-Button-1>", self.mouseDoubleClicked)
        self.bind("<ButtonRelease-1>", self.mouseUp)
        self.parent = parent
        self.config(bg="gray")
        self.classList=[]
        self.offsetx=0
        self.offsety=0
        self.dragObj = None
        self.dragging = False
    def redraw(self):
        self.clear()
        self.drawClasses()
    def newClass(self):
        self.classList += [DragAndDropClassObject()]
    def drawClasses(self):
        for ddclass in self.classList:
            ddclass.draw(self)
    #def mouseDoubleClicked(self, event):
        #print "clicked"
    def mousePressed(self, event):
        if self.dragging==False:
            for ddClassObj in self.classList:
                rect = (ddClassObj.position())
                if (rect[0] <= event.x <= rect[2]) and \
                        (rect[1] <= event.y <= rect[3]):
                    
                    self.offsetx = event.x - rect[0]
                    self.offsety = event.y - rect[1]
                    x=event.x - self.offsetx
                    y=event.y - self.offsety
                    self.dragObj = self.findNearestClass(x,y)
                    self.dragging = True
                    
    def mouseMoved(self, event):
        if self.dragging:
            x= event.x - self.offsetx
            y= event.y - self.offsety
            self.dragObj.x = x
            self.dragObj.y = y
        self.redraw()
    def mouseUp(self, event):
        print self.dragObj
        self.dragging=False
        self.dragObj = None
        self.offsetx = None
        self.offsety = None
        
    def findNearestClass(self, x, y):
        minDist = 9999999
        minObj = None
        for component in self.classList:
            if component.distanceTo(x,y) < minDist:
                minDist = component.distanceTo(x,y)
                minObj = component
        if (minObj != None) and (minDist < 50) :
            return minObj
        return None
            
    def clear(self):
        self.delete("all")
        
        
class DragAndDropClassObject:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.classObject = ClassObject()
        self.spareCanvas = Canvas()
    def position(self):
        height = 20
        x = 0
        for string in ([self.classObject.name]+self.classObject.attributes+\
                        self.classObject.methods):
            if x < self.getSize(string)[0]:
                x = self.getSize(string)[0]
            height += 20
        if height < 60:
            height = 60
        return self.x, self.y, self.x+x+20, self.y+height
    def getSize(self, string):
        string = self.spareCanvas.create_text(0,0,text=string)
        bbox = self.spareCanvas.bbox(string)
        return (bbox[2]-bbox[0], bbox[3]-bbox[1])
    def draw(self, parent):
        parent.create_rectangle(self.position(), 
                outline='black', fill='white')
    def distanceTo(self, x, y):
        return (abs(self.x-x))+(abs(self.y-y))
        
class Undo:
    def __init__(self):
        self.actionList = []
        self.currentPosition = 0
    def undo(self):
        pass
    def redo(self):
        pass
    def onAction(self, action):
        pass
        
class ClassObject:
    def __init__(self):
        self.name=""
        self.links = []
        self.attributes = []
        self.methods = []
        
class Link:
    def __init__(self):
        pass

class Generator:
    def __init__(self):
        self.attributePattern = \
            "^([+\- ]|)\s{0,1}([a-z][a-zA-Z_]+):\s{0,1}([a-zA-Z_]+)$"
        self.methodPattern = \
            "^([+\- ]|)\s{0,1}([a-z][a-zA-Z_]+)\s{0,1}\(\
            (?:\s{0,1}([a-z][a-zA-Z]+)\s{0,1}:\s{0,1}([a-zA-Z_]+)\
            \s{0,1}(?:\s{0,1},|)|)+\)\s{0,1}:\s{0,1}([a-zA-Z_]+)$"
    def generateCode(self, classList):
        for classObj in classList:
            pass

if __name__=='__main__':
    app = GUI()
    app.mainloop()
