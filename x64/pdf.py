from PyPDF2 import PdfFileWriter, PdfFileReader
import os

os.system('cls') # clear console
 # page numbering starts from 0

fileLocation = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents/Work/test/')

os.chdir(fileLocation)
print('Working in ' + os.getcwd() + "...")

pages_to_keep = [0, 1, 2, 3] # 4 pagers
pages_to_keep2 = [0, 3] # 4 pagers trimmed to 2 pages

output = PdfFileWriter()

for file in os.listdir():
    pdfObj = PdfFileReader(open(file, 'rb'))
    pagecount = pdfObj.getNumPages() 
    print(str(pagecount) + " " + file)
    if pagecount == 2: # 2 page W3A
        page = pdfObj.getPage(0)
        output.addPage(page)
    # if pagecount > 4: # Produce sanitized 4 page W3As
    #     for i in pages_to_keep:
    #         p = pdfObj.getPage(i)
    #         output.addPage(p)
    # if pagecount == 4: # Take 4 page W3As and trim pages 2 and 3
    #     #for file in os.listdir():
    #         #with open(fileLocation + file + ' - Copy.pdf', 'wb') as f:
    #         #    output.write(f)
    #     for i in pages_to_keep2:
    #         p = pdfObj.getPage(i)
    #         output.addPage(p)

with open('C:/Users/Administrator/Documents/Work/test/' + file, 'wb') as f:
    output.write(f)