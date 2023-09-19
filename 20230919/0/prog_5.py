while str := input():
	if eval(str)==13: break
	elif eval(str)%2 == 0:
		print(str)
else: print("HAPPY, no 13!")
