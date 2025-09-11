s=input()
rev=""
length=len(s)
for i in range(length):
    w=s[i]
    rev= w+rev 
if rev.upper() == s.upper():
    print("Palindrome")
else:
    print("Not a Palindrome")
