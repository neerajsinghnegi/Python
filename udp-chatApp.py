import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

my_ip = "192.168.43.101"
my_port = 1234

s.bind((my_ip, my_port))

def get_data():
  while True:
    x = s.recvfrom(1024)
    print(x[0].decode())

def send_data():
  while True:
    server_ip = "192.168.43.162"
    server_port = 1234
    msg = input()
    msg = "Neeraj : " + msg
    s.sendto(msg.encode(), (server_ip, server_port))

get_data = threading.Thread(target = get_data)
send_data = threading.Thread(target = send_data)

get_data.start()
send_data.start()
