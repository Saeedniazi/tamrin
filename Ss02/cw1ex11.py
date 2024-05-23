s1=input("1... ")
s2=input("2... ")

if s1.find(s2) or s2.find(s1):
    print("yes")
else: 
    print("no")

#finde if s1 and s2 is balance (s1 characters in s2 or s2 in s2 )