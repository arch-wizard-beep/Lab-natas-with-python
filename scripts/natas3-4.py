import requests

username = 'natas3'
content = open('C:\\Users\\niroj\\Documents\\Natas\\password.txt')
password = content.readlines()[2][8:40]

# print(password)

# url = f'http://{username}.natas.labs.overthewire.org/robots.txt'
url = f'http://{username}.natas.labs.overthewire.org/s3cr3t/users.txt'
response = requests.get(url, auth = (username, password))
htmlDoc = response.text
print(htmlDoc)