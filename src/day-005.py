#Practing error handling and api validation.
import requests 


try:
  response = requests.get(
    "https://catfact.ninja/fact" #getting the api connection from the website
  )
  
  if response.status_code == 200: # to check the status code like (200 , 401 , 404 , 500) codes
    data = response.json()
    print(f'the fact is : {data['fact']}')
  else:
      print(f'failed with this status code :{response.status_code}') #rise error if status code not match

except requests.exceptions.RequestException:      #RequestException?
    print("Network error occurred")
                                                  #The requests library has many network-related errors:

                                                  #ConnectionError
                                                  #Timeout
                                                  #TooManyRedirects
                                                  #RequestException (this is parent for all errors)
