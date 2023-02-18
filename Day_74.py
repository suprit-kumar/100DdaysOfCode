
"""
Write a program to manipulate pdf files using pyPDF.
Your programs should be able to merge multiple pdf files into a single pdf.
You are welcome to add more functionalities




pypdf is a free and open-source pure-python PDF library capable of splitting,
merging, cropping, and transforming the pages of PDF files.
It can also add custom data, viewing options, and passwords to PDF files.
pypdf can retrieve text and metadata from PDFs as well.
"""

from PyPDF2 import PdfWriter,PdfReader
import os

merger = PdfWriter()
reader = PdfReader("sample.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
print(number_of_pages)
print(page)
print(text)


files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()