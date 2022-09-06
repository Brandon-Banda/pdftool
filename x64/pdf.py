from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import shutil

os.system('cls') # clear console
 # page numbering starts from 0

fileLocation = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents/PDF TEST/test')

os.chdir(fileLocation)
print('Working in ' + os.getcwd() + "...")

pages_to_keep = [0, 1, 2, 3] # 4 pagers
pages_to_keep2 = [0, 3] # 4 pagers trimmed to 2 pages

for file in os.listdir():
    pdfObj = PdfFileReader(open(file, 'rb'))
    pagecount = pdfObj.getNumPages() 
    print(str(pagecount) + " pages in file : " + file)

    if pagecount == 2: # 2 page W3A
        page = pdfObj.getPage(0)
        twoPageHandler = PdfFileWriter()
        twoPageHandler.addPage(page)
        with open('C:/Users/Administrator/Documents/PDF TEST/finishtest/' + file, 'wb') as f:
            twoPageHandler.write(f)
        print('Trimmed ' + file + ' down to 1 page -')

    if pagecount > 4: # Produce sanitized 4 page W3As
        fourPageHandler = PdfFileWriter()
        for i in pages_to_keep:
            page = pdfObj.getPage(i)
            fourPageHandler.addPage(page)
        with open('C:/Users/Administrator/Documents/PDF TEST/finishtest/' + file, 'wb') as f:
            fourPageHandler.write(f)
        print('Trimmed ' + file + ' down to 4 page -')

    if pagecount == 4: # Take 4 page W3As and trim pages 2 and 3
        fourPageCopyHandler = PdfFileWriter()
        shutil.copyfile(file,'C:/Users/Administrator/Documents/PDF TEST/finishtest/' + file)
        print('Made a copy of ' + file)
        for i in pages_to_keep2:
            p = pdfObj.getPage(i)
            fourPageCopyHandler.addPage(p)
        fileName = os.path.splitext(file)[0]
        with open('C:/Users/Administrator/Documents/PDF TEST/finishtest/' + fileName + ' - Copy.pdf', 'wb') as f:
            fourPageCopyHandler.write(f)
        print('Trimmed ' + file + ' into a 2 page W3A for Drillinginfo -')


# cleanup function to delete all files in the folder

print ('--------------------')