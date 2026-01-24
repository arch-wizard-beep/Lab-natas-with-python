import requests 
import re 

username = 'natas0'
password = username

url = 'http://natas0.natas.labs.overthewire.org'

response = requests.get(url, auth = (username, password))
content = response.text

# to get the exact line after 'password' string
print(re.findall('password (.*)', content))

