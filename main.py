print("📚 Let's do easy division!")

a = int(input("Dividend(Big Number): "))
b = int(input("Divisor(Small number): "))

if b == 0:
    print("🙄 Can't divide by zero!")
else:
    count = 0 
    while a >= b:
        a = a - b
        count = count + 1

    print("🙂 Answer is:")
    print("Quotient =", count)
    print("remainder =", a)