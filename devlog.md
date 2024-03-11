1. Implemented a filter to distinguish a W3A from a Notification instead of handling only the W3As that are named "DOC"

2. wrote variables using pythons env variable for USERPROFILE for paths for neater code and ability to run on more than one machine

3. Changed folder to RRC and added an IF listdir is empty condition for running
8/9/22

4. Implemented a try-catch block with an exception thats allows the script to continue upon the FileNotFoundError. This is a workout for bad code
8/14/22

5. Added subprocess library to open file explorer to today's folder with moved files
8/26/22

6. Conditonalized a couple things so if there isnt a file then most of the script doesnt run
   Added functionality to open file explorer to Downloads folder if no file is present
   Added a runtime function to log how long it takes to run
9/5/22

7. Did a lot of the PDF stuff. A lot
9/5/22

shututil seemed to work better than os for copying files

It seems easier to copy and write to a separate folder instead of over itself so i logged and filled an array to iterate over which contains the files to delete the rest of the files will be moved by the code in the original first script

OS wont let you rename/delete files while the file is open in an Object, so you must close it first. Best to use a context manager like "with open" which will auto close the file upon finishing the code in its indent block

os.path.normpath returns "a\\b\\c\\d" like for file explorer. can use replace ('\\','/') at the end of it to remedy this

merged the two scripts finally

8. 1/21/24 - 1/26/24
Ton of UI stuff with tkiner -> custom tkinter
Restructuring, trying to get it to run more logically and sequentially
More run conditionals


----

IVE GOTTA FIX it not recognizing 'noti' but it recognizes Noti