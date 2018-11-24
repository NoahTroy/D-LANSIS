#Distributed Local Area Network Sign In System a.k.a. D-Lansis
#Last Updated by Noah Troy on October 8, 2018
#V1.0.0
#passwordPrompt.py

#Import tkinter to create the GUI:
from tkinter import *
#For creating message boxes:
import tkinter.messagebox as popup

#Import the encryption file for dealing with passwords upon initialization:
import encryption


#Declare the necessary global variables:
returnPassword = False
password = ''


#Define a function to verify that entered passwords are the same and valid, and then execute the correct steps, depending on the results:
def newPassVerification(pass1 , pass2 , passbox1 , passbox2 , window):
	pass1 = str(pass1)
	pass2 = str(pass2)
	if (pass1 == pass2):
		#Check to make sure the password meets the minimum requirements (at least 12 characters long, includes at least one captital and one lowercase letter, at least one number, and at least two different special characters):
		if (len(pass1) < 12):
			popup.showerror('Password Verification' , 'Error\nYour Password Is Less Than 12 Characters In Length.\nPlease Make Sure To Create A Strong Password, As It Is The Only Defense Between The Outside World, And Private Student Data.')
			passbox1.delete(0 , 'end')
			passbox2.delete(0 , 'end')
			return
		else:
			capitalLetters = ['A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z']
			hasCapLet = False
			for letter in capitalLetters:
				if (letter in pass1):
					hasCapLet = True
					break

			if not(hasCapLet):
				popup.showerror('Password Verification' , 'Error\nYour Password Does Not Contain A Capital Letter.\nPlease Make Sure To Create A Strong Password, As It Is The Only Defense Between The Outside World, And Private Student Data.')
				passbox1.delete(0 , 'end')
				passbox2.delete(0 , 'end')
				return

			lowercaseLetters = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z']
			hasLowercaseLet = False
			for letter in lowercaseLetters:
				if (letter in pass1):
					hasLowercaseLet = True
					break

			if not(hasLowercaseLet):
				popup.showerror('Password Verification' , 'Error\nYour Password Does Not Contain A Lowercase Letter.\nPlease Make Sure To Create A Strong Password, As It Is The Only Defense Between The Outside World, And Private Student Data.')
				passbox1.delete(0 , 'end')
				passbox2.delete(0 , 'end')
				return

			numbers = ['1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '0']
			hasNumber = False
			for num in numbers:
				if (num in pass1):
					hasNumber = True
					break

			if not(hasNumber):
				popup.showerror('Password Verification' , 'Error\nYour Password Does Not Contain A Number.\nPlease Make Sure To Create A Strong Password, As It Is The Only Defense Between The Outside World, And Private Student Data.')
				passbox1.delete(0 , 'end')
				passbox2.delete(0 , 'end')
				return

			symbols = ['~' , '`' , '!' , '@' , '#' , '$' , '%' , '^' , '&' , '*' , '(' , ')' , '-' , '_' , '+' , '=' , '[' , ']' , '{' , '}' , '\\' , '|' , '\'' , '"' , ':' , ';' , '/' , '?' , '<' , '>' , ',' , '.']
			hasSymbol = False
			hasSecondSymbol = False
			hasUniqueSymbols = False
			usedSymbols = []
			for sym in symbols:
				if (sym in pass1):
					if (hasSymbol):
						hasSecondSymbol = True
					else:
						hasSymbol = True
					usedSymbols.append(sym)

			if (hasSecondSymbol):
				for includedSymbol in usedSymbols:
					if (includedSymbol != usedSymbols[0]):
						hasUniqueSymbols = True
						break

			if not((hasSymbol & hasSecondSymbol) & hasUniqueSymbols):
				popup.showerror('Password Verification' , 'Error\nYour Password Does Not Contain At Least Two Unique Symbols.\nPlease Make Sure To Create A Strong Password, As It Is The Only Defense Between The Outside World, And Private Student Data.')
				passbox1.delete(0 , 'end')
				passbox2.delete(0 , 'end')
				return

			#Now save the hash of the password, and destroy the window:
			encryption.savePasswordHash(pass1)
			window.destroy()
	else:
		popup.showerror('Password Verification' , 'Error\nThe Two Passwords You Entered Do Not Match!\nPlease Enter The Same Password Twice!\nThanks!')
		passbox1.delete(0 , 'end')
		passbox2.delete(0 , 'end')
		return


#Define a function to verify an entered password against the stored hash, and then if correct, return the password:
def oldPassVerification(pass1 , passBox , window):
	if (encryption.verifyHash(pass1 , 'None' , True)):
		global returnPassword
		global password
		returnPassword = True
		password = pass1
		popup.showerror('Success!' , 'Thank You!\nYour password has been successfully verified!')
		window.destroy()
	else:
		popup.showerror('Verification Failed!' , 'We\'re sorry, but the password you entered does not match the hash we have stored in our database. Please make sure you are entering the right password, and try again.')
		passBox.delete(0 , 'end')


#Create a function to prompt for a password (for creation, verification, or replacement):
def prompt(promptType):
	#Create the GUI window object:
	window = Tk()

	#Set all of the window attributes:

	#Determine the specific size of the window:
	window.geometry('600x350')

	#Set the window background color:
	window.configure(bg = '#FFFFFF')

	if (promptType == 1):
		window.title('Create a Password')

		heading = Label(window , text = 'Please Create a New Password' , bg = '#FFFFFF' , fg = '#000000' , font = ('Times New Roman' , 22))
		heading.place(x = 120 , y = 25)

		enterPassLabel = Label(window , text = 'Please Enter Your New Password in the Box Below:' , bg = '#FFFFFF' , fg = '#000000' , font = ('Times New Roman' , 14))
		enterPassLabel.place(x = 105 , y = 100)

		passBox1 = Entry(window , width = 50 , font = ('Times New Roman' , 14) , bg = '#FFFFFF' , fg = '#000000' , show = '*')
		passBox1.place(x = 70 , y = 135)

		verifyPassLabel = Label(window , text = 'Please Re-Type Your Password:' , bg = '#FFFFFF' , fg = '#000000' , font = ('Times New Roman' , 14))
		verifyPassLabel.place(x = 178 , y = 175)

		passBox2 = Entry(window , width = 50 , font = ('Times New Roman' , 14) , bg = '#FFFFFF' , fg = '#000000' , show = '*')
		passBox2.place(x = 70 , y = 205)

		submitButton = Button(window , text = 'Set Password' , bd = 0 , bg = '#FFFFFF' , fg = '#000000' , activebackground = '#CCCDCE' , activeforeground = '#000000' , command = lambda: newPassVerification(passBox1.get() , passBox2.get() , passBox1 , passBox2 , window))
		submitButton.place(x = 235 , y = 280)
	elif (promptType == 2):
		window.title('Verify Your Password')

		heading = Label(window , text = 'Please Verify Your Current Password,\nBy Entering It In The Box Below:' , bg = '#FFFFFF' , fg = '#000000' , font = ('Times New Roman' , 18))
		heading.pack(side = 'top' , pady = 10)

		passBox1 = Entry(window , width = 50 , font = ('Times New Roman' , 14) , bg = '#FFFFFF' , fg = '#000000' , show = '*')
		passBox1.place(x = 70 , y = 135)

		submitButton = Button(window , text = 'Verify Password' , bd = 0 , bg = '#FFFFFF' , fg = '#000000' , activebackground = '#CCCDCE' , activeforeground = '#000000' , command = lambda: oldPassVerification(passBox1.get() , passBox1 , window))
		submitButton.place(x = 235 , y = 250)
	elif (promptType == 3):
		pass
		####################################CODE THIS SECTION LATER, AS IT WILL INVOLVE HAVING TO RE-ENCRYPT ALL FILES######################################
	else:
		popup.showerror('Coding Error!' , 'Error\nIf you are seeing this message, a runtime error has ocurred!\nThat means that you did something the code was not expecting, or prepared for!\nYour best bet is to restart the computer, and hopefully you\'ll never see this again!\nSorry!')


	#Run the event listener main window loop:
	window.mainloop()
	if (returnPassword):
		return password



