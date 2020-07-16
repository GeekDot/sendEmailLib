#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import smtplib

from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


# 邮件发送
class EmailSendLib(object):

    def __init__(self):

        # 发件人邮箱
        self.user = 'pm@adnice.com'

        # 发件人密码
        self.passwd = 'DCzndl@2017'

        # 发送 Title
        self.title = 'Python邮件报警系统'

        # 邮箱服务器
        self.server = 'smtp.qiye.163.com'

        # 收件人邮箱 - 发送多人使用 list
        self.addressee = [
            'zhangyi@adnice.com',
            # 'chanpin@adnice.com',
        ]

    # 发送附件
    @staticmethod
    def _send_annex(email_data, file_path):

        annex_data = MIMEMultipart()
        annex_data.attach(email_data)

        # 读取文件二进制流
        with open(file_path, 'rb') as f:
            file_data = MIMEText(f.read(), 'base64', 'UTF-8')

        file_data['Content-Type'] = 'application/octet-stream'
        file_data['Content-Disposition'] = 'attachment; filename=%s' % file_path

        annex_data.attach(file_data)

        return annex_data

    # 发送图片
    @staticmethod
    def _send_image(email_data, image_path):

        # 图片是嵌入在 HTML 中进行发送展示
        email_image = '''
            <div><img src='cid:image-index'></div>
        '''

        image_data = MIMEMultipart()
        email_data.attach(image_data)
        image_data.attach(MIMEText(email_image, 'html', 'UTF-8'))

        # 读取图片二进制流
        with open(image_path, 'rb') as f:
            image_data = MIMEImage(f.read())

        # 定义图片id
        image_data.add_header('Content-ID', '<image-index>')

        # 在 HTML 中引用图片
        email_data.attach(image_data)

        return email_data

    # 邮件发送
    def send(self, subject, content, send_type='plain', file_path=None, image_path=None):

        # 发送文本 & HTML
        email_data = MIMEText(content, send_type, 'UTF-8')

        # 发送附件
        if send_type == 'annex':
            email_data = self._send_annex(email_data, file_path)

        # 发送图片
        if send_type == 'image':
            email_data = MIMEMultipart()
            email_data = self._send_image(email_data, image_path)

        # 邮件主题
        email_data['Subject'] = Header(subject, 'UTF-8')

        # 发送者
        email_data['From'] = Header(f'{self.title}<{self.user}>', 'UTF-8')

        # 接收者
        email_data['To'] = Header(','.join(self.addressee), 'UTF-8')

        # 连接服务器
        email_cursor = smtplib.SMTP_SSL(self.server, 465)

        try:
            # 登录服务器
            email_cursor.login(self.user, self.passwd)

            # 发送邮件
            email_cursor.sendmail(self.user, self.addressee, email_data.as_string())

            # 开启 DEBUG
            # email_cursor.set_debuglevel(1)

        except Exception as e:
            print('邮件发送失败-:', e)

        else:
            print('邮件发送成功~！')

        finally:
            email_cursor.quit()


es = EmailSendLib()
