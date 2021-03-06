@ECHO OFF
TITLE Compiling Simple-Sleeper...
ECHO:
ECHO This batch file compiles Simple-Sleeper application.
ECHO The folder containing the generated app will be opened afterwards.
ECHO If you get an error, do "pip install pyinstaller"
ECHO If the result file is .notanexecutable, run the compiler again.
ECHO:
PAUSE
MKDIR dist
pyinstaller -w --onefile ..\main.py --icon app_icon.ico --name Simple-Sleeper --splash splashfile.png
ECHO:
ECHO DONE! PRESS ANYTHING TO OPEN OUTPUT FOLDER
ECHO:
PAUSE
START dist
