n=int(input())
for i in range(1,n+1):
    if i == n or i < 3:
       print((" "*(n-i)) +  "* "*i) 
    elif i >= 3 and i < n:
        print((" "*(n-i)) + "* " + ("  "*(i-2)) + "* ")