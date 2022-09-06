from datetime import date
import os
import shutil
import subprocess
import time
from PyPDF2 import PdfFileWriter, PdfFileReader

startTime = time.time() #logging runtime

date = date.today().strftime("%#m-%d-%Y")
downloads = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents/RRC/Downloads')
main = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents/RRC/')
archive = main + '/archive/'
todays = archive + date + '/'
normalTodays = os.path.normpath(todays).replace("\\","/")
 
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

pages_to_keep = [0, 1, 2, 3] # 4 pagers
pages_to_keep2 = [0, 3] # 4 pagers trimmed to 2 pages
delete_list = []

def handleFourPagers(x): # im cringe
    fourPageCopyHandler = PdfFileWriter()
    shutil.copyfile(x, normalTodays  + '/' + x)
    print('Made a copy of ' + x)
    for i in pages_to_keep2:
        p = pdfObj.getPage(i)
        fourPageCopyHandler.addPage(p)
    fileName = os.path.splitext(x)[0]
    with open(normalTodays  + '/' + fileName + ' - Copy.pdf', 'wb') as f:
        fourPageCopyHandler.write(f)
    print('Trimmed ' + x+ ' into a 2 page W3A for Drillinginfo -')
    delete_list.append(x)

for file in os.listdir():
    with open(file, "rb") as f:
        pdfObj = PdfFileReader(f)
        pagecount = pdfObj.getNumPages() 
        print(str(pagecount) + " pages in file : " + file)

        if pagecount == 2: # 2 page W3A
            page = pdfObj.getPage(0)
            twoPageHandler = PdfFileWriter()
            twoPageHandler.addPage(page)
            with open(normalTodays + '/' + file, 'wb') as f:
                twoPageHandler.write(f)
            print('Trimmed ' + file + ' down to 1 page -')
            delete_list.append(file)

        if pagecount > 4: # Produce normal 4 page W3As
            fourPageHandler = PdfFileWriter()
            for i in pages_to_keep:
                page = pdfObj.getPage(i)
                fourPageHandler.addPage(page)
            with open(normalTodays  + '/' + file, 'wb') as f:
                fourPageHandler.write(f)
            print('Trimmed ' + file + ' down to 4 page -')
            fileName = os.path.splitext(file)[0]
            print(str(pagecount) + " pages in file : " + file)  # at this point it still says the pagecount is 5, this backs up that "file" is still the shit one...
            delete_list.append(file)
            #handleFourPagers(file) # i'm sending the shit one to the function. i need to send the actual trimmed 4 pager which is lost in memory atm

        if pagecount == 4: # Take 4 page W3As and trim pages 2 and 3
            fourPageCopyHandler = PdfFileWriter()
            shutil.copyfile(file, normalTodays  + '/' + file)
            print('Made a copy of ' + file)
            for i in pages_to_keep2:
                p = pdfObj.getPage(i)
                fourPageCopyHandler.addPage(p)
            fileName = os.path.splitext(file)[0]
            with open(normalTodays  + '/' + fileName + ' - Copy.pdf', 'wb') as f:
                fourPageCopyHandler.write(f)
            print('Trimmed ' + file + ' into a 2 page W3A for Drillinginfo -')
            delete_list.append(file)

# cleanup function to delete all files in the folder

print ('Deleting... ' + str(delete_list))
for i in delete_list:
    os.remove(i)

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

elif len(os.listdir(todays)) == 0:
    FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
    sanitizedDownloads = os.path.normpath(downloads)
    subprocess.run([FILEBROWSER_PATH, sanitizedDownloads])

executionTime = (time.time() - startTime)
print('Runtime: ' + str(executionTime) + ' seconds')