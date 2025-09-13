n=int(input())
start=0
for i in range(n,0,-1):
    i=int(i)
    start+=i 
num=start
for k in range(n,0,-1):
    for spaces in range(n-k):
        print(" ",end=" ")
    for j in range(k):
        print(num,end=" ")
        num-=1
    print()
        