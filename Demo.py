from guizero import *
import os
from glob import glob
from pathlib import Path
import shutil

pathUSBDrive = "/media/pi/"
pathPhone = "/run/user/1000/gvfs/"
uploadFolder = "/Internal shared storage/APKUpdaterFolder/"
connectedPhoneDir = ""
selectedFile = ""

def setFileNameLabel():
    fileNameLabel.value = "Changed!"

def setPhoneNameLabel():
    global connectedPhoneDir
    phoneList = glob(pathPhone + "*")
    if phoneList:
        connectedPhoneDir = phoneList[0]
        phoneNameLabel.value = phoneList[0].replace(pathPhone,"").replace("mtp:host=","")[:20] + "..."
    else:
        phoneNameLabel.value = "ERROR"
        statusLabel.value = "Current Status: Error \n Failed to locate a connected device."
    
def openUsbWidow():
    count = 0
    for path in Path('/media/pi').rglob('*.apk'):
        apkFullPathList[os.path.basename(path)] = path
        apkFileList.insert(count,os.path.basename(path))
        count = count + 1
    usbWindow.show(wait=True)

   
def testListSelection(value):
    global selectedFile
    selectedFile = apkFullPathList[value]
    fileNameLabel.value = "File to upload: " + value
    
def startUploadProcess():
    global selectedFile
    if connectedPhoneDir == "":
        statusLabel.value = "Current Status: ERROR \n Please connect a phone first!"
        return
    
    if not os.path.exists(connectedPhoneDir + uploadFolder):
        os.mkdir(connectedPhoneDir + uploadFolder)
        
    if selectedFile == "":
        statusLabel.value = "Current Status: ERROR \n Failed to locate the APK file from USB drive!"
        
    print("Source: " + str(selectedFile) + " Dest: " + connectedPhoneDir + uploadFolder + str(os.path.basename(selectedFile))) 
    shutil.copyfile(str(selectedFile),connectedPhoneDir + uploadFolder + str(os.path.basename(selectedFile)))
    
    print("adb install " + "'" + connectedPhoneDir + uploadFolder + str(os.path.basename(selectedFile)) + "'")
    os.system("adb install " + "'" + connectedPhoneDir + uploadFolder + str(os.path.basename(selectedFile)) + "'")

    


app = App(layout="grid",title="Android updater")
buttonHeight = 1


usbWindow = Window(app)
usbWindow.hide()
apkFileList = ListBox(usbWindow,command=testListSelection,items=[])
apkFullPathList = {}

#First row
fileNameLabel = Text(app,text="File to upload: ", grid=[0,0],align="left")
usbButton = PushButton(app, command=openUsbWidow,width=10,height=buttonHeight, text="USB drive", grid=[1,0])
piButton = PushButton(app, command=setFileNameLabel,width=10,height=buttonHeight, text="Pi", grid=[2,0])

#Second row
phoneNameLabel = Text(app,text="Phone to update: ", grid=[0,1],align="left")
phoneButton = PushButton(app, command=setPhoneNameLabel,width=10,height=buttonHeight, text="Detect phone", grid=[1,1])

#Third row
startButton = PushButton(app, command=startUploadProcess,width=10,height=buttonHeight, text="Start upload!", grid=[1,2])

#Fourth row
progressLabel = Text(app,text="Current progress: 0%", grid=[0,3],align="left")

#Fifth row 
statusLabel = Text(app,text="Current status: OK", grid=[0,4],align="left")

app.display()




