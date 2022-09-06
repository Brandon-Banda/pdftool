from datetime import date
import os
import shutil
import subprocess
import time

startTime = time.time() #logging runtime

date = date.today().strftime("%#m-%d-%Y")
downloads = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents/RRC/Downloads')
main = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents/RRC/')
archive = main + '/archive/'
todays = archive + date + '/'
 
os.system('cls') # clear console

if not os.path.exists(downloads):
    print('CREATING DOWNLOADS FILE...')
    os.makedirs(downloads)

os.chdir(downloads)
print('Working in ' + os.getcwd() + "...")

if not os.path.exists(archive):
    print('CREATING ARCHIVE FILE...')
    os.makedirs(archive)

if not os.path.exists(todays):
    print('CREATING TODAYS FILE...')
    os.makedirs(todays)

filter = ['DOC','Ltd', 'Energy','Company','Inc', 'Prod', 'LLC', 'Group', 'Corp']
nid = 0
wid = 0

if not len(os.listdir()) == 0:
    for file in os.listdir():
        for key in filter:
            if key in file:
                try:
                    wid += 1
                    os.rename(file,'{}{} #{}.pdf'.format("W3A ", date, wid))
                    print(file + ' -> ' '{}{} #{}'.format("W3A ", date, wid)) #log
                except FileNotFoundError:
                    continue
        if 'Noti' in file:
            nid += 1
            os.rename(file,'{}{} #{}.pdf'.format("DN ", date, nid))
            print(file + ' -> ' '{}{} #{}'.format("DN ", date, nid)) #log
    print("------------Files Renamed---------")
else:
    print('No files to work with')

# move renamed files to today's folder and open it in file explorer
# otherwise if no files, open downloads folder
if not len(os.listdir()) == 0:
    file_names = os.listdir(downloads)
    for file_name in file_names:
        shutil.move(os.path.join(downloads, file_name), todays)
    print ('Moved renamed files...')
    FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
    sanitizedTodays = os.path.normpath(todays)
    subprocess.run([FILEBROWSER_PATH, sanitizedTodays])

else:
    FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
    sanitizedDownloads = os.path.normpath(downloads)
    subprocess.run([FILEBROWSER_PATH, sanitizedDownloads])

executionTime = (time.time() - startTime)
print('Runtime: ' + str(executionTime) + ' seconds')