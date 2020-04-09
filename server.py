#! /usr/bin/python3
# -*- coding: cp866 -*-


import socket, os
def main():
	ip = "0.0.0.0"
	port = 4444

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((ip, port))
	print(f'listening {ip}:{port}')
	s.listen(1)
	clientsocket, address = s.accept()

	try:
		while True:
			full_msg = ''
			while True:
				msg  = clientsocket.recv(1024)
				full_msg += msg.decode('cp866');
				if full_msg[-11:] == "{<END MSG>}":
					break
			print(full_msg[:-11], end='> ')
			full_msg = input() + "{<END MSG>}"
			if full_msg[:-11] == "clear" or full_msg[:-11] == "cls":
				os.system(full_msg[:-11])
			if full_msg[:-11] == "exit":
				print("Exiting...")
				clientsocket.send("exit{<END MSG>}".encode('cp866'))
				s.close()
				clientsocket.close()
				return 0
			clientsocket.send(full_msg.encode('cp866'))
	except:
		print("Exiting...")
		clientsocket.send("exit{<END MSG>}".encode('cp866'))
		s.close()
		clientsocket.close()
		return 0


if __name__ == '__main__':
	main()
