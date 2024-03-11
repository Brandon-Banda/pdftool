from datetime import date
import os
import shutil
import subprocess
import time
from PyPDF2 import PdfFileWriter, PdfFileReader

pages_to_keep = [0, 3]

if not len(os.listdir()) == 0:
    for file in os.listdir():
        fourPageCopyHandler = PdfFileWriter()
        for i in pages_to_keep2:
			p = pdfObj.getPage(i)
            fourPageCopyHandler.addPage(p)
        fileName = os.path.splitext(file)[0]
        with open(normalTodays  + '/' + fileName + ' - Copy.pdf', 'wb') as f:
        fourPageCopyHandler.write(f)
        print('Trimmed ' + file + ' into a 2 page W3A for Drillinginfo -')	