s=input("enter any thing... ")
digits=0
characters=0
symbols=0

for i in s:
    if 47< ord(i) <58:
        digits+=1
    elif 64< ord(i) <91 or 96< ord(i) < 123:
        characters+=1
    else:
        symbols+=1

print(digits,"digits")
print(characters, "characters")
print(symbols, "symbols")

# unicode 47ta58 digit
# unicode  64 ta 91 va 96 ta 123 character
# unicode els symbol
