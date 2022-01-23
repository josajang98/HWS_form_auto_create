# HWS form auto create



### 매일 만드는 hws 폴더 양식 자동생성 해주게끔 만들어봤습니다



### 사용방법

#### 1. hws, handout 폴더가 있는 경로에 클론 받기



#### 2. pdfminer.six 설치

pdf 파일을 읽어오는 모듈입니다

```
pip install pdfminer.six
```



#### 3. 디렉토리명 상수 변경

상대경로로 파일 읽고 생성하기 때문에 본인 디렉토리명에 맞게 변경해줘야 해요

- main.py
  HWS_NAME, HANDOUT_MINE_NAME 상수 값을 바꿔주세요

- read_pdf.py

  HANDOUT_MINE_NAME 상수 값을 바꿔주세요



#### 3. 실행하기



### 오류 시 확인하기

예외 핸들링을 안했습니다 하하

#### 1. hws 폴더 안에 오늘 날짜 폴더가 생성되있는지 확인하기

#### 2. handout_mine 폴더 안에 오늘 날짜 폴더를 복사해왔는지 확인하기

