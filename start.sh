#!/bin/bash
echo "PieMC Server Software for Minecraft: Bedrock Edition"

# Install required dependencies silently
pip install -r requirements.txt > /dev/null

# Start the server
python3 start.py

# Display message after the server process has stopped
echo "Server process stopped."

# Pause the script to keep the terminal open for further inspection
read -p "Press Enter to exit."
