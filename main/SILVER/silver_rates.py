import http.client
import json
import time



API = input("BOT: SILVER-API TOKEN :--- \t")
print("\n")



# API-ACCESS FUNCTION
def silver_api(API):

  payload = ''
  headers = {
    'x-access-token': API,
    'Content-Type': 'application/json'
  }
  
  url = "www.goldapi.io"
  
  try:
      conn = http.client.HTTPSConnection(url)
      print("LOADING...")
      time.sleep(2)
      conn.request("GET", "/api/XAG/INR", payload, headers)
      res = conn.getresponse()
      return (json.loads(res.read().decode("utf-8")))
      
  except:
      print("\nERROR!! Try checking the API-PIN, AND INTERNET CONNECTIVITY!")



# DRIVER CODE..
try: 
    data = silver_api(API)
    silver_price = data['price']
    print("SILVER PRICE, for today [INR] :\t",silver_price)
except:
    print("~Thank You")



@ CODED BY TSG405, 2021        
