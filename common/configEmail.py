import smtplib
from email.mime.text import MIMEText
from common.log import logger


class SendEmail(object):
    def __init__(self, subject, mail_host, mail_user, mail_pass, sender, receivers, content):
        self.subject = subject
        self.mail_host = mail_host
        self.mail_user = mail_user
        self.mail_pass = mail_pass
        self.sender = sender
        self.receivers = receivers
        self.content = content

    def sendemail(self):
        message = MIMEText(self.content, 'html', 'utf-8')  # 邮件内容
        message['Subject'] = self.subject  # 标题
        message['From'] = self.sender  # 发送人
        message['To'] = self.receivers  # 收件人

        # 登陆尝试发送邮件
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, 25)  # 连接到服务器
            smtpObj.login(self.mail_user, self.mail_pass)  # 登录到服务器
            smtpObj.sendmail(self.sender, self.receivers, message.as_string())  # 发送信息
            smtpObj.quit()  # 退出
            logger.info('send to %s email success' % self.receivers)
        except smtplib.SMTPException as e:
            logger.debug("send email fail", e)


if __name__ == '__main__':
    print("ok")

    # # 读取config中的email配置
    # readconfig = ReadConfig()
    # subject = readconfig.get_email("subject")
    # mail_host = readconfig.get_email("mail_host")
    # mail_user = readconfig.get_email("mail_user")
    # mail_pass = readconfig.get_email("mail_pass")
    # sender = readconfig.get_email("sender")
    # receivers = readconfig.get_email("receivers")
    #
    # #打开测试报告文件
    # data = open('/Users/dongyue/Documents/framework/result/report/report.html','rb').read()
    # c = SendEmail(subject,mail_host,mail_user,mail_pass,sender,receivers,data)
    # c.sendemail()
    #

