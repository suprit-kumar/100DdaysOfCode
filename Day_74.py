
"""
Write a program to manipulate pdf files using pyPDF.
Your programs should be able to merge multiple pdf files into a single pdf.
You are welcome to add more functionalities




pypdf is a free and open-source pure-python PDF library capable of splitting,
merging, cropping, and transforming the pages of PDF files.
It can also add custom data, viewing options, and passwords to PDF files.
pypdf can retrieve text and metadata from PDFs as well.
"""

from PyPDF2 import PdfFileReader
import os

class PdfFunctionalitis:
    def __init__(self):
        self.data = None

    def get_info(self,filepath):
        with open(filepath, 'rb') as f:
            pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
        print(f"File Info: {info}")
        author = info.author
        creator = info.creator
        producer = info.producer
        subject = info.subject
        title = info.title
        print(f"Number of pages: {number_of_pages}")
        print(f"author: {author} | creator: {creator} | producer: {producer} | subject: {subject} | title:{title}")


pdf_func = PdfFunctionalitis()
pdf_func.get_info('sample.pdf')