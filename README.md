# MinecraftModUpdater
Automatically download mods pack from specified URLs, then use hash to update or delete the mods in the ./mods folder.
# URLs
`manifestURL="path to minifest"  `  
It will download mod zip package specified in minifest from same path with minifest doc.
# Format of minifest
`package:packagename`  
Jsut simply replace the package name with your zip file.
# How it work
It will read minifest from URL, then parse find out the package name.
Then it will download and unzip the package to temp folder.
Finally the script will hash all files in` ./mods` and `./mcUpdaterTemp`.  
After comparison process work done, it will copy, delete all needed mods in `./mods` and from `./mcupdaterIcon` folder.

# Build
 To make it a binary, I choosed pyinstaller as solution.  
 `python3 is needed ` in this work, I installed `3.10`  
 Building scripts:  
 `"Path to python" Python310\Scripts\pyinstaller.exe -D .\minecraftUpdater.py -i'.\mcupdaterIcon.ico' -c`  
 If you don't need icon  
  `"Path to python" Python310\Scripts\pyinstaller.exe -D .\minecraftUpdater.py -c `  
I tried pack it all into one exe file. but Microsoft Defender will treat it as malware refusing to run. Just in case you meet such fails.