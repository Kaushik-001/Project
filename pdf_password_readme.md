PDF Encryption and Permission Modification Script
This repository contains a Python script that utilizes the pikepdf library to modify the permissions of an existing PDF file and save it as a new, encrypted PDF. The main features of this script include:

->Opening an Existing PDF: The script reads an existing PDF file from the specified path.

->Setting Permissions: It sets custom permissions to restrict certain actions, such as preventing text and image extraction.

->Saving with Encryption: The modified PDF is saved with encryption, requiring a user password to open and protected by an owner password.

Script Details
Import pikepdf Library:

python
Copy code
import pikepdf
Open Existing PDF:

python
Copy code
old_pdf = pikepdf.Pdf.open("Games/MINI project ppt(Final).pdf")
Set Permissions:

python
Copy code
no_extr = pikepdf.Permissions(extract=False)
Save New PDF with Encryption:

python
Copy code
old_pdf.save("Games/new_pdf.pdf", encryption=pikepdf.Encryption(user="1001kk", owner="KKkamat", allow=no_extr))
Usage
To use this script, ensure you have the pikepdf library installed. You can install it using pip:

bash
Copy code
pip install pikepdf
Then, update the file paths and passwords as needed and run the script to generate your encrypted PDF with modified permissions.

Requirements:-
Pikepdf library
