import requests 
import re 

username = 'natas1'
content = open('C:\\Users\\niroj\\Documents\\Natas\\password.txt')
password = content.readline(-1)[7:39]
print(f"The Password of natas1 is {password}")
# print(password)

url = f'http://{username}.natas.labs.overthewire.org'

response = requests.get(url, auth = (username, password))
htmlDoc = response.text
# print(htmlDoc)
# to get the exact line after 'password' string
print(re.findall('password (.*)', htmlDoc))

