import PyPDF2
from PyPDF2 import PdfFileMerger, PdfFileReader
import os
import glob
#merging with another file from: https://stackoverflow.com/questions/17104926/pypdf-merging-multiple-pdf-files-into-one-pdf

#getting a path
script_path = os.path.dirname(os.path.abspath( __file__ ))
print(script_path)
a = '/'
string = a.join([script_path, "*.pdf"])
print (string)

#getting all the pdf at the particular path
pdfs = glob.glob(string)
print(pdfs[1])
print(len(pdfs))

#sorting all the pdfs alphabetically
new_pdfs = sorted(pdfs, key = str.lower)
print("\n".join(new_pdfs))

#merging the files
merger = PdfFileMerger()
for i in new_pdfs:
    file1 = open(i, 'rb')
    merger.append(PdfFileReader(file1))
    file1.close()
merger.write("PDF_output.pdf")
