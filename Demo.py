from guizero import *

def setFileNameLabel():
    fileNameLabel.value = "Changed!"

def setPhoneNameLabel():
    phoneNameLabel.value = "Changed phone!"
    
def openUsbWidow():
    usbWindow.show(wait = True)

app = App(layout="grid",title="Android updater")
buttonHeight = 1

usbWindow = Window(app)
usbWindow.hide()
#First row
fileNameLabel = Text(app,text="File to upload: ", grid=[0,0],align="left")
usbButton = PushButton(app, command=openUsbWidow,width=10,height=buttonHeight, text="USB drive", grid=[1,0])
piButton = PushButton(app, command=setFileNameLabel,width=10,height=buttonHeight, text="Pi", grid=[2,0])

#Second row
phoneNameLabel = Text(app,text="Phone to update: ", grid=[0,1],align="left")
phoneButton = PushButton(app, command=setFileNameLabel,width=10,height=buttonHeight, text="Detect phone", grid=[1,1])

#Third row
startButton = PushButton(app, command=setFileNameLabel,width=10,height=buttonHeight, text="Start upload!", grid=[1,2])

#Fourth row
progressLabel = Text(app,text="Current progress: 0%", grid=[0,3],align="left")

#Fifth row
statusLabel = Text(app,text="Current status: OK", grid=[0,4],align="left")

app.display()




