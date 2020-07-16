#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from emailSendLib import es


# 发送文本格式
# 发送文本 send_type 参数需要指定为 plain，因为 plain 为默认参数所以可以忽略
es.send('测试邮件(标题)', '测试邮件(内容) - 文本')

# 发送 html 格式
# 发送 html send_type 参数需要指定为 html
es.send('测试邮件(标题)', '<h2> 测试邮件(内容) - HTML </h2>', send_type='html')

# 发送带有 [附件] 的格式：
# 发送附件 send_type 参数需要指定为 annex
# file_path 参数为文件路径
es.send('测试邮件(标题)', '测试邮件(内容) - 附件', send_type='annex', file_path='./demo.zip')

# 发送带有 [图片] 的格式：
# 发送图片 send_type 参数需要指定为 image
# image_path 参数为图片路径
es.send('测试邮件(标题)', '测试邮件(内容) - 图片', send_type='image', image_path='./demo.jpg')
