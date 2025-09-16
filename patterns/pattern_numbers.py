n=int(input("Enter the number of rows: "))
start=1 
for i in range(n,0,-1):
    for s in range(n-i):
        print(" ",end="")
    for j in range(1,i+1):
        if i == 1 or j == 1 or i == j or i == n:
            
           print(start+j-1,end=" ")
        else:
            print(" ",end=" ")
    print()