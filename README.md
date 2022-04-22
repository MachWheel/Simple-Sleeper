# Simple-Sleeper
### *A simple way to schedule a Windows shut down (or restart), with an easy to use interface.*

# How to use it
![MAIN_DEMO](https://s10.gifyu.com/images/simple-sleeper.gif)

# How it works
The program works by making a simple Windows batch file, 
containing the SHUTDOWN command.

If you want to read more about the Windows SHUTDOWN command and all of its supported flags, go to:

https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/shutdown

The user interface allows you to choose the desired shut down 
or restart time, which gets converted into seconds and copied 
to /t flag of the command.

Currently supported modes are 'Shut down' and 
'Restart', using /s and /r flags respectively.

When the start button (green) is pressed, the selected options are
parsed into a temporary *'turn_off.bat'* file, which gets 
executed (scheduling the shut down) and deleted afterwards

When the abort button is pressed, the /a option is
parsed into a temporary *'turn_off.bat'* file, which gets 
executed (aborting the scheduled shut down) and deleted afterwards.