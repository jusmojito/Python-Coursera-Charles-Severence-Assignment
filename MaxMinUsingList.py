number=list()
inp=0
while inp!='done':
    inp=input("Enter a number: ")
    if inp=='done':
        continue
    number.append(float(inp))

print('Maximum:',max(number))
print('Minimum:',min(number))
