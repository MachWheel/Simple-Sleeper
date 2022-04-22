# Simple-Sleeper
### *A simple way to schedule a Windows shut down (or restart), with an easy to use interface.*

# How to use it
![MAIN_DEMO](https://s10.gifyu.com/images/simple-sleeper.gif)

# How to install it
There is no installation needed.

Just download the zip file at [Releases](https://github.com/WyllerMachado/Simple-Sleeper/releases), extract it 
and run the **standalone .exe file**.

# How to compile it
Simple Sleeper is compiled into a standalone .exe file using PyInstaller.

To do it, first you will need to:

```
pip install pyinstaller
```

If you want to know more about PyInstaller and all of its 
supported features, go to: 

[PyInstaller Manual @ PyInstaller 5.0 documentation](https://pyinstaller.org/en/stable/)




# How it works
The program works by making a simple Windows batch file, 
containing the SHUTDOWN command.

If you want to know more about the Windows SHUTDOWN command and all of its 
supported flags, go to: 

[shutdown @ Microsoft Docs](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/shutdown)


The user interface allows you to choose the desired shut down 
or restart time, which gets converted into seconds and copied 
to /t flag of the command.

### Supported modes
Currently supported modes are **'Shut down'** and 
**'Restart'**, using **/s** and **/r** flags respectively.

### Scheduling
When the **start** button (green) is pressed, the selected options are
parsed into a temporary **'turn_off.bat'** file. For example, the demo 
above gets parsed into a file containing: 
```
SHUTDOWN /s /f /t 8700
```
Then, the file gets executed (scheduling the shut down) and deleted afterwards.

### Aborting
When the **abort** button (red) is pressed, the **/a** flag is
parsed into a temporary **'turn_off.bat'** file:
```
SHUTDOWN /a
```
which gets executed (aborting the scheduled shut down) and deleted afterwards.
