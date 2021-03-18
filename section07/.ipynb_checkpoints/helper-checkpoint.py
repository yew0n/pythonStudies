#-*- coding: utf-8 -*-

import os.path #경로 정보를 취득하기 위한 모듈
from smtplib import SMTP #발송서버와 연동하기 위한 모듈
from email.mime.text import MIMEText #본문 구성 기능
from email.mime.application import MIMEApplication #파일을 Multipart 형식으로 변환
from email.mime.multipart import MIMEMultipart #파일을 본문에 추가하는 기능 제공

#메일발송 함수 정의
def sendmail(from_addr, to_addr, subject, content, files=[]):
    #----------------------------------
    #발송정보 설정
    #----------------------------------
    content_type = "html" #컨텐츠 형식(text or html)
    username = "syewon0128@gmail.com" #구글 메일 주소
    password = "ajssrajbbzlxxxmm" #구글 비밀번호
    smtp = 'smtp.gmail.com' #구글 발송 서버 주소(고정값)
    port = 587 #구글 발송 서버 포트(고정값)
    
    #----------------------------------
    # 발송 정보 구성
    #----------------------------------
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr

    #본문 설정
    msg.attach(MIMEText(content, content_type))
    
    #----------------------------------
    # 파일 첨부
    #----------------------------------
    #리스트 변수의 원소가 하나라도 존재할 경우 True
    if files:
        for f in files:
            #바이너리(b) 형식으로 읽기(r)
            with open(f, 'rb') as a_file:
                #전체 경로에서 파일의 이름만 추출
                basename = os.path.basename(f)
                #파일의 내용과 파일이름을 메일에 첨부할 형식으로 변환
                part = MIMEApplication(a_file.read(), Name=basename)

                #파일첨부
                part['Content-Disposition'] = 'attachment; filename="%s"' % basename
                msg.attach(part)

    #----------------------------------
    # 메일 보내기
    #----------------------------------
    mail = SMTP(smtp)
    #메일 서버 접속
    mail.ehlo()
    #메일 서버 연동 설정
    mail.starttls()
    #메일 서버 로그인
    mail.login(username, password)
    #메일 보내기
    mail.sendmail(from_addr, to_addr, msg.as_string())
    #메일 서버 접속 종료
    mail.quit()