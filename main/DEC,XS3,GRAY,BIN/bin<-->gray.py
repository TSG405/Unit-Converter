# Helper function [ XOR - LOGIC ]
def xor_c(a, b):
    return '0' if(a == b) else '1'
 
 
# Helper function [ fliping bits ]
def flip(c):
    return '1' if(c == '0') else '0'



# BIN --> GRAY-CODE FUNC. [1]
def binarytoGray(binary):
    gray = "";    
    gray += binary[0];
 
    for i in range(1, len(binary)):
         
        # Concatenation
        gray += xor_c(binary[i - 1], 
                      binary[i]);
 
    return (gray)
 
 
# GRAY-CODE --> BIN FUNC. [2]
def graytoBinary(gray):
    binary = "";
    binary += gray[0];
  
    for i in range(1, len(gray)):
         
        if (gray[i] == '0'):
            binary += binary[i - 1];
            
        else:
            binary += flip(binary[i - 1]);
 
    return (binary)
    



# DRIVER FUNCTION
def temp():
        
    try:
        
        print("\n\n-----------------------------------------------------------------------------")
        print("PRESS '1' -- TO CONVERT BINARY TO GRAY-CODE.")
        print("PRESS '2' -- TO CONVERT GRAY-CODE TO BINARY.")
        print("-----------------------------------------------------------------------------")
        
        us = int(input())
        
        
        if (us == 1):
        
            try:
                binary = input("\nENTER THE BINARY [BIN] CODE -- \t")
                
                print("\n------***------------***------")
                print("GRAY-CODE OF --> ", binary, "   IS ---> ", binarytoGray(binary));
                print("------***------------***------\n")
                        
            except:
                print("\n* INVALID [BIN] CODE INPUT! PLEASE TRY AGAIN..!")
                temp()
                
                
        elif (us == 2):
          
            try:
                gray = input("\nENTER THE GRAY [GRAY-CODE] -- \t")
                
                print("\n------***------------***------")
                print("BINARY OF --> ", gray, "   IS ---> ", graytoBinary(gray));
                print("------***------------***------\n")
                        
            except:
                print("\n* INVALID [GRAY] CODE INPUT! PLEASE TRY AGAIN..!")
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



print("\n              ***  [BIN] <---> [GRAY-CODE] CONVERTER  ***\n                ---------------------------------------")
temp()


@ CODED BY TSG405, 2021 
