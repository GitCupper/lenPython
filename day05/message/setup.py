from distutils.core import setup

setup(name="message",  # 包名
      version="1.0",  # 版本
      description="发送和接收消息模块",  # 描述信息
      long_description="完整的发送和接收消息模块",  # 完整描述信息
      author="David",  # 作者
      author_email="david@163.com",  # 作者邮箱
      url="www.github.com/GitCupper/",  # 主页
      py_modules=["day05.message.send_message",
                  "day05.message.receive_message"]
      )
