# HWS form auto create



## 매일 만드는 hws 폴더 양식 자동생성 해주게끔 만들어봤습니다



## 사용방법

### 1. hws, handout 폴더가 있는 경로에 클론 받기
![image](https://user-images.githubusercontent.com/77478240/150665019-71236527-9148-4d38-bfbc-34bb61d39aca.png)

상대경로로 파일이랑 폴더를 읽기 때문에 경로를 맞춰줘야되요





### 2. pdfminer.six 설치

pdf 파일을 읽어오는 모듈입니다

클론 받아서 생성된 HWS_form_auto_create 폴더에서 git bash 열어서 명령어 입력 해주기

```
pip install pdfminer.six
```



### 3. vscode를 열어서 디렉토리명 상수 변경

상대경로로 파일 읽고 생성하기 때문에 본인 디렉토리명에 맞게 변경해줘야 해요

- main.py 파일을 vscode로 열어서 수정 후 저장해주기

  HWS_NAME, HANDOUT_MINE_NAME 상수 값을 바꿔주세요
  디렉토리명에 맞게 바꿔주시면 됩니다
  ![image](https://user-images.githubusercontent.com/77478240/150665037-08801fee-7858-4881-876a-80e44a15c388.png)


- read_pdf.py 파일을 vscode로 열어서 수정 후 저장해주기

  HANDOUT_MINE_NAME 상수 값을 바꿔주세요
  디렉토리명에 맞게 바꿔주시면 됩니다
  ![image](https://user-images.githubusercontent.com/77478240/150665073-8d83665e-d475-4168-840e-90b6fa38d35a.png)


### 4. 실행하기
  1. 교수님이 오늘 올려주신 과제를 handsout_notpush에 저장
  2. handsout_notpush에서 handsout_mine 으로 오늘 과제 복사
  3. 클론 받아서 생성된 HWS_form_auto_create 폴더에서 git bash 열어서 명령어 입력 해주기


  
  ```
  python main.py
  ```
  ![image](https://user-images.githubusercontent.com/77478240/150665256-fd5c7487-7977-4c0c-8f57-c6c261792797.png)

  정상적으로 실행되면 hws 폴더 안에 오늘 날짜 폴더가 생성되고 그 안에 md에 목차가 쓰여져서 생성되요
  
  오늘 날짜 pdf의 목차가 자동으로 md파일에 써져요! 이게 뽀인트
  ![image](https://user-images.githubusercontent.com/77478240/150665121-52a6ab64-9e44-4783-9aaa-e7b70e758e03.png)



## 오류 시 확인하기

예외 핸들링을 안했습니다 하하

### 1. hws 폴더 안에 오늘 날짜 폴더가 생성되있는지 확인하기

### 2. handout_mine 폴더 안에 오늘 날짜 폴더를 복사해왔는지 확인하기

