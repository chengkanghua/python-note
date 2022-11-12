




import unittest
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from HTMLTestRunner import HTMLTestRunner

class MyCase(unittest.TestCase):

    def test_case_01(self):
        self.assertTrue(1)

    def test_case_02(self):
        self.assertTrue("")

    def test_case_03(self):
        self.assertTrue(0)



def get_result():
    suite = unittest.makeSuite(testCaseClass=MyCase, prefix="test")

    file_path = './result.html'

    f = open(file_path, 'wb')

    HTMLTestRunner(
        stream=f,
        title="发邮件",
        description="将测试报告发邮件",
        verbosity=2
    ).run(suite)
    f.close()

    f1 = open(file_path, 'r', encoding='utf-8')

    return f1.read()

def send_mail():

    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器   # 勿动
    mail_user = "1206180814@qq.com"  # 用户名
    mail_pass = "hrcjrrkrdzdabaej"  # 口令
    # 设置收件人和发件人
    sender = '1206180814@qq.com'
    receivers = ['1206180814@qq.com', 'tingyuweilou@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 创建一个带附件的实例对象
    message = MIMEMultipart()

    # 邮件主题、收件人、发件人
    subject = '请查阅--s28的第一个测试报告'  # 邮件主题
    message['Subject'] = Header(subject, 'utf-8')
    message['From'] = Header("{}".format(sender), 'utf-8')  # 发件人
    message['To'] = Header("{}".format(';'.join(receivers)), 'utf-8')  # 收件人

    # 邮件正文内容
    send_content = 'hi man，你收到附件了吗？'
    content_obj = MIMEText(send_content, 'plain', 'utf-8')  # 第一个参数为邮件内容
    message.attach(content_obj)

    # 构造附件
    att = MIMEText(_text=send_content, _subtype='base64', _charset='utf-8')
    att["Content-Type"] = 'application/octet-stream'
    file_name = 'result.html'
    att["Content-Disposition"] = 'attachment; filename="{}"'.format(file_name)  # # filename 为邮件附件中显示什么名字
    message.attach(att)

    try:
        smtp_obj = smtplib.SMTP()
        smtp_obj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtp_obj.login(mail_user, mail_pass)
        smtp_obj.sendmail(sender, receivers, message.as_string())
        smtp_obj.quit()
        print("邮件发送成功")

    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


if __name__ == '__main__':
    send_mail()
    # get_result()


