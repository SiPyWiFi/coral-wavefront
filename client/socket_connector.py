import cv2
import time
from PIL import Image
# Import socket module 
import socket			 


# load camera modul
cap = cv2.VideoCapture(0)
cap.isOpened()

# Create a socket object 
s = socket.socket()		 

# Define the port on which you want to connect 
port = 12346				

# connect to the server on local computer 
s.connect(('192.168.178.40', port)) 

# receive data from the server 
print(s.recv(1024))

# send data to server
s.send(str.encode("Client aquire image..."))
cap.read()
ret, frame = cap.read()

if ret:
    cv2_im = frame
    cv2_im_rgb = cv2.cvtColor(cv2_im, cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(cv2_im_rgb)
    pil_im.save("snap.png", "png")
    pil_im_byn = pil_im.tobytes()
    print(len(pil_im_byn))
    buffer_size = 1024
    for loop in range(921600//buffer_size):
        start_buffer = loop*buffer_size
        end_buffer = (loop+1)*buffer_size
        s.send(pil_im_byn[start_buffer:end_buffer])
        s.recv(10)
    print(loop)
else:
    s.send(str.encode("ERROR"))
time.sleep(1)
s.send(str.encode(r'image sended ...'))

# close the connection 
cap.release()
s.close()	
