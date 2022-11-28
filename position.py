import pyautogui, time

time.sleep(5)

while True:
	x, y = pyautogui.position()
	print(x, y)
	time.sleep(5);


# X
# 	mon 470
#	tues 585
#	weds 700
#	thurs 815
#	fir 930
#	sat 1045
#	sun 1160

# Y

	# 00:00 ~ 10:00 (scroll(500)) 
		# 00:00 ~ 00:15 (204) <197 - 227>
		# 00:15 ~ 00:30 (220)
		# 00:30 ~ 00:45 (234) <227 - 257>
		# 00:45 ~ 01:00 (250) <257 - 287>


	# 10:00 ~ 14:00 

	# 14:00 ~ 24:00 (scroll(-500))
