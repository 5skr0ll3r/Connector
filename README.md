# Connector
Is a multi session handler written in python3

Run: `python3 main.py`


## Terminal Commands: 

**help** Usage: `help <command>`
calls 911
takes 0-1 arguments
- 0: Prints info for all the availlable commands
- 1: Prints info for a specific command

**connect** Usage: `connect <ip> <port> <alias>`
creates a client and tries to connect to a remote host
takes 3 arguments space seperated 
- Remote IP
- Port
- Alias


**listen** Usage: `listen <ip> <port> <alias>`
create a listener and awaites for remote connection
takes 3 arguments
- Interface
- Port
- Alias


**shell** Usage: `shell <alias>`
fronts the specified session
takes 1 argument
- Alias


**kill** Usage: `kill <alias>`
terminates the specified session
takes 1 argument
- Alias


**exit** Usage: `exit`
Terminates all sessions and exits the program
takes 0 arguments


## Shell commands:

**back/exit**
- Backgrounds the current session and returns to the main Terminal

