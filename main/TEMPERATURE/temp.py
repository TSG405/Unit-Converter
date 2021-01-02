# DRIVER FUNCTION
def temp():
    
    try:
        
        print("\n\n----------------------------------------------------------------------------------")
        print(" ENTER '1' ----> TO CONVERT TEMPERATURE FROM CENTIGRADE SCALE to FAHRENHEIT SCALE,\n ENTER '2' ----> TO CONVERT TEMPERATURE FROM FAHRENHEIT SCALE to CENTIGRADE SCALE,\n ENTER '0' ----> TO EXIT THE CONVERTER")
        print("----------------------------------------------------------------------------------\n")
        
        U = int(input())
        print("\n")
        
        if (U == 1):
            
            try:    
                C = float(input(" ENTER THE TEMPERATURE IN CENTIGRADE SCALE [ONLY THE UNITS]:-- \t"))
                re = float((9.0 * C) / 5.0 + (32.0))
                print("\n------*****------------*****------------*****------------*****------\n SO, THE TEMPERATURE IN FAHRENHEIT SCALE IS :-- {}°F\n------*****------------*****------------*****------------*****------".format(re))
            except:
                print("\n WRONG INPUT! ")
        
        elif (U == 2):
            
            try:    
                F = float(input(" ENTER THE TEMPERATURE IN FAHRENHEIT SCALE [ONLY THE UNITS]:-- \t"))
                re = float((F - 32.0) * (5.0 / 9.0))
                print("\n------*****------------*****------------*****------------*****------\n SO, THE TEMPERATURE IN CENTIGRADE SCALE IS :-- {}°C\n------*****------------*****------------*****------------*****------".format(re))
            except:
                print("\n WRONG INPUT! ")
        
        elif (U == 0):
        
            print("------*****------\n~~ THANK YOU \n------*****------")
            exit()
        
        else:
        
            print("\n WRONG INPUT! ")
    
    
    except:
    
        print("\n WRONG INPUT! ")
    
    temp()




temp()



@ CODED BY TSG405, 2021
