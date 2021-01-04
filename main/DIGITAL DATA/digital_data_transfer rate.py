# LOGICAL FUNCTION
def convert_SI(val, unit_in, unit_out):
    
    # WITH BASE "BIT PER SECOND"...
    SI = {'kbps':1024, 'mbps':1049000, 'bs':1.0, 'kbs':1000, 'kbs2':8000, 'mbs':1000000, 'mbs2':8000000, 'gbs':1000000000, 'gbs2':8000000000, 'gbps':1074000000, 'tbs':1000000000000, 'tbs2':8000000000000, 'tbps':1100000000000}
    
    return (float(val * SI[unit_in] / SI[unit_out]))



# DRIVER FUNCTION
def temp():
    
    tsg = ['kbps','mbps','bs','kbs','kbs2','mbs','mbs2','gbs','gbs2','gbps','tbs','tbs2','tbps']
    
    
    try:
        
        print("\n\n-----------------------------------------------------------------------------")
        print("LIST OF AVAILABLE UNITS OF DATA TRANSFER --")
        print("* BIT PER SECOND -- bs [CODE]")
        print("* KILOBIT PER SECOND -- kbs [CODE]")
        print("* KILOBYTE PER SECOND -- kbs2 [CODE]")
        print("* KIBIBIT PER SECOND -- kbps [CODE]")
        print("* MEGABIT PER SECOND -- mbs [CODE]")
        print("* MEGABYTE PER SECOND -- mbs2 [CODE]")
        print("* MEBIBIT PER SECOND -- mbps [CODE]")
        print("* GIGABIT PER SECOND -- gbs [CODE]")
        print("* GIGABYTE PER SECOND -- gbs2 [CODE]")
        print("* GIBIBIT PER SECOND -- gbps [CODE]")
        print("* TERABIT PER SECOND -- tbs [CODE]")
        print("* TERABYTE PER SECOND -- tbs2 [CODE]")
        print("* TEBIBIT PER SECOND -- tbps [CODE]")
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
