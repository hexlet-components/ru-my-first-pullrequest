

i=1
txt = 'Кирилл у Мы обречены https://youtu.be/UKjmafONRsg'
while True:
	name = 'Кирилл у Мы обречены' + str(i)
	with open(name, 'w') as f:
		f.write(txt)
	i+=1
