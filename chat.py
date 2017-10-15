# -*- coding: utf-8 -*-
import socket


def get_5():
	sock.send('get_5\0'.encode())
	data=sock.recv(1024).decode()
	print(data)

def get_all():
	sock.send('getal\0'.encode())
	 #FAIL. I don't know how to do it correctly
	data=sock.recv(10000).decode()
	print(data)

def send_mess():
	sock.send('sendm\0'.encode())
	print("Введите сообщение:\n")
	sock.send(((input())+"\0").encode())


works=True
sock = socket.socket()
sock.connect(('95.165.172.150',11111))
print("Введите имя")
name = input()
sock.send(("login\0").encode())
sock.send((name+"\0").encode())
while works:
	print('выберите действите:\n'
	+'1-получить последние 5 сообщений\n'
	+'2-получить все сообщения\n'
	+'3-отправить собщение\n'
	+'0-выход')
	str_ = input()
	if str_=="0":
		works=False
	if str_=="1":
		get_5()
	if str_=="2":
		get_all()
	if str_=="3":
		send_mess()
		get_5()
