import os
from datetime import datetime

today = datetime.today().strftime('%m%d')

HWS_NAME = 'HWS'
HWM_PATH = f'../{HWS_NAME}/{today}/'


def mkdir_today():
    os.mkdir(HWM_PATH)
