#Distributed Local Area Network Sign In System a.k.a. D-Lansis
#Last Updated by Noah Troy on October 2, 2018
#V1.0.0
#encryption.py

#Import the necessary security-related libraries:
#Use fernet instead of hazmat, to maintain the best security possible:
from cryptography.fernet import Fernet
import rsa
from passlib.hash import sha256_crypt
import base64

#Import any other necessary modules:
import pickle , time , os

#Store the deviceID as a global variable, so that system information may be easily accessed:
with open('deviceID' , 'r') as deviceIDFile:
	deviceID = deviceIDFile.read()

#Define a function to encrypt desired files with the given password, in a secure manner:
def encrypt(data , password , fileLocation , filename):
	data = str(data)

	#Turn the password into 32 url-safe base64-encoded bytes:
	if (len(password) > 32):
		password = password[0:32]
		key = base64.urlsafe_b64encode(str.encode(password))

	elif (len(password) < 32):
		newPass = ''
		for i in range(0 , 32):
			if (i < len(password)):
				newPass += password[i]
			else:
				#Risk taking the literal "l" for having a weak password:
				newPass += 'l'

		password = newPass
		key = base64.urlsafe_b64encode(str.encode(password))

	else:
		key = base64.urlsafe_b64encode(str.encode(password))


	#Encrypt the data:
	cipher_suite = Fernet(key)

	encryptedData = cipher_suite.encrypt(str.encode(data))


	#Check to make sure the directory exists, and create it if not:
	if (not(os.path.exists(fileLocation))):
		os.mkdir(fileLocation)

	#Save the data:
	with open(fileLocation + filename , 'wb') as encryptedFile:
		pickle.dump(encryptedData , encryptedFile)

	#Update the last-updated file:
	with open(fileLocation + filename + '.lastUpdated' , 'w') as lastUpdatedFile:
		lastUpdatedFile.write(str(time.time()))


#Define a function to decrypt desired files with the given password, in a secure manner:
#Note: if you wish a list returned without error, then the data to be decrypted must NOT contain any commas (other than those used to separate list items) or single or double quotes (except for those automatically added to designate a string object), or the string values "True" or "False" (unless you wish them to be automatically converted into boolean):
def decrypt(password , fileLocation , returnList = False):
	#Turn the password into 32 url-safe base64-encoded bytes:
	if (len(password) > 32):
		password = password[0:32]
		key = base64.urlsafe_b64encode(str.encode(password))

	elif (len(password) < 32):
		newPass = ''
		for i in range(0 , 32):
			if (i < len(password)):
				newPass += password[i]
			else:
				#Risk taking the literal "l" for having a weak password:
				newPass += 'l'

		password = newPass
		key = base64.urlsafe_b64encode(str.encode(password))

	else:
		key = base64.urlsafe_b64encode(str.encode(password))


	#Decrypt the data:
	cipher_suite = Fernet(key)

	with open(fileLocation , 'rb') as encryptedFile:
		encryptedData = pickle.load(encryptedFile)

	decryptedData = cipher_suite.decrypt(encryptedData)

	if (returnList):
		decryptedData = decryptedData.decode('utf-8')
		decryptedData = decryptedData[1:(len(decryptedData))]
		listToReturn = []

		currentItem = ''
		skipSpace = False
		skipQuotes = False
		counter = 0

		for item in decryptedData:
			counter += 1

			if ((item == '\'') or (item == '"')):
				skipQuotes = True

			if (skipSpace):
				skipSpace = False
				continue

			if (skipQuotes):
				skipQuotes = False
				continue

			if ((item == ',') or (counter >= len(decryptedData))):
				works = True
				try:
					currentItemInt = int(currentItem)
				except:
					works = False
					if (currentItem == 'True'):
						currentItem = True
					if (currentItem == 'False'):
						currentItem = False
				if (works):
					currentItem = int(currentItem)
				listToReturn.append(currentItem)
				currentItem = ''
				skipSpace = True
				continue

			currentItem += item

		return listToReturn
			

	else:
		return decryptedData.decode('utf-8')


#Define a function to generate a random encryption key, and symmetrically encrypt data with that key, then asymmetrically encrypt the decryption key with the given public key, and save both of the newly encrypted files:
#Note, the public_key expects raw data input; i.e. the result of pemFile.read() (in other words, the input has to be in bytes!)
def transfer(data , fileLocation , public_key):
	#Generate a random, compatible key:
	symmetricKey = Fernet.generate_key()

	#Encrypt the data:
	encrypt(data , symmetricKey , filename)


	#Load the public key under the Public Key Cryptography Standards #1:
	pubKey = rsa.PrivateKey.load_pkcs1(public_key)

	#Encrypt the random symmetricKey with the given public key:
	encryptedKey = rsa.encrypt(symmetricKey , pubKey)

	#Save the file with the ecryptedKey:
	with open(fileLocation + '.key' , 'wb') as encryptedFile:
		encryptedFile.write(encryptedKey)


#Define a function to decrypt a symmetric key located in a file, with our private key, then decrypt the symmetrically encrypted second file with the newly-recovered key:
def receive(filename , privKeyFile):
	pass


#Define a function to verify a sha256 hash:
def verifyHash(stringToVerify , knownHash , fetchFromDefaultFile = False):
	if (fetchFromDefaultFile):
		with open('Passwords/' + deviceID + '/hash.sha256' , 'r') as hashFile:
			knownHash = hashFile.read()

	return sha256_crypt.verify(stringToVerify , knownHash)

#Define a function to generate and save the hash of a new password:
def savePasswordHash(password):
	passwordHash = sha256_crypt.encrypt(password)

	if (not(os.path.exists('Passwords/' + deviceID))):
		os.mkdir('Passwords/' + deviceID)

	with open('Passwords/' + deviceID + '/hash.sha256' , 'w') as hashFile:
		hashFile.write(passwordHash)

#Define a function to generate and return a new netID:
def netIDGen():
	return Fernet.generate_key().decode('utf-8')

























