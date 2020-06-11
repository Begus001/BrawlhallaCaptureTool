import keyboard
import time
import win32gui
from PIL import ImageGrab
import os.path

img_name = 0

if not os.path.isfile('path.txt'):
	print("Enter image path:")
	path = input()
	file = open('path.txt', 'x')
	file.write(path)
	file.close()
else:
	file = open('path.txt', 'r')
	path = file.read()
	file.close()
	
brawlWindow = win32gui.FindWindow(None, r'Brawlhalla')

print('Press del to start capture')
keyboard.wait('del')

while True:
	try:
		dim = win32gui.GetWindowRect(brawlWindow)
		img = ImageGrab.grab(dim, include_layered_windows=True, all_screens=True)
		
		while os.path.isfile(path + '\\' + str(img_name) + '.png'):
			img_name += 1
		
		img.save(path + '\\' + str(img_name) + '.png')
		print('Image "{0}.png" saved to {1}'.format(str(img_name), path))
		
		time.sleep(1)
	except KeyboardInterrupt:
		exit()
