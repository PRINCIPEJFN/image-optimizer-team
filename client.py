HOST = "127.0.0.1"
PORT = 1255

N = 0

import socket
from PIL import Image

print("type: connect")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	
	
	
	
	CONNECTED = False
	
	
	while True:
		C = input()
		
		if "connect" in C:
			print("CONNECTING WITH ", HOST, PORT)
			s.connect((HOST, PORT))
			CONNECTED = True
		else:
			if CONNECTED:
				print("sending command")
				
				
				if C.startswith("EP"):
					CLEAN = C[2:]
					ARR = CLEAN.split(" ")
					print(ARR)
					if len(ARR) > 6 or len(ARR) <5:
						print("Err X y R g b")
					print("Pixel at ", ARR[0], ARR[1], ARR[2], ARR[3], ARR[4])
					s.sendall(C.encode("utf8"))
					data = s.recv(1024)
					print(data)
				if C.startswith("SF"):
					Frame_number = 0
					NUMBER = C.split(" ")
					
					s.sendall(C.encode("utf8"))
					print("Frame number selected", NUMBER)
					data = s.recv(1024)
					print(data)
				if C.startswith("AF"):
					print("ADICIONADO NOVO FRAME"
					)
					s.sendall(C.encode("utf8"))
				if C.startswith("SW"):
					s.sendall(C.encode("utf8"))
					print("REDEFINIDO TAMANHO")
				if C.startswith("SH"):
					s.sendall(C.encode("utf8"))
					print("REDEFINIDO TAMANHO")
			else:
				N = N +1
				print("NOT POSSIBLE TO CONNCT n  type connect #", N)