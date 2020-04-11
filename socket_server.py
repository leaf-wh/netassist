# -*- coding: utf-8 -*-
import socket
import struct
import binascii
from ctypes import create_string_buffer


class socket_server:
    #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock = socket.socket()
    # conn = ""
    # addr = ""

    def __init__(self):
        self.sock = socket.socket()
        self.conn = ""
        self.addr = ""

    def initport(self, address, port):
        temp = (address, int(port))
        self.sock.bind(temp)
        print('connect success!')
        self.sock.listen(3)  # 限制排队的个数
        print('waiting......')
        self.conn, self.addr = self.sock.accept()

    def send(self, inp):
        buf = create_string_buffer(int(len(inp)/2))
        for i in range(0, int(len(inp)/2)):
            temp1 = inp[2*i:2*i+2]
            temp2 = int(temp1, 16)
            struct.pack_into("B", buf, i, temp2)
        self.conn.send(buf.raw)
        print('the send message is:%s' % inp)

    def recv(self):
        data = self.conn.recv(1024)
        data = binascii.hexlify(data)
        print('the receive message is:%s' % data)
        return str(data, 'utf8')
        # return int(data, 'utf8')

    def closeport(self):
        # 关闭套接字
        self.sock.close()
        # self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print('close socket!')
