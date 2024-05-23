print("if you want to covert Fahrenheit to Celsius type ..1.. otherwise type 2")
h=int(input())

if h==1 :

    f=int(input("enter Celsius temp: "))
    f=f*1.8+32
    print(f),print("F")


else:

    f=int(input("enter Fahrenheit temp: "))
    k=f-32
    c=k*5/9
    print("f="); print(c); print("c")

#F and C converting