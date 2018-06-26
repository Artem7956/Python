import requests
import xml.dom.minidom


def get_cel_by_far(temp):

    url = 'https://www.w3schools.com/xml/tempconvert.asmx'
    headers = {"Content-Type": "text/xml"}
    data_f_to_c = f'''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <FahrenheitToCelsius xmlns="https://www.w3schools.com/xml/">
      <Fahrenheit>{temp}</Fahrenheit>
    </FahrenheitToCelsius>
  </soap:Body>
</soap:Envelope>'''

    req = requests.post(url=url, data=data_f_to_c, headers=headers)
    dom = xml.dom.minidom.parseString(req.text)
    dom.normalize()
    node1 = dom.getElementsByTagName("FahrenheitToCelsiusResult")[0]
    return node1.childNodes[0].nodeValue


def get_avg_temp(file):
    with open(file, 'r') as f:
        temps = [int(line.split()[0]) for line in f]
    return sum(temps)/len(temps)


avg = get_avg_temp('temps.txt')
print('Средняя температура по Фаренгейту: {0}, по Цельсию: {1}'.format(avg, get_cel_by_far(avg)))
