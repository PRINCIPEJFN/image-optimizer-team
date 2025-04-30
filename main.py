from PIL import Image

import socket

 
# SERVER

HOST = "127.0.0.1"
PORT = 1255

print("RUNNING AT ", HOST, PORT)

#print(img.format)  # Output: JPEG
#print(img.size)    # Output: (width, height)
#print(img.mode)    # Output: RGB or other mode
   
   #   resized_img = img.resize((new_width, new_height))
   
   #   rotated_img = img.rotate(angle)  # Counter-clockwise
   
   #   cropped_img = img.crop((left, top, right, bottom))  # Coordinates in pixels

if False:
	for i in range(40):
	 	 None
  	 #img.putpixel((i,i), (120,0,0))
   

DW = 500
DH = 500
NUMBER = str(0)

def A():
	global DW
	global DH
	global NUMBER
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		  s.bind((HOST, PORT))
		  s.listen()
		  conn, addr = s.accept()
		  print("accepted ", conn)
		  while data := conn.recv(1024):
		  	print("recived", str(data)[2:-1])
		  	if str(data)[2:-1].startswith("SF"):
		  		print("Selcting frame with commans -> ", data)
		  		NUMBER = str(data)[3:-1]
		  	elif str(data)[2:-1].startswith("AF"):
				  im = PIL.Image.new(mode = "RGB", size = (DW, DH), color = (153, 153, 255))
				  im.save("/storage/emulated/0/Download/film/FRAME"+ NUMBER+ ".jpeg")
				  print("FRAME ADD UP")
		  	elif str(data)[2:-1].startswith("SW"):
		  		DW = int(str(data)[2:-1].split(" ")[1])
		  	elif str(data)[2:-1].startswith("SH"):
		  		DH = int(str(data)[2:-1].split(" ")[1])
		  	elif str(data)[2:-1].startswith("EP"):
		  		ARR = str(data)[5:-1].split(" ")
		  		print("Editing pixel at Frame N° ")
		  		img = Image.open("/storage/emulated/0/Download/film/FRAME"+ NUMBER+ ".jpeg")
		  		
		  		print("setting", ARR)
		  		for i in range(1):
		  			img.putpixel((int(ARR[0]), int(ARR[1])), (int(ARR[2]), int(ARR[3]), int(ARR[3])))
		  		img.save("/storage/emulated/0/Download/film/FRAME" + NUMBER + ".jpeg")  # Saves as PNG format

		  	else:
		  		print("command not found")
		  
#while True:
while True:
	A()

print("start to end.")