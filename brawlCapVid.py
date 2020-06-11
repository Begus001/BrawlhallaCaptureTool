import keyboard
import time
import win32gui
from PIL import ImageGrab
import cv2
import os.path
import numpy as np

img_name = 0

if not os.path.isfile('path.txt'):
	print("Enter video path:")
	path = input()
	file = open('path.txt', 'x')
	file.write(path)
	file.close()
else:
	file = open('path.txt', 'r')
	path = file.read()
	file.close()

brawlWindow = 0

print("Trying to get Brawlhalla window...")
while brawlWindow == 0:
	try:
		brawlWindow = win32gui.FindWindow(None, r"Brawlhalla")
	except:
		pass

print("done!")

dim = win32gui.GetWindowRect(brawlWindow)

print("Press del to start capture")
keyboard.wait("del")

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(os.path.join(path, "vid.avi"), fourcc, 5.0, (dim[2] - dim[0], dim[3] - dim[1]))

while True:
	try:
		img = cv2.cvtColor(np.asarray(ImageGrab.grab(dim, all_screens=True)), cv2.COLOR_RGB2BGR)
		
		out.write(img)
		
	except KeyboardInterrupt:
		out.release()
		cv2.destroyAllWindows()
		break
