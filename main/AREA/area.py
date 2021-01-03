# LOGICAL FUNCTION
def convert_SI(val, unit_in, unit_out):
    
    # WITH BASE "SQUARE-METRES"...
    SI = {'s-km':1000000, 's-mile':2590000, 's-m':1.0, 'hectare':10000, 's-yard': 0.836127, 's-ft': 0.092903, 's-in': 0.00064516, 'acre': 4046.86}
    
    return (float(val * SI[unit_in] / SI[unit_out]))



# DRIVER FUNCTION
def temp():
    
    tsg = ['s-km','s-mile','s-m','hectare','s-yard','s-ft','s-in','acre']
    
    
    try:
        
        print("\n\n-----------------------------------------------------------------------------")
        print("LIST OF AVAILABLE UNITS OF AREA --")
        print("* SQUARE-METERS -- s-m [CODE]")
        print("* SQUARE-MILE -- s-mile [CODE]")
        print("* SQUARE-KILOMETERS -- s-km [CODE]")
        print("* HECTARES -- hectare [CODE]")
        print("* SQUARE-YARDS -- s-yard [CODE]")
        print("* SQUARE-FOOT -- s-ft [CODE]")
        print("* SQUARE-INCH -- s-in [CODE]")
        print("* ACRES -- acre [CODE]")
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
