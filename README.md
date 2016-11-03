# Python-Keylogger (Linux)
A simple keylogger written in Python and shell script developed for Linux (background process included)

For installation and usage:
1. Edit the path in shell/keylog-start.sh
   For example: If you put your keylogger.py in a folder keylogger/ and just put it in your 
	/home/username/ directory, then edit the FILE as /home/username/keylogger/keylogger.py

2. If you want to add the keylogger as a startup program, then add it from Startup Applications 
   (you can search your computer for it) and add this command:
   
   cd /path/to/the/shell/script/shell/;./keylog-start.sh;cd

   (Edit the path so that your computer knows where the keylog-start.sh script is)

3. If you want to execute it manually, just execute the command in number 2 from your terminal.


