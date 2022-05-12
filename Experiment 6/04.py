for num in range(10,20):
    check = 0
    for i in range(2,num):    
        if num%i == 0:         
            j=num/i
            check = 1
            break
    if check == 0:
        print(num, " is prime")
