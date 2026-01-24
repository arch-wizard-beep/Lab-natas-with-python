import requests

userName = 'natas5'
fileContent = open('C:\\Users\\niroj\\Documents\\Natas\\password.txt') 
password = fileContent.readlines()[4][7:39] 
print(password)

url = f'{userName}.natas.labs.overthewire.org'
