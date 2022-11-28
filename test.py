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
		

print(x_axis_gen(39))