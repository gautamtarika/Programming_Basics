tc= int(input())
while(tc>0):
    num=[]
    for i in range(3):
        num.append(int(input())) 
    num.sort()
    print(num[-2])
    tc=tc-1