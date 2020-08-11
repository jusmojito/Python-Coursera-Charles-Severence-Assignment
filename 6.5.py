text = "X-DSPAM-Confidence:    0.8475";
pos=text.find("0")
number=text[pos:pos+6]
number=float(number)
print(number)