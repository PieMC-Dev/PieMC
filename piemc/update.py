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
from piemc.server import __version__

repo_url = "https://api.github.com/repos/PieMC-Dev/PieMC/releases"


def compare_versions(version1, version2):
    def normalize(v):
        numeric_part = ''.join(filter(str.isdigit, v))
        return [int(x) for x in numeric_part.split('.')]

    version1_parts = normalize(version1)
    version2_parts = normalize(version2)

    for v1, v2 in zip(version1_parts, version2_parts):
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1

    return 0

def check_for_updates():
    response = requests.get(repo_url)
    if response.status_code == 200:
        releases = response.json()

        if releases:
            latest_release = releases[0]
            latest_release_version = latest_release["tag_name"]

            current_release_version = __version__

            if compare_versions(current_release_version, latest_release_version) < 0:
                print("⚠️\033[33mNew version available:\033[0m", latest_release_version)
            else:
                print("The server is already up to date.")
        else:
            print("No releases found for the repository.")
    else:
        print("Failed to retrieve repository information.")

if __name__ == "__main__":
    check_for_updates()