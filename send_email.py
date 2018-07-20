# !/uer/bin/env python3
# coding=utf-8

import smtplib
import logging
import configparser
from email.mime.text import MIMEText
from email.utils import formataddr

LOGGER = logging.getLogger(__name__)
conf = configparser.ConfigParser()
conf.read("conf.ini")


def send_email(msg):
    mail_host = conf.get("EMAIL", "mail_host")
    rec_user = conf.get("EMAIL", "rec_user")
    mail_pass = conf.get("EMAIL", "mail_pass")
    sender = conf.get("EMAIL", "sender")

    message = MIMEText(msg, _subtype='html', _charset='utf-8')
    message['From'] = formataddr(["Python3", sender])
    message['To'] = formataddr(["路成督", rec_user])
    message['Subject'] = "**** 订单数据预警 from Python ****"

    try:
        smtp_obj = smtplib.SMTP(mail_host, 25)
        smtp_obj.login(sender, mail_pass)
        smtp_obj.sendmail(sender, [rec_user, ], message.as_string())
        LOGGER.info("邮件发送成功")
        smtp_obj.quit()
    except smtplib.SMTPException as e:
        LOGGER.error("Error: 无法发送邮件, {}".format(e))
        raise e


if __name__ == '__main__':
    send_email("123")
