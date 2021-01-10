# DEC --> XS3-CODE FUNC. [1]
def decxs(n):  
   t = list(n)
   r = ''
   d = {'0':'0011', '1':'0100', '2':'0101', '3':'0110', '4':'0111', '5':'1000', '6':'1001', '7':'1010', '8':'1011', '9':'1100', '.':'.'}
   
   for i in t:
       r = r + d[i]
   
   return(r)


# XS3-CODE --> DEC FUNC. [2]
def xsdec(n,z):   
   r =  ''
   dd = {'0011':'0', '0100':'1', '0101':'2', '0110':'3', '0111':'4', '1000':'5', '1001':'6', '1010':'7', '1011':'8', '1100':'9', '.':'.'}
   
   if '.' not in n:   
       for i in range (0,z,4):
           k = ''
           for ii in range(4):
               k = k + n[i+ii]
           r = r + dd[k]
       
       return(r)
   
   # FOR FRACTIONAL NUMBERS
   else:   
       f = n.index('.')
       
       for i in range (0,f,4):
           k = ''
           for ii in range(4):
               k = k + n[i+ii]
           r = r + dd[k]
           
       r += '.'
       
       for i in range (f+1,z,4):
           k = ''
           for ii in range(4):
               k = k + n[i+ii]
           r = r + dd[k]
       
       return(r)



# DRIVER FUNCTION
def temp():
        
    try:
        
        print("\n\n-----------------------------------------------------------------------------")
        print("PRESS '1' -- TO CONVERT DECIMAL TO EXCESS-3 CODE.")
        print("PRESS '2' -- TO CONVERT EXCESS-3 CODE TO DECIMAL.")
        print("-----------------------------------------------------------------------------")
        
        us = int(input())
        
        
        if (us == 1):
        
            try:
                j = float(input("\nENTER THE DECIMAL [DEC] CODE -- \t"))
                
                if (j >= 0.0):
                    n = str(j)
                    print("\n------***------------***------")
                    print("{} = {} [XS-3 FORMAT] ".format(j,decxs(n)))
                    print("------***------------***------\n")
     
                else:
                    n = str ( j * (- 1.0) )
                    print("\n------***------------***------")
                    print("{} = -{} [XS-3 FORMAT] ".format(j,decxs(n)))
                    print("------***------------***------\n")
                    
            except:
                print("\n* INVALID CODE INPUT! PLEASE TRY AGAIN..!")
                temp()
                
                
        elif (us == 2):
        
            try:
                jk = input("\nENTER THE EXCESS-3 [XS-3] CODE -- \t")
                
                j = list(jk)
                z = len(j)
                
                if '-' not in j:
                    print("\n------***------------***------")
                    print("{} = {} [DEC FORMAT] ".format(jk,xsdec(j,z)))
                    print("------***------------***------\n")
     
                else:
                    j.remove('-')
                    print("\n------***------------***------")
                    print("{} = -{} [DEC FORMAT] ".format(jk,xsdec(j,z)))
                    print("------***------------***------\n")
                    
            except:
                print("\n* INVALID CODE INPUT [USE 4-DIGIT GROUP CODE]! PLEASE TRY AGAIN..!")
                temp()
                
                
        else:
            print("\n* INVALID INPUT! TRY AGAIN..!")
            temp()
            
    except:
        print("\n* ENTER THE [OPTION](1/2) CORRECTLY!!")
        temp()
    
    
    U = input("\nWANT TO TRY AGAIN? PLEASE TYPE -- [YES/Y    OR    NO/N] :--\t").lower()
    
    if (U == 'yes' or U == 'y'):
        temp()
        
    else:
        print("\n\n~THANK YOU! ")
        exit()



print("\n              ***  [DEC] <---> [XS-3] CONVERTER  ***\n                ----------------------------------")
temp()


@ CODED BY TSG405, 2021
