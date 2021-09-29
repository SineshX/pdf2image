# working code :)


# Import Library
from pdf2jpg import pdf2jpg

# Enter PDF File With extensions
pdf_file_path = "main.pdf"

# Output Folder Name
folder_name = "ConvertedImages"

# Convert Single Page
# pdf2jpg.convert_pdf2jpg(pdf_file_path, folder_name, pages="1")

# Convert Multiple Pages
# pdf2jpg.convert_pdf2jpg(pdf_file_path, folder_name, pages="1,0,3")

# Convert All Pages
pdf2jpg.convert_pdf2jpg(pdf_file_path, folder_name, pages="ALL")

# with overwriting prop :) will fix
#  will add option file name + sys arg 