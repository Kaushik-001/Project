import pikepdf

old_pdf = pikepdf.Pdf.open("Games/MINI project ppt(Final).pdf")

no_extr = pikepdf.Permissions(extract=False) 

old_pdf.save("Games/new_pdf.pdf",encryption= pikepdf.Encryption(user = "1001kk",owner = "KKkamat",allow = no_extr)) #user here stands for the password
