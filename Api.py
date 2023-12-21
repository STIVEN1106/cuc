#import Flask
import requests
import sqlite3

class API():
        def GetApi():
                Authorization="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6InBydWViYTIwMjJAY3VjLmVkdS5jbyIsImV4cCI6MTY0OTQ1MzA1NCwiY29ycmVvIjoicHJ1ZWJhMjAyMkBjdWMuZWR1LmNvIn0.MAoFJE2SBgHvp9BS9fyBmb2gZzD0BHGPiyKoAo_uYAQ"
        #"JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6InBydWViYTIwMjJAY3VjLmVkdS5jbyIsImV4cCI6MTY0OTQ1MzA1NCwiY29ycmVvIjoicHJ1ZWJhMjAyMkBjdWMuZWR1LmNvIn0.MAoFJE2SBgHvp9BS9fyBmb2gZzD0BHGPiyKoAo_uYAQ"


                url="https://consultas.cuc.edu.co/api/v1.0/articulos?format=json"
                headers = {"Authorization": f"JWT {Authorization}","Accept": "application/json"}
                try:
                        Respuesta=requests.get(url,headers=headers)
                        #print(Respuesta)
                        if Respuesta.status_code==200:
                                dataJson=Respuesta.json()
                                #print(url,headers)
                                #print('ingresó a la API')
                                #print(dataJson)
                                return dataJson


                except Exception as e:

                        print("error",e)
        GetApi()