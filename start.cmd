@echo off
title PieMC Server Software for Minecraft: Bedrock Edition

REM Install required dependencies silently
python -m pip install -r requirements.txt > nul

REM Start the server
python start.py

REM Display message after the server process has stopped
echo Server process stopped.

REM Pause the script to keep the window open for further inspection
pause
