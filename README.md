#  D-LANSIS
Distribted Local Area Network Sign In System

### About
 D-LANSIS (pronounced "DEE-LANsihs") is an open source project developed by Noah Troy, with the aim of giving organizations (such as schools, workplaces, etc.) the ability to run and maintain simple, inexpensive, and secure sign-in and accountability systems.

###Project Goals
- Create a system as inexpensive and independent as possible, eliminating the need for nonprofit and educational organizations to have to pay large amounts of money to big companies, in order to receive simple, yet necessary software.
- Keep the code extremely lightweight, allowing it to be easily run from a myriad of systems, including any old or extra technology lying around, or something as inexpensive as a ($35) [raspberry pi](https://www.raspberrypi.org/ "raspberry pi").
- Write all of the source code in an open-source, highly commented, and easily readable format, making it easier for any organization (or student) to modify, improve, or change the code to fit their needs.
- Have a support system built into the code, where users and administrators alike can easily get help and have all  of their questions answered in a user-friendly format.
- Maintain an extremely high level of security and data protection, using many different tested and open-source resources.
- Make the entire system completely decentralized, thereby limiting server costs, and providing redundency.
------------
###Installation Instructions
###### Please Note: This Software Is Currently Under Development, And Not Ready For Official Use Yet. Please Do Not Try To Install This Software Until The All-Clear Is Given. For The Latest Updates On Its Development, Feel Free To Bookmark This Page And Check Back As Often As You Like.
 1. Pick your target intallation device. We recommend a device with ***at least***:
  * A dual-core 1Ghz processor
  * 2GB of memory
  * 1 network interface, and a lan to connect it to (can be wireless or wired)
  * 16GB of internal storage
  * A usable keyboard or number pad, a mouse, and a monitor, for simple user interaction
 2. Download and install a compatible linux distribution onto that machine *(See dependencies list for more information on the exact requirements.)* 
  * We recommend using Ubuntu. The recommended desktop LTS (long-term support) version can be downloaded [here](https://www.ubuntu.com/download/desktop "here"), and the raspberry pi version may be downloaded [here](https://ubuntu-mate.org/raspberry-pi/ "here").
  * If you need help installing Ubuntu, please see this guide [here](https://tutorials.ubuntu.com/tutorial/tutorial-install-ubuntu-desktop#0 "here") for desktop computers, and this guide [here](https://fossbytes.com/install-ubuntu-mate-on-raspberry-pi-2-3/ "here") for raspberry pis.
 3. Clone this repository using the following command:
 ```bash
sudo apt update && sudo apt install git && cd ~ && git clone https://github.com/NoahTroy/D-LANSIS.git && cd D-LANSIS
```
 4. Install all of the necessary dependencies using the following command:
 ```bash
sudo apt install python3 python3-tk && sudo pip3 install cryptography rsa passlib
```
 5. Go to Settings>Power and set Blank Screen to Never, and turn Automatic Suspend off. This will allow the computer to function like a kiosk.
 6. Go to Settings>Devices>Keyboard and unbind all key combinations. This will prevent users from being able to access a terminal, or pull up any other features, limiting them to only the window provided by the code.
 7. Go to Settings>Privacy and turn off screenlock. This will stop the computer from automatically locking and preventing users from taking advantage of the system.
 8. Go to Settings>Notifications and turn off notifications. This will prevent users from being able to click on notification popups, and exit the sign-in application.
 9. Go to Settings>Details>Users and turn on automatic login. This will prevent administrators from having to log in, every time they power on the device.
 10. Open the startDLANSIS.conf file, and replace the text *PutYourUsernameHere* with your username. The following command will show you your username (it will be the italicised text, appearing like this: /home/*YourUsername*/D-LANSIS), then after twenty seconds (enough time for you to copy your username), it will open a text editor, allowing you to replace the *PutYourUsernameHere* text with your actual username. When you have done this, save the document, then close the text editor.
 ```bash
pwd && sleep 20 && gedit startDLANSIS.conf
```
 11. Now you must move the file to the systemd folder, so that the code may run automatically at boot. Use the following command to do so:
```bash
sudo mv startDLANSIS.conf /etc/systemd/startDLANSIS.conf
```
 12. The setup is now complete. As soon as you restart your computer, it will now function as if in kiosk mode, successfully running the script.
