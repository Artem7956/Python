import requests
import osa

def get_cel_by_far(temp):

    url = 'https://www.w3schools.com/xml/tempconvert.asmx'
    headers = {"Content-Type":"text/xml"}
    data_f_to_c = f''''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <FahrenheitToCelsius xmlns="https://www.w3schools.com/xml/">
      <Fahrenheit>{temp}</Fahrenheit>
    </FahrenheitToCelsius>
  </soap:Body>
</soap:Envelope>'''
    print(data_f_to_c)
    req = requests.post(url=url,data=data_f_to_c,headers=headers)
    print ('result',req.text)


def get_avg_temp(file):

    with open(file, 'r') as f:
        temps = list()
        for line in f:
             temps.append(int(line.split()[0]))

    return sum(temps)/len(temps)

avg = get_avg_temp('temps.txt')
print(avg)
get_cel_by_far(120)

