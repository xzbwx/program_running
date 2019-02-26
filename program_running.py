import os
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '发送人的邮箱'
receivers = ['接收人的邮箱'] 

message = MIMEText('Python 邮件发送...您的程序已经完成', 'plain', 'utf-8')
message['From'] = Header("你的电脑", 'utf-8')   # 发送者
message['To'] =  Header("qq邮箱", 'utf-8')        # 接收者

subject = 'Python process测试'
message['Subject'] = Header(subject, 'utf-8')


def isRunning(process_name) :
    try:
        print('tasklist | findstr '+process_name)
        process=len(os.popen('tasklist | findstr '+process_name).readlines())
        print(process)
        if process >=1 :
            return True
        else:
            return False
    except:
        print("程序错误")
        return False

def sendemail():
    try:
        server = smtplib.SMTP('smtp.qq.com',25)
        server.ehlo()
        server.starttls()
        server.login(sender , "你的密码")
        text = message.as_string()
        server.sendmail(sender, receivers, text)
        server.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error")

if __name__=="__main__":
    flag=True
    while flag:
        flag = isRunning("程序的名字")
        print(flag)
        if flag == False:
            sendemail()
        time.sleep(60)##每隔60s进行检查
