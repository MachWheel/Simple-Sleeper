@ECHO OFF
:: This batch file compiles Simple-Sleeper application
:: The generated app will be in the ./dist folder
:: First make sure to "pip install -r requirements.txt"
TITLE Compiling MessyFolderOrganizer...
MKDIR dist
pyinstaller --onefile -w compile.spec
ECHO:
ECHO DONE! PRESS ANYTHING TO OPEN OUTPUT FOLDER
ECHO:
PAUSE
START dist
