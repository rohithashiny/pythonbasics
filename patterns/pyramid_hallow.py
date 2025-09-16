n=int(input())
for i in range(1,n+1):
    for s in range(n-i):
        print("",end=" ")
    for j in range(1,i+1):
        if i == j or i == 1 or j == 1 or i == n:
            
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()