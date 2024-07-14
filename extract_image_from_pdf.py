from pikepdf import Pdf , Name , PdfImage

old_pdf = Pdf.open("Games/MINI project ppt(Final).pdf")
page_1 = old_pdf.pages[6]
#rint(list(page_1.images.keys())) #BRINGS OUT THE LIST OF CODES OF ALL THE IMAGES IN THAT PARTICULAR PAGE

raw_image = page_1.images['/Image49'] #Image id1

pdf_image = PdfImage(raw_image)

pdf_image.extract_to(fileprefix = "test1")

raw_image1 = page_1.images['/Image5'] #Image id2

pdf_image1 = PdfImage(raw_image1)

pdf_image1.extract_to(fileprefix = "test2")
