# import fitz

# pdffile = "main.pdf"
# doc = fitz.open(pdffile)
# page = doc.loadPage(0)  # number of page
# pix = page.getPixmap()
# output = "outfile.png"
# pix.writePNG(output)

# *------------------------------------------------ *#
import sys, fitz  # import the bindings
fname = sys.argv[1]  # get filename from command line
doc = fitz.open(fname)  # open document
for page in doc:  # iterate through the pages
    pix = page.get_pixmap()  # render page to an image
    pix.save("page-%i.png" % page.number)  # store image as a PNG



''' 
# Import Library
import fitz

# Enter PDF File With extensions
pdf_file_path = ""

# Read PDF File
pdf_file = fitz.open(pdf_file_path)

# Iterate through all pages
for i in range(len(pdf_file)):

  # Load each page
  page = pdf_file.loadPage(i)

  # Get all pixel of page
  page_pixel = page.getPixmap()

  # Write all page pixel in image format
  page_pixel.writePNG(f"image {i}.png")


'''