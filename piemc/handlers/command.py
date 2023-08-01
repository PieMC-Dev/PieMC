import inspect

registered_commands = {}

def Command(func):
    cmd_name = func.__name__.lower()
    registered_commands[cmd_name] = func
    return func

def handle_command(server, cmd):
    cmd_args = cmd.strip().split()
    cmd_name = cmd_args[0].lower()
    
    func = registered_commands.get(cmd_name)
    if func is not None:
        if inspect.getfullargspec(func).args:
            func(server, *cmd_args[1:])
        else:
            func(server)
    else:
        print(f"Command '{cmd_name}' not found.")
