import os
import smtplib
import unittest
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText


def send_mail(path):
    file = open(path, 'rb')
    msg = file.read()
    mail_msg = MIMEText(msg, 'html', 'utf-8')
    # MIMEText(msg, _subtype='html', "utf-8")
    mail_msg['Subject'] = '自动化测试报告'
    mail_msg['From'] = 'bwftest126@126.com'
    mail_msg['To'] = 'changchengxc@126.com'
    smtp = smtplib.SMTP()
    smtp.connect('smtp.126.com')
    smtp.login('bwftest126@126.com', 'abc123asd654')
    smtp.send_message(mail_msg, 'bwftest126@126.com', 'changchengxc@126.com')
    smtp.quit()



if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover(".","*.py")
    # unittest.TextTestRunner().run(suite)
    path = os.path.dirname(__file__) + "/report.html"
    file = open(path,'wb')
    HTMLTestRunner(stream=file, verbosity=1, title=None, description=None).run(suite)
    file.close()
    send_mail(path)