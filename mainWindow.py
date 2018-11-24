#Distributed Local Area Network Sign In System a.k.a. D-Lansis
#Last Updated by Noah Troy on October 2, 2018
#V1.0.0
#mainWindow.py

#Import tkinter to create the GUI:
from tkinter import *
#For creating message boxes:
import tkinter.messagebox as popup

#Import any other necessary, non-specific modules:
import pickle , os , encryption


#Declare all of the global variables:
firstRun = True
password = ''

#Store the deviceID as a global variable, so that system information may be easily accessed:
with open('deviceID' , 'r') as deviceIDFile:
	deviceID = deviceIDFile.read()

#KEY: windowAttsList = [window title , window resolution , make window fullscreen , remove toolbar , stop alt + f4 from working , window background color , main heading text , main heading background color , main heading foreground color , main heading typeface , main heading font size , id prompt text , id prompt background color , id prompt foreground color , id prompt typeface , id prompt font size , entry box input length , entry box typeface entry box font size , entry box background color , entry box foreground color , hide entry , allow changing input hiding setting , button background color , button foreground color , button active background color , button active foreground color]
#Default Values:
windowAttsList = ['Sign In' , '1080x720' , False , False , False , '#000000' , 'Classroom Sign In' , '#000000' , '#FF5000' , 'Times New Roman' , 70 , 'Please Enter Your Student I.D. Below:' , '#000000' , '#FFFFFF' , 'Times New Roman' , 25 , 4 , 'Times New Roman' , 250 , '#FFFFFF' , '#000000' , True , True , '#0061FF' , '#FFFFFF' , '#FF5000' , '#000000']


#Updates all of the design variables for the window:
def updateWindowAtts(save = False , newAttsToSave = []):
	global windowAttsList

	if (save):
		encryption.encrypt(newAttsToSave , password , 'Settings/' + deviceID + '/' , 'mainWindowAtts.dat')
		return

	if (not(os.path.isfile('Settings/' + deviceID + '/mainWindowAtts.dat'))):
		encryption.encrypt(windowAttsList , password , 'Settings/' + deviceID + '/' , 'mainWindowAtts.dat')

	windowAttsList = encryption.decrypt(password , 'Settings/' + deviceID + '/mainWindowAtts.dat' , True)


#Define a function to enable/disable the private mode feature, that obscures the input:
def enablePrivateMode(box):
	if (windowAttsList[21]):
		box.configure(show = '')
	else:
		box.configure(show = '*')


#Define a function designed to no† react/do anything when called:
def passRequest():
	pass


#Define a function to be called once the enter key is pressed:
def enterPressed(enteredData , window):
	if (os.path.isfile('Temp/mainWindowExitStatus.dat')):
		os.remove('Temp/mainWindowExitStatus.dat')

	try:
		enteredData = int(enteredData)
	except:
		popup.showerror('Invalid Input' , 'Error\nThe Input You Have Entered Is Not Valid.\nPlease Make Sure You Are Entering Only Integers.')
		encryption.encrypt([False] , password , 'Temp/' , 'mainWindowExitStatus.dat')
		window.destroy()
		return

	if (len(str(enteredData)) != (windowAttsList[16])):
		popup.showerror('Invalid Input' , 'Error\nThe Input You Have Entered Is Not Valid.\nPlease Make Sure The Length Of Your Input Is ' + str(windowAttsList[16]) + ' Integers.')
		encryption.encrypt([False] , password , 'Temp/' , 'mainWindowExitStatus.dat')
		window.destroy()
		return

	encryption.encrypt([True , enteredData] , password , 'Temp/' , 'mainWindowExitStatus.dat')
	window.destroy()


#Creates and launches the GUI:
def startWindow(encryptPass):
	#Make the password a global variable:
	global password
	password = encryptPass

	#If this is the first run, force an attributes check and update:
	global firstRun
	if (firstRun):
		updateWindowAtts()
		firstRun = False

	#Create the GUI window object:
	window = Tk()

	#Title the window:
	window.title(windowAttsList[0])

	#Determine the specific size of the window:
	window.geometry(windowAttsList[1])

	#Make the window fullscreen:
	if (windowAttsList[2]):
		window.attributes('-fullscreen', True)

	#Disable/Remove the toolbar, allowing for window closing, resizing, minimizing, etc.:
	if (windowAttsList[3]):
		window.overrideredirect(True)

	#Stop alt + f4 from working to close the window:
	if (windowAttsList[4]):
		window.protocol('WM_DELETE_WINDOW', passRequest)

	#Set the window background color:
	window.configure(bg = windowAttsList[5])

	#Create and pack a heading to display the title of the program:
	heading1 = Label(window , text = windowAttsList[6] , bg = windowAttsList[7] , fg = windowAttsList[8] , font = (windowAttsList[9] , windowAttsList[10]))
	heading1.pack(side = 'top' , pady = 10)

	#Add a text label asking for input:
	enterIDLabel = Label(window , text = windowAttsList[11] , bg = windowAttsList[12] , fg = windowAttsList[13] , font = (windowAttsList[14] , windowAttsList[15]))
	enterIDLabel.pack(side = 'top' , pady = 10)

	#Add an input box to enter the student I.D. number into:
	studentIDBox = Entry(window , width = windowAttsList[16] , font = (windowAttsList[17] , windowAttsList[18]) , bg = windowAttsList[19] , fg = windowAttsList[20])
	if (windowAttsList[21]):
		studentIDBox.configure(show = '*')
	else:
		studentIDBox.configure(show = '')
	studentIDBox.pack(side = 'top' , pady = 125)
	#Make the box automatically selected, and ready for text entry:
	studentIDBox.focus_set()

	#Add a button allowing for switching in and out of private mode:
	if (windowAttsList[22]):
		if (windowAttsList[21]):
			privateModeButtonText = 'Show Input'
		else:
			privateModeButtonText = 'Hide Input'

		privateModeButton = Button(window , text = privateModeButtonText , bd = 0 , bg = windowAttsList[23] , fg = windowAttsList[24] , activebackground = windowAttsList[25] , activeforeground = windowAttsList[26] , command = lambda: enablePrivateMode(studentIDBox))
		privateModeButton.place(x = 0 , y = 0)

	#Bind the return key, so that when it is pressed, the appropriate function will be called:
	window.bind('<Return>' , lambda x: enterPressed(studentIDBox.get() , window))
	window.bind('<KP_Enter>' , lambda x: enterPressed(studentIDBox.get() , window))



	#Run the event listener main window loop:
	window.mainloop()
