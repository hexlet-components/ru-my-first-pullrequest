

i=1
txt = 'Привет. Здесь побывал @zafross.\nНе обижайтесь, мне просто нечего было делать :)\nhttps://github.com/zafross'
while True:
	name = 'Здесь был @zafross.' + str(i)
	with open(name, 'w') as f:
		f.write(txt)
	i+=1