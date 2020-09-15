def ab_v(n1):
    print(abs(n1))
    # abs() is a predefined/inbuilt function in python
n1=int(input())
ab_v(n1)

# we can use another method also where pre defined "abs()" function is not used.

def ab_v2(n):
    if(n>=0):
        print(n)
    else:
        print(-n)

n=int(input())
ab_v2(n)