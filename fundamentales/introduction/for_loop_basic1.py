#1basic
for i in range(151):
    print(i)
#multiples of five
for i in range(1001):
    if(i%5==0):
        print(i)
#couting the dojo way 
for i in range(1,101):
    if(i%10==0):
        print("coding dojo")
    elif(i%5==0):
        print("coding")
    else:
        print(i)
#Whoa. That Sucker's Huge
sum=0
for i in range(500000):
    sum=sum+i
print(sum)
#Countdown by Fours
for i in range (2018,0,-4):
    print(i)
#Flexible Counter
lowNum=2
highNum=9
mult=3
for i in range(lowNum,highNum+1):
    if (i%mult==0):
        print(i)
        
            