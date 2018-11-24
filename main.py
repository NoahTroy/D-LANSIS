#Distributed Local Area Network Sign In System a.k.a. D-Lansis
#Created by Noah Troy on September 5, 2018
#Last Updated by Noah Troy on October 2, 2018
#V1.0.0
#main.py

#Import all of the necessary libraries:
#Import system functionality, to allow easy, built-in sftp file transfer:
import subprocess

#Import threading to allow multiprocessing:
import threading

#Import functions stored as separate files:
import mainWindow , init

#Import any other necessary non-specific modules:
import time , pickle , os , encryption



#Upon boot, make sure all of the necessary information is present, and ask for it if it isn't:
localPass = init.startupCheck()
#Load the deviceID, in order to access the home directory:
with open('deviceID' , 'r') as deviceIDFile:
	deviceID = deviceIDFile.read()

#Start the main loop that runs the GUI infinitely:
while (True):
	mainWindow.startWindow(localPass)

	#Only allow the code to proceed if there is a favorable exit status:
	if (not(os.path.isfile('Temp/mainWindowExitStatus.dat'))):
		continue
	else:
		mainWindowExitStatus = encryption.decrypt(localPass , 'Temp/mainWindowExitStatus.dat' , True)
		mainWindowExitStatus[0] = bool(mainWindowExitStatus[0])

		if (not(mainWindowExitStatus[0])):
			continue

	#Load the GUI allowing the user to select their action and destination:
