from io import StringIO
from unittest import result
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from datetime import datetime
import re
import os


today = datetime.today().strftime('%m%d')
HANDOUT_MINE_NAME = 'handout_mine'
HANDOUT_MINE_PATH = f'../{HANDOUT_MINE_NAME}/{today}/hws/'


def convert_pdf_to_txt(HANDOUT_MINE_PATH):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(HANDOUT_MINE_PATH, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text


file_list = os.listdir(HANDOUT_MINE_PATH)


def get_contents():
    pdf_to_text_list = [convert_pdf_to_txt(
        HANDOUT_MINE_PATH+i) for i in file_list]

    reg = re.compile('\d+\.\s.+')

    result = []
    for i in map(reg.findall, pdf_to_text_list):
        title = i[0]

        def inner(x):
            if x == title:
                return False
            else:
                return True

        result.append(list(filter(inner, i)))

    return result
