igrade=input('')
try:
	igrade=float(igrade)
except:
	igrade=-1

if(0.0<=igrade<=1.0):
	if(igrade>=0.9):
		print("A")
	elif(igrade>=0.8):
		print("B")
	elif(igrade>=0.7):
		print("C")
	elif(igrade>=0.6):
		print("D")
	elif(igrade<0.6):
		print("F")
else:
	print("Wrong Input")