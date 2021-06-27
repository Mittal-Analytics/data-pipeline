"""Usage:
filepath = 'samples/quarterly-results/imfa-mar-21.pdf
pdf = extract.PDFparse(filepath)
page = pdf.find_page_containing_title('BALANCE')
page_full_text = pdf.get_text(pno=0)
"""
import pdftotext
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTText, LTTextBox, LTTextLine


def page_text(page):
    return "".join(el.get_text() for el in page if isinstance(el, LTText))


class PDFparse:
    """
    TOOD:
    find_page_containing_title
    find_tables
    extract_table_data
    """

    def __init__(self, filepath):
        self.tree = list(extract_pages(filepath))
        with open(filepath, "rb") as f:
            self.pdftext = pdftotext.PDF(f)
        self._cache = {}
        self._main_text = {}

    def find_page_containing_text(self, search):
        pageno = next((i for i, p in enumerate(self.pdftext) if search in p), None)
        return self.tree[pageno] if pageno else None

    def find_page_containing_title(self, search):
        for pno, page in enumerate(self.tree):
            if pno in self._main_text:
                text = self._main_text[pno]
            else:
                text = self._main_text_of_page(page)
                self._main_text[pno] = text
            if search in text:
                return page
        return

    def _main_text_of_page(self, page, top=0.1):
        """plain text of top 10% of page."""
        h = page.height * (1 - top)
        text = ""
        for el in page:
            if (el.y0 > h) and isinstance(el, LTText):
                text += el.get_text()
        return text

    def get_text(self, pno=None, page=None):
        if pno is not None:
            return self.pdftext[pno]
        if page is None:
            Exception
        return page_text(page)
