import requests
import zipfile
import io
import os

repo_path = "PieMC-Dev/PieMC"

def check_for_updates(repo_url):
    api_url = f"https://api.github.com/repos/{repo_url}/tags"
    response = requests.get(api_url)

    if response.status_code == 200:
        latest_release = response.json()[0]
        latest_tag = latest_release["name"]
        current_tag = get_current_tag()

        if latest_tag != current_tag:
            print(f"New release available: {latest_tag}")
            zipball_url = latest_release["zipball_url"]
            destination_folder = ""
            update_download(zipball_url, destination_folder)
            update_config_file()
        else:
            print("No updates available.")
    else:
        print("Error occurred while checking for updates.")

def get_current_tag():
    # CURRENT VERSION DETECTION
    pass

def update_download(zipball_url, destination_folder):
    response = requests.get(zipball_url)
    if response.status_code == 200:
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
            zip_file.extractall(path=destination_folder)
    else:
        print(f"Failed to download asset from URL: {zipball_url}")
        
def update_config_file():
    new_config_file = "config.py.new"
    old_config_file = "config.py"
    if os.path.isfile(new_config_file):
        os.rename(new_config_file, old_config_file)
        print("Config file updated successfully.")
    else:
        print("Failed to update config file.")
        
check_for_updates(repo_path)