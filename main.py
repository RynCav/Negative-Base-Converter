#Used for values after nine
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Converts a base 10 integer to a negative base integer
def neg_int(number, base):
    number *= -1
    remainder = ""
    while number != 0:
        if abs(number % base) >= 10:
            remainder += alphabet[abs(int(number) % base) - 10]
        else:
            remainder += str(abs(number % base))
        number = (number - (number % base)) // base
    return remainder[::-1]

#Converts a negative base fraction to a base 10 fraction
def pos_frac(number, base):
    new = ""
    while len(new) < 12:
        number *= base
        if int(number) >= 10:
            new += str(alphabet[int(int(number) - 10)])
        else:
            new += str(int(int(number)))
        if number >= 1:
            number %= 1
    return new

#Converts a negative base integer to a base 10 integer
def pos_dec(number, base):
    new = ""
    while number != 0:
        if (number % base) >= 10:
            new += alphabet[((number % base) - 10)]
        else:
            new += str(number % base)
        number = int(number / base)
    return new[::-1]

#calculates the number that is used to find the link between bases
def convert_dec(number, base):
    power = 0
    new = 0
    negative = False
    if "-" in number:
        number = number.replace("-", "")
        negative = True
    for i in number:
        if i in alphabet:
            i =alphabet.index(i) + 10
        new += int(i) * (base ** power)
        power += 1
    if negative:
        new *= -1
    return new

#converts base 10 to negative integer
def int_neg_base(number, base):
    new = 0
    x = 0
    for i in str(number):
        if i in alphabet:
            i = (alphabet.index(i) + 10)
        new += int(i) * (base ** x)
        x += 1
    return new

#converts base 10 to negative fraction
def frac_neg_base(number, base):
    new = 0
    x = -1
    for i in str(number):
        if i in alphabet:
            i = (alphabet.index(i) + 10)
        new += int(i) * (base ** x)
        x -= 1
    return new

#places the radix point in the number
def get_number(number, base, goal):
    for i in range(0, len(self)):
        if int_neg_base(self[:i][::-1], base) + frac_neg_base(number[i:], base) == goal:
            return number[:i] + "." + number[i:]

#Gets the new negative base number
def new_number(number, base):
    new = str(pos_dec(abs(int(number)), abs(base)) + pos_frac(abs(number) % 1, abs(base)))[::-1]
    if self < 0:
        new = convert_dec("-" + new, abs(base))
    else:
        new = convert_dec(new, abs(base))
    return new

#Converts base 10 fractional numbers to a negative base
def neg_frac(number, base):
    final_number = get_number(neg_int(new_number(number, base), base), base, number)
    return final_number

#Gets the user input and prints the result to the screen
input  = neg_frac(float(input("Goal: ")), int(input("Base: ")))
print(input)
