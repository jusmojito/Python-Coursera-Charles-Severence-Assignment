hours=input("Enter Number of Hours")
rate=input("Enter Rate per Hour")

try:
	hours=float(hours)
	rate=float(rate)
except:
	hours=-1
	rate=-1
grosspay=0
if(0<=hours<=40):
	grosspay=hours*rate
	print(grosspay)
elif(hours>40):
	grosspay=(hours-40)*1.5*rate + 40*rate
	print(grosspay)
else:
	print("Wrong Input")
