from datetime import date
import os

date = date.today().strftime("%#m-%d-%Y")
downloads = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents/Work/Downloads')
main = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents/Work/')

os.system('cls') # clear console

### Use Windows explorer Preview pane to quickly check pages

### TODO Files need to move to the current date folder

if not os.path.exists(downloads):
    print('CREATING FILE...')
    os.makedirs(downloads)

os.chdir(downloads)
print('Working in ' + os.getcwd() + "...")

if not os.path.exists(main + date + '/'):
    print('CREATING FILE...')
    os.makedirs(main + date + '/')


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

#this stuff is for when we progamatically move files from the downloads to todays folder
#os.chdir(main + date + '/')
#print('Working in ' + os.getcwd() + "...") #log

print("------------Files Renamed---------")

#now that we know which files are which (besides W3s), we can bring in pyLib to figure out how many pages they have
# logic for this is :
    #while page > 5 : delete page 5,  OR delete every page beyond number 5
    #if page = 2 : delete page 2
    #if page = 3 : PRINT UHHHHHHHHHH
    #if page = 4 : delete pages 2, 3

#at the end, purge the folder
