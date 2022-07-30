from datetime import date
import os
import shutil

date = date.today().strftime("%#m-%d-%Y")
downloads = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents/Work/Downloads')
main = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents/Work/')
todays = main + date + '/'

os.system('cls') # clear console

if not os.path.exists(downloads):
    print('CREATING DOWNLOADS FILE...')
    os.makedirs(downloads)

os.chdir(downloads)
print('Working in ' + os.getcwd() + "...")

if not os.path.exists(todays):
    print('CREATING TODAYS FILE...')
    os.makedirs(todays)

W3A = "DOC"
filt = ['DOC', 'Energy', 'Ltd', 'Company','Inc', 'Prod', 'Operat']
a = "Noti"
nid = 0
wid = 0

for file in os.listdir():
    for thing in filt:
        if thing in file:
            ftype = "W3A "
            wid += 1
            os.rename(file,'{}{} #{}.pdf'.format(ftype, date, wid))
            print(file + ' -> ' '{}{} #{}'.format(ftype, date, wid)) #log
    if a in file:
        ftype = "DN "
        nid += 1
        os.rename(file,'{}{} #{}.pdf'.format(ftype, date, nid))
        print(file + ' -> ' '{}{} #{}'.format(ftype, date, nid)) #log

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