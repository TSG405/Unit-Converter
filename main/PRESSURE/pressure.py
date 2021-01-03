# LOGICAL FUNCTION
def convert_SI(val, unit_in, unit_out):
    
    # WITH BASE "PASCAL"...
    SI = {'bar':100000, 'pa':1.0, 'p-si':6894.76, 's-atm':101325, 'torr':133.322}
    
    return (float(val * SI[unit_in] / SI[unit_out]))



# DRIVER FUNCTION
def temp():
    
    tsg = ['bar','pa','p-si','s-atm','torr']
    
    
    try:
        
        print("\n\n-----------------------------------------------------------------------------")
        print("LIST OF AVAILABLE UNITS OF PRESSURE --")
        print("* BAR -- bar [CODE]")
        print("* PASCAL -- pa [CODE]")
        print("* POUND PER SQUARE INCH -- p-si [CODE]")
        print("* STANDARD ATMOSPHERE -- s-atm [CODE]")
        print("* TORR -- torr [CODE]")
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
