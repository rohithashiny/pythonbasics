m=int(input())
n=int(input())
found = 0
for i in range(m,n+1):
    if i > 1:
       count=0 
       for j in range(2,i):
        
            if i %  j == 0:
               count+=1  
        
       if count == 0:
          print(i,end=" ")
          found = 1 
if found == 0:
    print("No Prime Numbers Found")

