@echo off
title PieMC Server Software for Minecraft: Bedrock Edition

REM Find Python
where py >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    where python >nul 2>&1
    if %ERRORLEVEL% NEQ 0 (
        echo Python not found.
        pause
        exit
    )
    set PYTHON=python
) else (
    set PYTHON=py
)

REM Install required dependencies silently
%PYTHON% -m pip install -r requirements.txt >nul 2>&1

REM Start the server
%PYTHON% -m piemc

REM Pause the script to keep the window open for further inspection
pause
