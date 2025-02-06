print("Multiples of a Number")
print("Give me two numbers. First number is your base, and the second is your 'up-to' limit")

base = int(input("Multiples of: "))
print("Perfect! %s is your base" % base)

limit = int(input("Enter your limit: "))
print("I will show multiples of %s up to %i" % (base , limit))

for multiples in range(base, limit + 1,base):
    if(multiples % base == 0):
        print(multiples)