import requests
import time

API = input("BOT: ENTER YOUR FIXER.IO-API TOKEN :--- \t")
print("\n")


# API-ACCESS FUNCTION
def currency_data(API):

    try:
        url = str.__add__('http://data.fixer.io/api/latest?access_key=',API) 
        print("LOADING...")
        time.sleep(2)
        return requests.get(url).json();
    
    except:
        print("\nBOT: CAN'T ACCESS THE CURRENCY API RIGHT NOW! PLEASE CHECK YOUR API-ID AND INTERNET CONNECTION!")
        exit();


# CONVERTER FUNCTION
def convert(rates, from_currency, to_currency, amount): 
    
    initial_amount = amount 
    
    if from_currency != 'EUR' : 
        amount = amount / rates[from_currency] 
    amount = round(amount * rates[to_currency], 2)
        
    print("\n----------------------------------**")
    print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))
    print("----------------------------------**\n")
   
   
# DISPLAY COUNTRY-CODES
def c_list():
    k=['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTC', 'BTN', 'BWP', 'BYN', 'BYR', 'BZD', 'CAD', 'CDF', 'CHF', 'CLF', 'CLP', 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SRD', 'STD', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VEF', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMK', 'ZMW', 'ZWL']
    print("\nBOT: LIST OF ACCEPTED COUNTRY CODES -----> \n",k)
 
 
# DRIVER FUNCTION
def main():
    
    try:
        c_data=currency_data(API)
        I = input("BOT: WANT TO KNOW THE AVAILABLE COUNTRY CODES ?? ENTER [YES/Y   OR   NO/N]: -- \t").lower()
        if I == "yes" or I == "y":
            c_list()
        
        from_country = input("\nFrom Country [CODE]: ") 
        to_country = input("To Country [CODE]: ") 
        amount = int(input("Amount [VALUE]: ")) 
        convert(c_data["rates"],from_country, to_country, amount) 
    
    except:
        print('BOT: ERROR! THE COUNTRY CODE WAS NOT FOUND...! \n');


# DRIVER CODE..
main()
while (1):
    
    print("\n-----***----------***----------***----------***----------***-----")
    U = input("BOT: WANT TO CHECK MORE ?? ENTER [YES/Y  or  NO/N]:\t").lower()
    print("-----***----------***----------***----------***----------***-----\n")
    
    if U == "yes" or U == "y":
        main()
    
    elif U == "no" or U == "n":
        print("\nBOT: THANK YOU!")
        break
    
    else:
        print("\nWRONG INPUT!!")
        
        
        
        
@ CODED BY TSG405, 2021         
