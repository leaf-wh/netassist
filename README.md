# netassist
网页版网口调试工具

# 2020/04/11
从春节假期的最后几天开始，尝试做了一个web版的网口调试工具，初衷是学习js、flask的基础知识，并看一看selenium能否在工作中使用。

写的过程中遇到过下列问题：

1、ajax只能由前台向后台发消息，而网口调试工具可能收到被测软件主动发过来的消息。
  解决办法是使用websocket技术，即python中的socketio来实现后台主动向前台推送
  
2、发送和接收的消息显示在web的两个文本框中，python取值时候默认当成string，而实际使用过程中，希望能把填入的内容当做hex格式报文直接发送。
  解决办法是接收时使用binascii.hexlify(data)，将收到的string转化为hex
  发送时使用int(x,16)逐字节转化发送内容后，使用struct.pack_into()，将发送内容转化为hex
  
目前这个版本还很原始，主要体现在使用的sock是同步模式，收发不能同时进行，且线程单一，不过应该足够我用于接下来selenium的学习了吧
