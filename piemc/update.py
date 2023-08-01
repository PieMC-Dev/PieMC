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

import requests
import os
from datetime import datetime

repo_url = "https://api.github.com/repos/PieMC-Dev/PieMC/releases"

def check_for_updates():
    response = requests.get(repo_url)
    if response.status_code == 200:
        releases = response.json()

        if releases:
            latest_release = releases[0]
            latest_version = latest_release['tag_name']
            latest_date = datetime.strptime(latest_release['published_at'], "%Y-%m-%dT%H:%M:%SZ")

            version_file = os.path.join(os.path.dirname(__file__), "version.dat")
            if os.path.exists(version_file):
                with open(version_file, 'r') as file:
                    current_date_str = file.read().strip()
                    current_date = datetime.strptime(current_date_str, "%Y-%m-%dT%H:%M:%SZ")
            else:
                current_date = datetime(1970, 1, 1)  # A default date for initial comparison

            if current_date < latest_date:
                print("⚠️\033[33mNew version available:\033[0m", latest_version)
                # You can add code here to perform the update, like downloading and installing the latest version.
            else:
                print("The server is already up to date.")
        else:
            print("No releases found for the repository.")
    else:
        print("Failed to retrieve repository information.")