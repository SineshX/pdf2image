
# error_Wala_Code
# 
# 
# # import module
import pdf2image

# Store Pdf with convert_from_path function

images = pdf2image.convert_from_path("main.pdf")

for i in range(len(images)):
    images[i].save("page" + str(i) + ".jpg", "JPEG")
