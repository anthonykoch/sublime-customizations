from Customizations.Utils import ignore, all_views


IS_FAILURE = 0
IS_SUCCESS = 1





def UpdateStatusCommand(status_id, status):
	for view in all_views():
		view.set_status(status_id, status)

def EraseStatusCommand(status_id):
	for view in all_views():
		view.erase_status(status_id)


commands = {
	"update_status": UpdateStatusCommand,
	"erase_status": EraseStatusCommand,
}




def run_command(command_name, data):
	if not command_name in commands:
		raise Exception('Command not found for command name {0}'.format(command_name))

	command = commands[command_name]
	command(**data)




def handle_received(command):
	with ignore(Exception, origin="handle_received"):
		# print(command)
		command_name = command['command_name']
		data = command['data']

		run_command(command_name, data)




def plugin_loaded():
	from Customizations.Server import on_received
	on_received(handle_received)








