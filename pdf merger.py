# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 09:54:26 2018

@author: hl3803
"""

#make a pdf merge function that merges all .pdf files in a directory into a single pdf
#sorts by file name, sticks them all together.

#added feature to check if "final pdf" compiled name is in folder already, and remove it from interested list
#can be run and overwrite multiple times without interferring with code; old data will be obliterated

import PyPDF2, os

#define common variables:
#these are editable to where you are working and what the file is called (use underscore to have it at top of file explorer)
targetdirectory = "C:/Users/hl3803/OneDrive - DuPont/Relief valve stuff/ioMosaic/Information requests/1-9-2018/BPF239529/"
finalpdf = "_BPF239529 - Combined.pdf"
#------------------------------------------------------------------------------
overwritefile = False
pdfFiles = []

#get all the PDF filenames
for filename in os.listdir(targetdirectory):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
#if program already ran, and old result is there, skip using old result; otherwise recursion error (due to PyPDF2 failing EOF marker in pdf generation)
if finalpdf in pdfFiles:
    pdfFiles.remove(finalpdf)
    overwritefile =True

pdfFiles.sort(key=str.lower)
pdfWriter = PyPDF2.PdfFileWriter()

#open all the PDF's in order to add them
for filename in pdfFiles:
    pdfFileObj = open(targetdirectory + filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    #add all the files
    for pageNum in range(0,pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    
#save the results of the combination
pdfOutput = open(targetdirectory+finalpdf,'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()


