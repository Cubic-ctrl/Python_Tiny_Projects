# importing Python Modules
import PyPDF2

Pdf_File= open("mypdf.pdf", "rb")
PDF_Reader = PyPDF2.PdfFileReader(Pdf_File)
Text = PDF_Reader.getPage(0).extractText()
print(Text)
