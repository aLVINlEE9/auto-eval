import time
import pyautogui
import webbrowser
import const


# time.sleep(3)

a = input("input(day, start-time, end-time)[ex. FRI, 10:00, 10:30]>> ")
day = a[:3]
start_time = a[5:10]
end_time = a[12:17]
print(day, start_time,end_time)

url = 'https://profile.intra.42.fr/'
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
webbrowser.get(chrome_path).open(url)

time.sleep(2)

pyautogui.moveTo(1340, 140)
pyautogui.click() # profile

time.sleep(1)
pyautogui.moveTo(1340, 188)
pyautogui.click() # Manage slot

time.sleep(1)
pyautogui.scroll(-500) # scroll down

pyautogui.moveTo(800, 500)

def set_y_axis(day):
	if day == "MON":
		return const.Y_MON
	elif day == "TUE":
		return const.Y_TUE
	elif day == "WED":
		return const.Y_WED
	elif day == "THU":
		return const.Y_THU
	elif day == "FRI":
		return const.Y_FRI
	elif day == "SAT":
		return const.Y_SAT
	elif day == "SUN":
		return const.Y_SUN

def get_idx(time, set):
	i = 0
	if set == 0:
		i = int(time[:2]) * 4 + (int(time[3:]) / 15)
	elif set == 1:
		i = (int(time[:2]) * 4 + (int(time[3:]) / 15)) - 24
	elif set == 2:
		i = (int(time[:2]) * 4 + (int(time[3:]) / 15)) - 54
	print(i)
	return i

def x_axis_gen(set):
	i = 0
	a = 204
	b = 220
	while True:
		if i == set:
			return a
		a += 30
		i += 1
		if i == set:
			return b
		b += 30
		i += 1

def set_x_axis(start_time, end_time):
	s = 0
	e = 0
	if end_time <= "10:00":
		pyautogui.scroll(500)
		time.sleep(1)
		s = x_axis_gen(get_idx(start_time, 0))
		e = x_axis_gen(get_idx(end_time, 0) - 1)
	elif end_time <= "14:00":
		time.sleep(1)
		s = x_axis_gen(get_idx(start_time, 1))
		e = x_axis_gen(get_idx(end_time, 1) - 1)
	elif end_time <= "24:00":
		pyautogui.scroll(-500)
		time.sleep(1)
		s = x_axis_gen(get_idx(start_time, 2))
		e = x_axis_gen(get_idx(end_time, 2) - 1)
	return s, e



y_axis = set_y_axis(day)
x_axis_s, x_axis_e = set_x_axis(start_time, end_time)
print(x_axis_s, x_axis_e)




# pyautogui.moveTo(1160, 500)

pyautogui.moveTo(y_axis, x_axis_s)
pyautogui.mouseDown(button='left')
pyautogui.moveTo(y_axis, x_axis_e)
pyautogui.click()














