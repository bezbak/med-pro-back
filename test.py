import requests 
print(requests.get('http://localhost:3000/doctorInfo/1').text)