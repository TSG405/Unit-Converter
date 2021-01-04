import re
import urllib.request
import string


# URL-ACCESS FUNCTION
def url_auth():
    
    global html
    
    try:
        ur = urllib.request.urlopen('http://www.exchangerates.org.uk/commodities/live-gold-prices/XAU-USD.html')
        html = ur.read().decode('utf-8')

        d = re.search("value_XAUUSD",html,re.I)
        return (d)
    
    except:
        print("\nERROR!! Try checking your -- INTERNET CONNECTIVITY!")


d = url_auth()

# DRIVER CODE..
if (d) :
    index_val =  html.index("value_XAUUSD")
    index_val_update = index_val + 14
    
    index_val_update_end = index_val + 23
   
    print ("GOLD PRICE [USD]:\t",html[index_val_update : index_val_update_end ])
    
else :
    print ('ERROR! TRY LATER!\n~THANK YOU')


@ CODED BY TSG405, 2021
