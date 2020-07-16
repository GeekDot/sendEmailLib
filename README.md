<h2 align= center> emailSendLib 邮件发送库 </h2>

<h5 align=right> 张懿 </h5>
<p align=right> 2019-09-11 </p>

### 一、概述

`emailSendLib` 是一个邮件发送库，依赖 `smtplib`、`email` 库

下面是对 `emailSendLib` 的详解，如想快速使用，请移步 `demo.py` 模块，里面有 `emailSendLib` 的使用 `demo`

### 二、安装

`emailSendLib` 是以源码的方式呈现，使用的时候直接导入即可

	from emailSendLib import es
    
### 三、使用

`emailSendLib` 所有的功能都是 `es` 的方法，`emailSendLib` 包括 `4` 类功能，各功能之间互斥，暂时不支持同时 `4` 种格式发送

1. 发送文本格式

2. 发送 `html` 格式

3. 发送带有 `[附件]` 的格式

4. 发送带有 `[图片]` 的格式

#### 1. 发送文本格式

发送文本，`send_type` 参数需要指定为 `plain`，因为 `plain` 为默认参数所以可以忽略

	es.send('测试邮件(标题)', '测试邮件(内容) - 文本')
	
#### 2. 发送 `html` 格式

发送 `html`，`send_type` 参数需要指定为 `html`
	
	es.send('测试邮件(标题)', '<h2> 测试邮件(内容) - HTML </h2>', send_type='html')

#### 3. 发送带有 `[附件]` 的格式

发送附件， `send_type` 参数需要指定为 `annex`，`file_path` 参数为文件路径

	es.send('测试邮件(标题)', '测试邮件(内容) - 附件', send_type='annex', file_path='./demo.zip')

#### 4. 发送带有 `[图片]` 的格式

发送图片 `send_type` 参数需要指定为 image，image_path 参数为图片路径

	es.send('测试邮件(标题)', '测试邮件(内容) - 图片', send_type='image', image_path='./demo.jpg')