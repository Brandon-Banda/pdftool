from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import shutil
from datetime import date

os.system('cls') # clear console
 # page numbering starts from 0

# this will be deleted after merge
date = date.today().strftime("%#m-%d-%Y")
fileLocation = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents/RRC/Downloads/')
main = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents/RRC/')
archive = main + '/archive/'
todays = archive + date + '/'

normalTodays = os.path.normpath(todays).replace("\\","/")

os.chdir(fileLocation)
print('Working in ' + os.getcwd() + "...")

pages_to_keep = [0, 1, 2, 3] # 4 pagers
pages_to_keep2 = [0, 3] # 4 pagers trimmed to 2 pages
delete_list = []

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
            delete_list.append(file)

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

print ('--------------------')