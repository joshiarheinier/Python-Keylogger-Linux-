# Python-Keylogger (Linux)
A simple keylogger written in Python and shell script developed for Linux (background process and startup included)

For installation and usage:
1. Edit the path in shell/initiate.sh
   For example: If you put your keylogger.py in a folder keylogger/ and just put it in your 
	/home/username/ directory, then edit the FILE as /home/username/keylogger/keylogger.py

2. Edit the path in shell/start-keylog
   Put the path to your shell folder in it. For example: If your directory is like in number 1, 
   and the shell folder is the subfolder of /home/username/keylogger/ folder, then edit the path 
   as /home/username/keylogger/shell/

3. If you want to execute it, just execute the start-keylog by typing the path for start-keylog 
   on your terminal.
   For example: /home/username/keylogger/shell/start-keylog

4. You can execute the program automatically when you first boot up your computer.
   First, open the Startup Applications manager (You can find it using Dash).
   Then, click the Add button, and put the command in number 3 in the command field.
   You can also put the name and comment as what you desire on the other fields.
   Don't forget to save it.

5. If you want to see the log, you can see it in the shell subfolder, along with initiate.sh 
   and start-keylog.
