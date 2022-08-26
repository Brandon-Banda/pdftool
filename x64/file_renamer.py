from datetime import date
import os
import shutil
import subprocess

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

W3A = "DOC"
filter = ['DOC','Ltd', 'Energy','Company','Inc', 'Prod', 'LLC', 'Group', 'Corp']
a = "Noti"
nid = 0
wid = 0

if not len(os.listdir()) == 0:
    for file in os.listdir():
        for key in filter:
            if key in file:
                try:
                    ftype = "W3A "
                    wid += 1
                    os.rename(file,'{}{} #{}.pdf'.format(ftype, date, wid))
                    print(file + ' -> ' '{}{} #{}'.format(ftype, date, wid)) #log
                except FileNotFoundError:
                    continue
        if a in file:
            ftype = "DN "
            nid += 1
            os.rename(file,'{}{} #{}.pdf'.format(ftype, date, nid))
            print(file + ' -> ' '{}{} #{}'.format(ftype, date, nid)) #log
else:
    print('No files to work with')
    
print("------------Files Renamed---------")

#now that we know which files are which (besides W3s), we can bring in pyLib to figure out how many pages they have
# logic for this is :
    #while page > 5 : delete page 5,  OR delete every page beyond number 5
    #if page = 2 : delete page 2
    #if page = 3 : PRINT UHHHHHHHHHH
    #if page = 4 : delete pages 2, 3

# move renamed files to today's folder
file_names = os.listdir(downloads)
for file_name in file_names:
    shutil.move(os.path.join(downloads, file_name), todays)
print ('Moved renamed files...')

FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
sanitizedTodays = os.path.normpath(todays)
subprocess.run([FILEBROWSER_PATH, sanitizedTodays])