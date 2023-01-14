class Terminal:

	
	commands = {
	
		'help' : {
			'details' : f'Help is on the way\n\thelp <command>',
			'min_args' : 0,
			'max_args' : 1
		},

		'connect' : {
			'details' : f'Connect to a remote host \n\tconnect <IP> <Server_Port> <Alias>',
			'min_args' : 3,
			'max_args' : 3
		},
		'listen' : {
			'details' : f'Start a listener on specified interface and port and await remote connection \n\tlisten <IP/interface> <Port> <Alias>',
			'min_args' : 3,
			'max_args' : 3
		},	

		'sessions' : {
			'details' : f'Sessions of machines that you have succesfully accessed.',
			'min_args' : 0,
			'max_args' : 0
		},
			
		'shell' : {
			'details' : f'Enable an interactive pseudo-shell for a session. Type back to background the session. \n\tshell <Alias>',
			'min_args' : 1,
			'max_args' : 1
		},					

		'kill' : {
			'details' : f'Terminate a session. \n\tkill <Alias>',
			'min_args' : 1,
			'max_args' : 1
		},		

		'clear' : {
			'details' : f'Clears the screen?.',
			'min_args' : 0,
			'max_args' : 0
		},

		'exit' : {
			'details' : f'Kill all sessions and quit.',
			'min_args' : 0,
			'max_args' : 0
		},
	
	}
	@staticmethod
	def isValid(command, num_of_args):
		
		isValid = True
		
		if command not in Terminal.commands:
			print('Unknown command.')
			isValid = False
			
		elif num_of_args < Terminal.commands[command]['min_args']:
			print('Missing arguments.\nType help <command> to get more information')
			isValid = False
		
		elif num_of_args > Terminal.commands[command]['max_args']:
			print('Too many arguments.')
			isValid = False			
	
		return isValid

	@staticmethod
	def printHelp():
		for i in Terminal.commands:
			print(f"\n{i}")
			for x in Terminal.commands[i]:
				print(f"\t{x}: {Terminal.commands[i][x]}")


	@staticmethod
	def commHelp(command):
		print(f"\n{command}:")
		for i in Terminal.commands[command]:
			print(f"\t{i}: {Terminal.commands[command][i]}")


