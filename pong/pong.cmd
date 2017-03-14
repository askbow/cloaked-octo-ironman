@echo off
SET scriptpath=%~dp0

rem TODO:
rem simple way to check for python presense: https://stackoverflow.com/questions/4920483/batch-file-to-check-if-python-is-installed/26241114#26241114
rem python --version 2>NUL
rem if errorlevel 1 goto errorNoPython
rem 
rem rem here goes python
rem python %scriptpath%pong.py
rem 
rem goto:eof
rem :errorNoPython
rem echo.
rem echo Python not installed. Continue with standard ping:
echo ==========================
echo World-wide PING starting
echo ==========================

for /F "tokens=1,*" %%A   in (%scriptpath%pinglist.txt) do @echo ========================== & @echo . & @echo     %%B & ping -w 500 -l 100 -n 3 %%A

echo ==========================
echo World-wide PING complete
echo ==========================
echo next stage - long ping 8.8.8.8
pause
ping -w 50 -l 32 -t 8.8.8.8
