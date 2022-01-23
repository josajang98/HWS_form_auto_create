import os
from datetime import datetime

today = datetime.today().strftime('%m%d')

HWS_NAME = 'HWS'
HANDOUT_MINE_NAME = 'handout_mine'
HWM_PATH = f'../{HWS_NAME}/{today}/'
HANDOUT_MINE_PATH = f'../{HANDOUT_MINE_NAME}/{today}/hws/python_04_homework.pdf'


def mkdir_today():
    os.mkdir(HWM_PATH)


def touch_today_file():
    HW_name = today+'_homework.md'
    WS_name = today+'_workshop.md'

    f = open(HWM_PATH+HW_name, 'w')
    f.close()

    f = open(HWM_PATH+WS_name, 'w')
    f.close()
