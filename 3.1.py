hours=float(input("Enter Number of Hours"))
rate=float(input("Enter Rate per Hour"))
grosspay=0
if(0<=hours<=40):
	grosspay=hours*rate
elif(hours>40):
	grosspay=(hours-40)*1.5*rate + 40*rate
else:
	print("Wrong Input")
print(grosspay)