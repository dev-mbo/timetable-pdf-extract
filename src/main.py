import typer
import PyPDF2

from rich import print
from pdfminer.high_level import (
    extract_pages, 
    extract_text
)
from pdfminer.layout import (
    LTTextContainer, 
    LTChar, 
    LTRect, 
    LTFigure
)
from extractors.image import ImageTextExtract
from extractors.table import TableTextExtract


app = typer.Typer()

@app.command()
def export_timetable(pdf_file: str):
    
    pdf_pages = extract_pages(pdf_file)

    pdf = PyPDF2.PdfReader(pdf_file)

    image_text = []
    table_text = []

    for pagenum, page in enumerate(pdf_pages):
        tablenum = 0
        for element in page:

            if isinstance(element, LTTextContainer):
                # process text
                # elements.append("LTTextContainer")
                print("text found ..")
                pass

            if isinstance(element, LTFigure):
                page_obj = pdf.pages[pagenum]

                # process image
                img_txt_ext = ImageTextExtract(element, page_obj)
                text = img_txt_ext.extract_text_from_image()
                image_text.append(text)

            if isinstance(element, LTRect):
                # process table
                # elements.append("LTRect")
                tbl_txt_ext = TableTextExtract(pdf_file, pagenum, tablenum)
                text = tbl_txt_ext.extract_text_from_table()

                table_text.append(text)
                tablenum += 1

    # text = list(filter(lambda elem: elem == "LTTextContainer", elements))
    # images = list(filter(lambda elem: elem == "LTFigure", elements))
    # table = list(filter(lambda elem: elem == "LTRect", elements))

    # print(len(text), len(images), len(table))
    print(image_text)
    print(table_text)


if __name__ == '__main__':
    app()