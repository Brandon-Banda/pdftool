from PyPDF2 import PdfFileWriter, PdfFileReader
import os

 # page numbering starts from 0

fileLocation = 'C:/Users/admin/Documents/work/testfile/'

os.chdir('C:/Users/admin/Documents/work/testfile/')
print('Working in ' + os.getcwd() + "...")

pages_to_keep = [0, 1, 2, 3] # 4 pagers
pages_to_keep2 = [0, 3] # 4 pagers trimmed to 2 pages
pages_to_keep3 = [0] # 2 page w3a


output = PdfFileWriter()

for file in os.listdir():

    pdfObj = PdfFileReader(open(file, 'rb'))
    pagecount = pdfObj.getNumPages() 
    print(str(pagecount) + " " + file)
    if pagecount = 2: # 2 page W3A
        for i in pages_to_keep3:
            p = pdfObj.getPage(i)
            output.addPage(p)
    elif pagecount > 4: # Produce sanitized 4 page W3As
        for i in pages_to_keep:
            p = pdfObj.getPage(i)
            output.addPage(p)
    elif pagecount = 4: # Take 4 page W3As and trim pages 2 and 3
        for file in os.listdir():
            ''' this is copying all the 4pagers but i need to make it where only the "copy"s are edited
            with open('C:/Users/admin/Documents/work/testfile/' + file + ' - Copy.pdf', 'wb') as f:
            output.write(f)

            I need to fix file so it trims the pdf extension
            '''
        for i in pages_to_keep2:
            p = pdfObj.getPage(i)
            output.addPage(p)

#with open('C:/Users/admin/Documents/work/testfile/' + file, 'wb') as f:
    #output.write(f)
# fix this to rename per elif ^