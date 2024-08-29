from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
import io

input_pdf_path = "Usage.pdf"
h_pad = 15
v_pad = 15


reader = PdfReader(input_pdf_path)
writer = PdfWriter()


def add_border_number(page, page_number):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setStrokeColorRGB(0, 0, 0)  # Black border
    can.setLineWidth(2)
    width, height = letter
    can.rect(h_pad, v_pad, width- 2*h_pad, height- 2*v_pad)  # Rectangle with  margin (left, bottom, right, top)
    can.drawString(width - 0.6*inch, 0.5 * inch, f"{page_number}")  # Add page number at bottom right corner
    can.save()

    packet.seek(0)
    border_pdf = PdfReader(packet)
    border_page = border_pdf.pages[0]

    border_page.merge_page(page)
    return border_page

writer = PdfWriter()
for page_number, page in enumerate(reader.pages, start=1):
    bordered_page = add_border_number(page, page_number)
    writer.add_page(bordered_page)

op_path = "output.pdf"
with open(op_path, "wb") as f:
    writer.write(f)