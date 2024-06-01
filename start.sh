#!/bin/bash
echo "PieMC Server Software for Minecraft: Bedrock Edition"

# Find Python
if command -v python3 >/dev/null 2>&1; then
  python_executable="python3"
elif command -v python >/dev/null 2>&1; then
  python_executable="python"
else
  echo "Python not found"
  exit 1
fi

# Install required dependencies silently
$python_executable -m pip install -r requirements.txt > /dev/null

# Start the server
python3 start.py

# Pause the script to keep the terminal open for further inspection
read -p "Press Enter to exit."
