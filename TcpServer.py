from socket import *
import time

HOST = ''
PORT = 9999
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)   #创建套接字
tcpSerSock.bind(ADDR)   #绑定IP和端口
tcpSerSock.listen(5)    #监听端口，最多5人排队

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()    #建立连接
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print("接收到：%s" %data.decode())
        content = "<ISAIP,YES>"
        tcpCliSock.send(content.encode("utf-8"))

    tcpCliSock.close()

tcpSerSock.close()