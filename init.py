#Distributed Local Area Network Sign In System a.k.a. D-Lansis
#Last Updated by Noah Troy on October 8, 2018
#V1.0.0
#init.py

#Import tkinter to create the GUI:
from tkinter import *
#For creating message boxes:
import tkinter.messagebox as popup

#Import any other necessary, non-specific modules:
import os , passwordPrompt , subprocess , time , encryption


#Define a function to automatically check for the presence of all of the necessary files and information for proper execution, and gather that information if it is not present. In the end, return the local password, so that it may be stored as a global variable.
def startupCheck():
	#Check to make sure all of the necessary directories exist, and create them if they don't:
	if (not(os.path.exists('Logs'))):
		os.mkdir('Logs')

	if (not(os.path.exists('Settings'))):
		os.mkdir('Settings')

	if (not(os.path.exists('Input'))):
		os.mkdir('Input')

	if (not(os.path.exists('Passwords'))):
		os.mkdir('Passwords')

	if (not(os.path.exists('Certs'))):
		os.mkdir('Certs')

	if (not(os.path.exists('Temp'))):
		os.mkdir('Temp')

	if (not(os.path.isfile('deviceID'))):
		with open('deviceID' , 'w') as deviceIDFile:
			deviceIDFile.write(encryption.netIDGen())

	if (not(os.path.isfile('netID'))):
		popup.showerror('Error: No Network ID' , 'We\'re sorry, but no network I.D. file was found on this device. Please contact the I.T. Department, and instruct them to generate a new device setup for you. As is, this device is currently unusable. The device will shutdown once you click okay.')
		#####################UN-COMMENT THIS LINE WHEN TESTING IS DONE###################subprocess.call('sudo shutdown now' , shell = True)
		exit()

	#Load the deviceID, in order to access the home directory:
	with open('deviceID' , 'r') as deviceIDFile:
		deviceID = deviceIDFile.read()

	#Check to make sure that a password has been successfully set, and ask to verify it (in order to save it in memory). If it doesn't exist, then prompt to create one:
	if (not(os.path.isfile('Passwords/' + deviceID + '/hash.sha256'))):
		passwordPrompt.prompt(1)
		popup.showerror('System Reboot Needed!' , 'Thank you for setting a password! The system must now reboot, so that it may start up in a secured mode, using your new password.\n\nThis will happen automatically.')
		time.sleep(10)
		###########UN-COMMENT THIS ONCE TESTING IS DONE!################subprocess.call('sudo reboot' , shell = True)
		exit()
	else:
		return passwordPrompt.prompt(2)
		
		
