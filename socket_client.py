# -*- coding: utf-8 -*-
import socket
import struct
import binascii
from ctypes import create_string_buffer


class socket_client:
    #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #sock = socket.socket()

    def __init__(self):
        self.sock = socket.socket()

    def initport(self, address, port):
        temp = (address, int(port))
        self.sock.connect(temp)
        print('connect success!')

    def send(self, inp):
        buf = create_string_buffer(int(len(inp)/2))
        for i in range(0, int(len(inp)/2)):
            temp1 = inp[2*i:2*i+2]
            temp2 = int(temp1, 16)
            struct.pack_into("B", buf, i, temp2)
        self.sock.send(buf.raw)

    def recv(self):
        # while True:
        # 接收数据
        data = self.sock.recv(1024)
        data = binascii.hexlify(data)
        # 打印接收到的数据
        print('the receive message is:%s' % data)
        return str(data, 'utf8')
        # return int(data, 'utf8')

    def closeport(self):
        # 关闭套接字
        self.sock.close()
        # self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print('close socket!')
