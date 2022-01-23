import os
from datetime import datetime
from read_pdf import get_contents
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
    name_list = [HW_name, WS_name]
    contents = get_contents()

    for idx, name in enumerate(name_list):
        f = open(HWM_PATH+name, 'w')

        f.write(f'# {name[:-3]}\n')

        for i in contents[idx]:
            f.write('\n\n## '+i)
        f.close()


mkdir_today()
touch_today_file()
