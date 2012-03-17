from Tkinter import *

class GUI(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.createMainWindow()
    def createMainWindow(self):
        mainFrame = Frame(self)
        buttonFrame = self.createButtonFrame(mainFrame)
        buttonFrame.pack(side=LEFT, fill=Y)
        mainCanvas = Canvas(self)
        mainCanvas.pack(side=RIGHT, fill=BOTH, expand=1)
        mainFrame.pack(fill=BOTH, expand=1)
    def createButtonFrame(self, parent):
        buttonFrame = Frame(parent)
        newClassButton = Button(buttonFrame, text="New Class")
        newClassButton.pack(fill=X)
	newRelButton = Button(buttonFrame, text="New Relationship")
	newRelButton.pack()
	clearCanvasButton = Button(buttonFrame, text="Clear Canvas")
	clearCanvasButton.pack()
	generateJavaCodeButton = Button(buttonFrame, text="Generate Java Code")
	generateJavaCodeButton.pack()
	editLinkButton = Button(buttonFrame, text="Edit/Delete a Relationship")
	editLinkButton.pack()
	editClassButton = Button(buttonFrame, text="Edit/Delete a Class")
	editClassButton.pack()
        return buttonFrame

if __name__=='__main__':
    app = GUI()
    app.mainloop()
