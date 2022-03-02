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

# 본인 handout_mine 폴더명으로 수정하기
HANDOUT_MINE_NAME = 'handout_mine'

HANDOUT_MINE_PATH = f'../{HANDOUT_MINE_NAME}/{today}/hws/'

# pdt to txt인데 저도 긁어온거에요 한줄한줄 해석안하셔도 되요


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


# hws 폴더 안에 있는 파일 목록
try:
    file_list = os.listdir(HANDOUT_MINE_PATH)
except:
    pass


def get_contents():
    # 파일 목록 별로 pdf 텍스트 리스트에 담기
    try:
        pdf_to_text_list = [convert_pdf_to_txt(
            HANDOUT_MINE_PATH+i) for i in file_list if i[-3:] == 'pdf']
    except:
        return None

    reg = re.compile('\d+\.\s.+')  # 정규식으로 목차 분류

    result = list(map(reg.findall, pdf_to_text_list))

    # pdf 페이지 별로 title가 한번씩 있어서 제거
    # for i in map(reg.findall, pdf_to_text_list):
    #     title = i[0]

    #     def inner(x):
    #         if x == title:
    #             return False
    #         else:
    #             return True

    #     result.append(list(filter(inner, i)))

    return result
