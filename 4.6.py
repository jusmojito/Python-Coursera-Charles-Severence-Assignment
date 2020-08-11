def computepay(h,r):
	grosspay=0
	if(0<=h<=40):
		grosspay=h*r
		return grosspay
	elif(h>40):
		grosspay=(h-40)*1.5*r + 40*r
		return grosspay
	else:
		return "Wrong Input"

hours=input("Enter Number of Hours")
rate=input("Enter Rate per Hour")

try:
	hours=float(hours)
	rate=float(rate)
except:
	hours=-1
	rate=-1

print(computepay(hours,rate))
