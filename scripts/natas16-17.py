import requests

userName = 'natas16'
url = f'http://{userName}.natas.labs.overthewire.org/'
pathToDir = '%MyDocuments%\\Natas\\'
password = open(pathToDir + 'password.txt', 'r').readlines()[15][8:40]
print(password)

response = requests.get(url, auth = (userName, password))
htmlDoc = response.text

print(htmlDoc)