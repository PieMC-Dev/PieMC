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

from pathlib import Path
import requests

repo_url = "https://api.github.com/repos/PieMC-Dev/PieMC/releases"


def check_for_updates():
    response = requests.get(repo_url)
    if response.status_code == 200:
        releases = response.json()

        if releases:
            latest_release = releases[0]
            latest_release_id = latest_release["id"]

            release_id_file = Path(Path(__file__).parent, "latest_release_id.dat")
            if release_id_file.exists():
                with open(release_id_file, "r") as file:
                    current_release_id = int(file.read().strip())
            else:
                current_release_id = 114668911

            if current_release_id < latest_release_id:
                print("⚠️\033[33mNew version available:\033[0m", latest_release["tag_name"])

                with open(release_id_file, "w") as file:
                    file.write(str(latest_release_id))
            else:
                print("The server is already up to date.")
        else:
            print("No releases found for the repository.")
    else:
        print("Failed to retrieve repository information.")

if __name__ == "__main__":
    check_for_updates()