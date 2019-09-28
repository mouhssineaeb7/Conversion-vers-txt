#!/usr/bin/env python
# coding: utf-8

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter  
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO #StringIO Read and write strings as files
from docx import Document

"""
conversion function from pdf to txt format
"""

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager() #PDFResourceManager store shared resources such as fonts or images
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
#PDFPageInterpreter process the page contents and PDFDevice to translate it to whatever you need
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    string = retstr.getvalue()
    retstr.close()
    return string
"""
conversion function from docx to txt format
"""
def convert_docx_to_txt(path):
	document = Document(path)
	return "\n".join([para.text for para in document.paragraphs])
convert_pdf_to_txt("C:/Users/asus/Desktop/stage/Zine-it pfe/cvtest.pdf")
"""
function that reads all file ftypes (docx, pdf, txt)
"""

def read_file(fileName):
        extension = fileName.split(".")[-1] #return the extension of the file(last item of the name list)
        if extension == "txt":
            f = open(fileName, 'r') #simple reading of the txt file
            string = f.read()
            f.close() 
            return string
        elif extension == "doc":
            return subprocess.Popen(['antiword', fileName], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0], extension
        elif extension == "docx":
            try:
                return convert_docx_to_txt(fileName) #call to the conversion function docxtotxt
            except:
                return ''
                pass
        elif extension == "pdf":
            try:
                return convert_pdf_to_txt(fileName) #call to the conversion function pdftotxt
            except:
                return ''
                pass
        else:
            print ('Unsupported format')
            return '', ''
"""Test Example"""			
read_file("enter your file path") 