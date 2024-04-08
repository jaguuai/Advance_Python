# ExchangeRate-Api servisini kullanarak döviz çeviri uygulaması 
import requests
import json

api_key="2e60aedf5e76aae8dbcf2799"
api_url=f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

current_currency_type=input("Bozulan döviz türü: ")  #USD,TRY
return_currency_type=input("Alınan döviz türü: ") #TRY
amount=input(f"Ne kadar {current_currency_type} döviz bozdurmak istiyorsunuz?")

result=requests.get(api_url + current_currency_type)
# print(result.text) / StrinG olarak api den çektiğimiz json dosyasını alırız
 #ama bize asıl gereken kısım conversion_rate bunun için strin olarak gelen
  #json dosaymızı dictinoray liseteye cevirelim
result_json=json.loads(result.text)
# print(result_json["conversion_rates"][return_currency_type])
print("1 {0}={1} {2}".format(current_currency_type,result_json["conversion_rates"][return_currency_type],return_currency_type))
print("{0} {1}={2} {3}".format(amount,current_currency_type,amount*result_json["conversion_rates"][return_currency_type],return_currency_type))