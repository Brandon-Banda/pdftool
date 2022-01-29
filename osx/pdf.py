from PyPDF2 import PdfFileWriter, PdfFileReader
import os

 # page numbering starts from 0

fileLocation = 'C:/Users/admin/Documents/work/testfile/test.pdf'
pdfObj = PdfFileReader(open(fileLocation, 'rb'))
pages_to_keep = [0, 1, 2, 3] # 4 pagers
pages_to_keep2 = [0, 3] # 4 pagers trimmed to 2 pages
pages_to_keep3 = [0] # 2 page w3a

pagecount = pdfObj.getNumPages() #log
print(pagecount) #log

output = PdfFileWriter()

for i in pages_to_keep:
    p = pdfObj.getPage(i)
    output.addPage(p)

with open('C:/Users/admin/Documents/work/testfile/newfile.pdf', 'wb') as f:
    output.write(f)