# Connector
Is a multi session handler written in python3

Run: `python3 main.py`


## Terminal Commands: 

**help** 
calls 911
takes 0-1 arguments
- 0: Prints info for all the availlable commands
- 1: Prints info for a specific command

**connect** 
creates a client and tries to connect to a remote host
takes 3 arguments space seperated
- Remote IP
- Port
- Alias

**listen**
create a listener and awaites for remote connection
takes 3 arguments
- Interface
- Port
- Alias

**shell**
fronts the specified session
takes 1 argument
- Alias

**kill**
terminates the specified session
takes 1 argument
- Alias

**exit**
Terminates all sessions and exits the program
takes 0 arguments

## Shell commands:

**back/exit**
- Backgrounds the current session and returns to the main Terminal

