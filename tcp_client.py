# coding=utf-8

import socket

# # 创建socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 建立连接
# s.connect(('www.sina.com.cn', 80))
# # 发送数据
# s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# # 接收数据
# buffer = []
# while True:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = ''.join(buffer)
# header, html = data.split('\r\n\r\n',1)
# print header
# # 把接收的数据写入文件
# with open('media/html/sina.html', 'wb') as f:
#     f.write(html)


# 创建socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('127.0.0.1', 9999))
# 接收数据
print s.recv(1024)
for data in ['Michael', 'Tracy', 'Sarah']:
    # 发送数据:
    s.send(data)
    print s.recv(1024)
s.send('exit')
s.close()
