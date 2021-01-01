def timeconv():
    try:
        print("\n-----------------------------------------------------------------------")
        print(" ENTER '1' ----> TO CONVERT TIME FROM 12-HOUR FORMAT to 24-HOUR FORMAT,\n ENTER '2' ----> TO CONVERT TIME FROM 24-HOUR FORMAT to 12-HOUR FORMAT,\n ENTER '0' ---> TO EXIT THE CONVERTER")
        print("-----------------------------------------------------------------------\n")
        
        U = int(input())
        print("\n")
        
        if U == 1:
            
            try:    
                twelve = input(" ENTER THE 12-HOUR FORMAT TIME -- [XX:YY AM/PM] Format :\t").split()
                
                if twelve[-1] == "PM" or twelve[-1] == "pm":
                    k = twelve[0].split(":")
                    re = int(k[0])+12
                    
                    if re <= 24 and re >= 12 and int(k[1]) >= 0 and int(k[1]) <= 59 and int(k[0])!=0 :
                        
                        if re != 24:
                            print(" TIME IN 24-HOUR FORMAT --> {}:{}".format(re,k[-1]))
                        else:
                            print(" TIME IN 24-HOUR FORMAT --> {}:{}".format(12,k[-1]))
                    
                    else:
                       print(" WRONG INPUT! ")
                
                elif twelve[-1] == "AM" or twelve[-1] == "am":
                    k = twelve[0].split(":")
                    
                    if int(k[0]) <= 12 and int(k[0]) > 0 and int(k[1]) >= 0 and int(k[1]) <= 59 :
                        
                        if int(k[0])!=12:
                            print(" TIME IN 24-HOUR FORMAT --> {}:{}".format(k[0],k[-1]))
                        else:
                            print(" TIME IN 24-HOUR FORMAT --> {}:{}".format(0,k[-1]))
                    
                    else:
                        print(" WRONG INPUT! ")
                
                else:
                    print(" WRONG INPUT! ")
            
            except:
                print(" WRONG INPUT! ")
            
            timeconv()
        
        
        
        elif U == 2:
            
            try:
                twenty_four = input(" ENTER THE 24-HOUR FORMAT TIME -- [XX:YY] Format :\t").split(":")
                
                if int(twenty_four[0]) >= 12 and int(twenty_four[0]) < 24 and int(twenty_four[1]) >= 0 and int(twenty_four[1]) <= 59 :
                    
                    if int(twenty_four[0]) != 12:
                        print(" TIME IN 12-HOUR FORMAT --> {}:{} PM".format(int(twenty_four[0])-12,(twenty_four[-1])))
                    else:
                        print(" TIME IN 12-HOUR FORMAT --> {}:{} PM".format(12,(twenty_four[-1])))
                
                elif int(twenty_four[0]) >= 0 and int(twenty_four[0]) < 13 and int(twenty_four[1]) >= 0 and int(twenty_four[1]) <= 59 :
                    
                    if int(twenty_four[0]) != 0:
                        print(" TIME IN 12-HOUR FORMAT --> {}:{} AM".format(int(twenty_four[0]),(twenty_four[-1])))
                    else:
                        print(" TIME IN 12-HOUR FORMAT --> {}:{} AM".format(12,(twenty_four[-1])))
                
                else:
                    print(" WRONG INPUT! ")
            
            except:
                print(" WRONG INPUT! ")
            
            timeconv()
        
        elif U == 0:
            print("\n Thank you!")
            exit()
        
        else:
            print(" WRONG INPUT! ")
            timeconv()
    
    except:
        print(" WRONG INPUT! ")
    
    timeconv()


timeconv()



@ CODED BY TSG405, 2021
