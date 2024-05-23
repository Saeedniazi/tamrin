#print ("سلام دنیا")

bool_variable=True
int_variable=1
float_variable=3.14
complex_variable=2+3.3j

print(bool(int_variable))
 #if input variable has any value exept 0 or 0.0 or *** bool() will return true els fals

print(float(bool_variable))
print (int(bool_variable))
#......

#coverting numbers to str 
#we can convert all numbers to str without error
str(int_variable)
str(float_variable)
str(bool_variable)

#we can convert strings to number if str only contains number
print(float(5.3))

#جنس اینپوت همیشه استرینگه input-->string

x=input()
y=input()
print(x=y) #--> xy

x = int(input("please enter number only x: "))
y = int(input("please enter number only y: "))
print(x+y) #-->x+y

a= 4>5
print(a)
b=5<=9
print(b)
c= 5==5
print(c)
#type(a,b,c)--> bool
