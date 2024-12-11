import socket
import threading
import time
import random
import string

# 服务器地址和端口
SERVER_HOST = 's1.ddfkj.com'
SERVER_PORT = 19101

# 客户端线程函数
def client_thread_main(client_id, send_str):
    try:
        # 创建socket对象
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_HOST, SERVER_PORT))

        # 生成随机指令并发送
        message = send_str
        client_socket.sendall(message.encode('utf-8'))
        print(f"Client {client_id} sent: {message}")

        # 接收服务器响应（可选）
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Client {client_id} received 1: {response}")

        num_clients = 10
        for i in range(num_clients):

            time.sleep(10)
            message = send_str
            client_socket.sendall(message.encode('utf-8'))
            print(f"Client {client_id} resent: {message}")

            # 接收服务器响应（可选）
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Client {client_id} received {i+1}: {response}")


    except Exception as e:
        print(f"Client {client_id} encountered an error: {e}")
    finally:
        # 关闭socket连接
        client_socket.close()