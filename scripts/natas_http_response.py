import requests

i = input("Enter the Level number of natas: ")
userName = f'natas{i}' 
# TODO: Add path of credentials
fileContent = open('C:\\Users\\niroj\\Documents\\Natas\\password.txt')

passwordIndex = int(i) - 1 # credential index
password = fileContent.readlines()[passwordIndex][7:39]
# print(password)

url = f'http://{userName}.natas.labs.overthewire.org'
response = requests.get(url, auth = (userName, password))
htmlDoc = response.text

# print(htmlDoc)

try:
    with open('C:\\Users\\niroj\\Documents\\Natas\\scripts\\temp\\index.html', 'w') as htmlFile:
        # TODO: Add path of your html file above--↑
        htmlFile.writelines(htmlDoc)
        print("Operation success!")
except IOError as e:
    print(f'Unexpected though: {e}')
