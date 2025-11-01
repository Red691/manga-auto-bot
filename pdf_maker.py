from fpdf import FPDF
from PIL import Image

def images_to_pdf(images, pdf_name):
    pdf = FPDF()
    for img_path in images:
        img = Image.open(img_path)
        pdf.add_page()
        pdf.image(img_path, x=10, y=10, w=pdf.w - 20)
    pdf.output(pdf_name, "F")
  
