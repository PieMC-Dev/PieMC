import requests
import os
import shutil
import zipfile

repo_url = "https://api.github.com/repos/PieMC-Dev/PieMC/releases/latest"

update_folder = os.path.join(os.path.dirname(__file__), "update")

config_file_path = os.path.join(os.path.dirname(__file__), "piemc", "config.py")

response = requests.get(repo_url)
if response.status_code == 200:
    latest_release = response.json()
    latest_version = latest_release['tag_name']
    
    version_file = os.path.join(os.path.dirname(__file__), "version.dat")
    if os.path.exists(version_file):
        with open(version_file, 'r') as file:
            current_version = file.read().strip()
    else:
        current_version = "0"
    
    if current_version < latest_version:
        print("New version available:", latest_version)
        
        if not os.path.exists(update_folder):
            os.makedirs(update_folder)
        
        asset_url = latest_release['zipball_url']
        response = requests.get(asset_url)
        if response.status_code == 200:
            zip_file_path = os.path.join(update_folder, "update.zip")
            with open(zip_file_path, 'wb') as file:
                file.write(response.content)
            print("Update file downloaded")
        else:
            print("Error downloading the update file")
        
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            extracted_folder = None
            for file_info in zip_ref.infolist():
                if file_info.is_dir():
                    extracted_folder = file_info.filename
                    break
            if extracted_folder is None:
                print("Error extracting the update folder from the zip file")
                exit(1)
            zip_ref.extractall(update_folder)
        
        for root, dirs, files in os.walk(os.path.join(update_folder, extracted_folder)):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, os.path.join(update_folder, extracted_folder))
                destination_path = os.path.join(os.path.dirname(__file__), relative_path)
                
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.move(file_path, destination_path)
                print("Updated file:", relative_path)
        
        with open(version_file, 'w') as file:
            file.write(latest_version)
        
        print("Server updated to version:", latest_version)
    
    else:
        print("The server is already up to date.")
    
    shutil.rmtree(update_folder)
    
else:
    print("Failed to retrieve repository information.")
