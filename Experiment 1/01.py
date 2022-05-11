principle=1000 
rate=10.25
time=5 
Amount = principle * (pow((1 + rate / 100), time)) 
CI = Amount - principle 
print("Compound interest is", CI) 
