largest_yet= None
smallest_yet= None
inp=0
number=0
while(inp!="done"):
    inp=input("Enter No.")
    if(inp!="done"):
	    try:
	        number=int(inp)
	    except:
	        print("Invalid input")
	    if(largest_yet is None):
	        largest_yet=number
	        smallest_yet=number
	    elif(largest_yet<number):
	        largest_yet=number
	    elif(smallest_yet>number):
	    	smallest_yet=number

print("Maximum is",largest_yet)
print("Minimum is",smallest_yet)