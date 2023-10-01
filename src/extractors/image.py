import os
import PyPDF2


import pytesseract

from PIL import Image
from pdf2image import convert_from_path
        
class ImageTextExtract():

    def __init__(self, element, page_obj):
        self.element = element
        self.page_obj = page_obj

        self.tmp_pdf = 'tmp_image.pdf'
        self.tmp_png = 'tmp_image.png'


    def _crop_image(self):
        [
            left,
            top,
            right,
            bottom
        ] = [self.element.x0, self.element.y0, self.element.x1, self.element.y1]

        self.page_obj.mediabox.lower_left = (left, bottom)
        self.page_obj.mediabox.upper_right = (right, top)

        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(self.page_obj)

        with open('tmp_image.pdf', 'wb') as tmp_image:
            pdf_writer.write(tmp_image)


    def _convert_2_image(self):
        images = convert_from_path(self.tmp_pdf)
        image = images[0]
        image.save(self.tmp_png, "PNG")


    def _image_2_text(self):
        image = Image.open(self.tmp_png)
        text = pytesseract.image_to_string(image)
        return text


    def extract_text_from_image(self):
        self._crop_image()
        self._convert_2_image()
        text = self._image_2_text()

        os.remove(self.tmp_pdf)
        os.remove(self.tmp_png)

        return text
