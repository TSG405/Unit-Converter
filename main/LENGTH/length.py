# LOGICAL FUNCTION
def convert_SI(val, unit_in, unit_out):
    
    # WITH BASE "METRES"...
    SI = {'mm':0.001, 'cm':0.01, 'm':1.0, 'km':1000, 'um':0.000001, 'nm':0.000000001, 'mile': 1609.34, 'yard': 0.9144, 'ft': 0.3048, 'in': 0.0254, 'nautical miles': 1852}
    
    return (float(val * SI[unit_in] / SI[unit_out]))



# DRIVER FUNCTION
def temp():
    
    tsg = ['mm','cm','m','km','um','nm','mile','yard','ft','in','nautical miles']
    
    
    try:
        
        print("\n\n-----------------------------------------------------------------------------")
        print("LIST OF AVAILABLE UNITS OF LENGTH --")
        print("* MILLIMETER -- mm [CODE]")
        print("* CENTIMETER -- cm [CODE]")
        print("* METER -- m [CODE]")
        print("* KILOMETER -- km [CODE]")
        print("* MICROMETER -- um [CODE]")
        print("* NANOMETER -- nm [CODE]")
        print("* MILE -- mile [CODE]")
        print("* YARD -- yard [CODE]")
        print("* FOOT -- ft [CODE]")
        print("* INCH -- in [CODE]")
        print("* NAUTICAL MILES -- nautical miles [CODE]")
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
