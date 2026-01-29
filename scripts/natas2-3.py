import requests

username = 'natas2'
content = open('C:\\Users\\niroj\\Documents\\Natas\\password.txt')# add your path where you stored the credentials
password = content.readlines()[1][8:40]
# print(password)

url = f'http://natas2.natas.labs.overthewire.org/files/users.txt'
response = requests.get(url, auth = (username, password))
htmlDoc = response.text
print(htmlDoc)

# print(re.findall('password(.*)', htmlDoc))

