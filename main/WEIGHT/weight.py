# LOGICAL FUNCTION
def convert_SI(val, unit_in, unit_out):
    
    # WITH BASE "GRAMS"...
    SI = {'mg':0.001, 'cg':0.01, 'g':1.0, 'kg':1000, 'ton':1000000, 'ug':0.000001, 'ng':0.000000001, 'us-ton': 907185, 'stone': 6350.29, 'pound': 453.592, 'ounce': 28.3495}
    
    return (float(val * SI[unit_in] / SI[unit_out]))



# DRIVER FUNCTION
def temp():
    
    tsg = ['mg','cg','g','kg','ug','ng','ton','us-ton','stone','pound','ounce']
    
    
    try:
        
        print("\n\n-----------------------------------------------------------------------------")
        print("LIST OF AVAILABLE UNITS OF WEIGHT --")
        print("* MILLIGRAM -- mg [CODE]")
        print("* CENTIGRAM -- cg [CODE]")
        print("* GRAM -- g [CODE]")
        print("* KILOGRAM -- kg [CODE]")
        print("* MICROGRAM -- ug [CODE]")
        print("* NANOGRAM -- ng [CODE]")
        print("* TONNE -- ton [CODE]")
        print("* US-TON -- us-ton [CODE]")
        print("* STONE -- stone [CODE]")
        print("* POUND -- pound [CODE]")
        print("* OUNCE -- ounce [CODE]")
        print("-----------------------------------------------------------------------------")
        
        unit_in = input("\nFROM UNIT [CODE]-- \t")
        if unit_in not in tsg:
            print("ENTER THE CODE CORRECTLY!")
            temp()
        
        unit_out = input("TO UNIT [CODE]-- \t")
        if unit_out not in tsg:
            print("ENTER THE CODE CORRECTLY!")
            temp()
            
        amount = float(input("ENTER THE AMOUNT --\t"))
        
        res = (convert_SI(amount, unit_in, unit_out))
        
        print("\n------***------------***------")
        print("{} {} = {} {}".format(amount, unit_in, res, unit_out))
        print("------***------------***------\n")
    
    
    except:
    
        print("\nENTER THE AMOUNT CORRECTLY!!")
        temp()
    
    
    U = input("\nWANT TO TRY AGAIN? PLEASE TYPE -- [YES/Y    OR    NO/N] :--\t").lower()
    
    if (U == 'yes' or U == 'y'):
        temp()
    else:
        print("\n\n~THANK YOU! ")
        exit()


temp()
        

@ CODED BY TSG405, 2021
