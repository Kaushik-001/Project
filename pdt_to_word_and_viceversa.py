# PDF TO WORD

from pdf2docx import Converter

# Define the input PDF file and output DOCX file
old_pdf = "Games/new_pdf.pdf"
new_docx = "Games/new.docx"

obj = Converter(old_pdf)

obj.convert(new_docx)
obj.close()

# DOCX/WORD TO PDF

from docx2pdf import Converter
convert("Games/new.docx","NEW_PDF_1.pdf")
