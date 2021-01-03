# LOGICAL FUNCTION
def convert_SI(val, unit_in, unit_out):
    
    # WITH BASE "CUBIC-METRES"...
    SI = {'ml':0.000001, 'l':0.001, 'c-m':1.0, 'cc':0.000001, 'u-lg':0.00378541, 'u-lq':0.000946353, 'u-lp':0.000473176, 'u-lc':0.00024, 'f-ou':0.000029574, 'u-ts':0.000014787, 'u-ts2':0.000004928, 'i-g':0.00454609, 'i-q':0.00113652, 'i-p':0.000568261, 'i-c':0.000284131, 'i-ts':0.000017758, 'i-ts2':0.000005919, 'c-f':0.0283168, 'c-i':0.000016387}
    
    return (float(val * SI[unit_in] / SI[unit_out]))



# DRIVER FUNCTION
def temp():
    
    tsg = ['ml','l','cc','c-m','u-lg','u-lq','u-lp','u-lc','f-ou','u-ts','u-ts2','i-g','i-q','i-p','i-c','i-ts','i-ts2','c-f','c-i']
    
    
    try:
        
        print("\n\n-----------------------------------------------------------------------------")
        print("LIST OF AVAILABLE UNITS OF VOLUME --")
        print("* MILLI-LITRES/CUBIC-CENTIMETRES -- ml/cc [CODE]")
        print("* LITRES -- l [CODE]")
        print("* CUBIC-METRES -- c-m [CODE]")
        print("* US-LIQUID GALLON -- u-lg [CODE]")
        print("* US-LIQUID QUART -- u-lq [CODE]")
        print("* US-LIQUID PINT -- u-lp [CODE]")
        print("* US-LEGAL CUP -- u-lc [CODE]")
        print("* FLUID OUNCE -- f-ou [CODE]")
        print("* US-TABLESPOON -- u-ts [CODE]")
        print("* US-TEASPOON -- u-ts2 [CODE]")
        print("* IMPERIAL GALLON -- i-g [CODE]")
        print("* IMPERIAL QUART -- i-q [CODE]")
        print("* IMPERIAL PINT -- i-p [CODE]")
        print("* IMPERIAL CUP -- i-c [CODE]")
        print("* IMPERIAL TABLESPOON -- i-ts [CODE]")
        print("* IMPERIAL TEASPOON -- i-ts2 [CODE]")
        print("* CUBIC-FOOT -- c-f [CODE]")
        print("* CUBIC-INCH -- c-i [CODE]")
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
