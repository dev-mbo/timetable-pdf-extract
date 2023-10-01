
import pdfplumber 

class TableTextExtract:

    def __init__(self, pdf_file, pagenum, tablenum):
        self.pdf_file = pdf_file
        self.pagenum = pagenum
        self.tablenum = tablenum


    def _extract_table(self):
        pdf = pdfplumber.open(self.pdf_file)

        table_page = pdf.pages[self.pagenum]
        try:
            tables = table_page.extract_tables()
            table = tables[self.tablenum]
        except IndexError as e:
            print(f"{e}")
            print(f"{len(tables)}")
            print(f"{self.pdf_file}, {self.pagenum}, {self.tablenum}")
            return []
        
        return table
    

    def _table_converter(self, table):
        table_text = []

        for rownum in range(len(table)):
            row = table[rownum]
            table_text.append(row)

        return table_text
    

    def extract_text_from_table(self):
        table = self._extract_table()
        
        return self._table_converter(table)