import string


# METHOD
symbols = string.digits + string.ascii_uppercase

# HELPER FUNCTIONS..
def _int_from_base(number, original_base):
    return int(number, original_base)


def _int_to_base(number, new_base):
    sign = -1 if number < 0 else 1
    number *= sign
    ans = ''
    while number:
        ans += symbols[number % new_base]
        number //= new_base
    if sign == -1:
        ans += '-'
    return ans[::-1]


def _fractional_from_base(number, original_base):
    ans = 0
    for i in xrange(1, len(number)+1):
        ans += symbols.index(number[i-1]) * original_base**-i
    return ans


def _fractional_to_base(number, new_base, precision=5):
    ans = ''
    for i in xrange(precision):
        tmp = number * new_base
        itmp = int(tmp)
        ans += str(symbols[itmp])
        number = tmp - itmp
    return ans
    
    
def convert(number, original_base, new_base, precision=None):

    #from -- Original_Base
    integral, point, fractional = number.strip().partition('.')
    num = int(integral + fractional, original_base) * original_base ** -len(fractional)

    #to -- New_Base
    precision = len(fractional) if precision is None else precision
    s = _int_to_base(int(round(num / new_base ** -precision)), new_base)
    if precision:
        return s[:-precision] + '.' + s[-precision:]
    else:
        return s
        
        

print("     ------***------------***------")
print("*** WELCOME TO BASE-TO-BASE CONVERTER ***")
print("     ------***------------***------\n")


# DRIVER FUNCTION
def main():
    t = str(input("\n\nENTER YOUR INPUT NUMBER[IN ANY BASE] --\t"))
    
    try:
        c1 = int(input("YOUR INPUT BASE ?? [Eg: 10, 12, 2, 16 etc] --\t"))
    except:
        print("ENTER THE BASE NUMBER CORRECTLY!!")
        main()
    
    try:
        c2 = int(input("YOUR OUTPUT[DESIRED] BASE ?? [Eg: 64, 12, 3, 10 etc] --\t"))
    except:
        print("ENTER THE BASE NUMBER CORRECTLY!!")
        main()
    
    print("\n\n------***------------***------")    
    print("OUTPUT -- >>  ",convert(t,c1,c2))
    print("------***------------***------\n")
    
    U = input("\nWANT TO TRY AGAIN? PLEASE TYPE -- [YES/Y    OR    NO/N] :--\t").lower()
    print("---------------------------------------------------------------------")
    
    if (U == 'yes' or U == 'y'):
        main()
    else:
        print("\n\n~THANK YOU! ")
        exit()


main()


@ CODED BY TSG405, 2021
