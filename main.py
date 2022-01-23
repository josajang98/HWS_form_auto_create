import os
from datetime import datetime
from read_pdf import get_contents
today = datetime.today().strftime('%m%d')

# 본인 hws 폴더명으로 수정하기
HWS_NAME = 'HWS'

# 본인 handout_mine 폴더명으로 수정하기
HANDOUT_MINE_NAME = 'handout_mine'
HWM_PATH = f'../{HWS_NAME}/{today}/'

# 오늘 날짜로 폴더 생성


def mkdir_today():
    os.mkdir(HWM_PATH)

# 오늘 날짜로 md파일 생성


def touch_today_file():
    HW_name = today+'_homework.md'
    WS_name = today+'_workshop.md'
    name_list = [HW_name, WS_name]
    contents = get_contents()

    for idx, name in enumerate(name_list):
        f = open(HWM_PATH+name, 'w')

        # title 작성
        f.write(f'# {name[:-3]}\n')

        # 목차 작성
        for i in contents[idx]:
            f.write('\n\n## '+i)

        f.close()


mkdir_today()
touch_today_file()
