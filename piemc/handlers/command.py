import importlib
import inspect
import pkgutil
import piemc.commands

registered_commands = {}

def Command(func):
    cmd_name = func.__name__.lower()
    registered_commands[cmd_name] = func
    return func

def handle_command(server, cmd):
    cmd = cmd.strip()
    if not cmd:
        print("Please enter a command.")
        return

    cmd_args = cmd.split()
    cmd_name = cmd_args[0].lower()
    
    func = registered_commands.get(cmd_name)
    if func is not None:
        if inspect.getfullargspec(func).args:
            func(server, *cmd_args[1:])
        else:
            func(server)
    else:
        print(f"Command '{cmd_name}' not found.")
        
def initialize_commands(self):
    command_classes = []
    package_path = piemc.commands.__path__
    package_name = piemc.commands.__name__ + '.'

    for importer, modname, ispkg in pkgutil.walk_packages(package_path, package_name):
        module = importlib.import_module(modname)
        command_classes.extend(cls for name, cls in inspect.getmembers(module, inspect.isclass) if hasattr(cls, 'Command'))

    for command_class in command_classes:
        setattr(self, command_class.__name__.lower(), command_class(self.logger, self))
