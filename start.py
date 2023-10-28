# -*- coding: utf-8 -*-

#  ____  _      __  __  ____
# |  _ \(_) ___|  \/  |/ ___|
# | |_) | |/ _ \ |\/| | |
# |  __/| |  __/ |  | | |___
# |_|   |_|\___|_|  |_|\____|
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# @author PieMC Team
# @link http://www.PieMC-Dev.github.io/

import subprocess
def check_python_version():
    try:
        # Attempt to run the 'python' command and check if it's available
        subprocess.check_output('python --version', shell=True)
        return 'python'
    except subprocess.CalledProcessError:
        try:
            # Attempt to run the 'python3' command and check if it's available
            subprocess.check_output('python3 --version', shell=True)
            return 'python3'
        except subprocess.CalledProcessError:
            raise Exception("Neither 'python' nor 'python3' found in your system.")

selected_python_command = check_python_version()
print(f"launching with the command: {selected_python_command}")
subprocess.call(['python', '-m', 'piemc'])
