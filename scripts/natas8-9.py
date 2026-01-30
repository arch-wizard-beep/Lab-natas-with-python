import binascii
import requests
import base64
import re

# import html
userName = 'natas8'
url = f'http://{userName}.natas.labs.overthewire.org/'
openFile = open('C:\\Users\\niroj\\Documents\\Natas\\password.txt')
password = openFile.readlines()[7][8:40]

print(password)

# to get the first page
response = requests.get(url, auth = (userName, password))
htmlDoc = response.text
# print(htmlDoc)

# to get the href of source page
response = requests.get(url + 'index-source.html', auth = (userName, password))
htmlDoc = response.text
# htmlDoc = html.unescape(htmlDoc)
# print(htmlDoc)

#----------------From here we will decrypt the code------------------
# lets create a function to reverse the encryption 

data = '3d3d516343746d4d6d6c315669563362'

hexToBin = binascii.unhexlify(data)
print(hexToBin)
revByte = hexToBin.decode()[::-1]
print(revByte)
base64Decode = base64.b64decode(revByte)
print(base64Decode)

plainText = base64Decode.decode() 
print(plainText)
# --------------- Decryption is done ----------------


newPassword = plainText

data = {
    'secret': 'oubWYf2kBq',
    'submit': 'submit'
}
response = requests.post(url, auth = (userName, password), data = data)

htmlDoc = response.text

print(re.findall('password (.*)', htmlDoc))

try:
    with open('C:\\Users\\niroj\\Documents\\Natas\\scripts\\temp\\index.html', 'w') as htmlContent:
        htmlContent.writelines(htmlDoc)
        print("Operation success!")
except IOError as e:
    print(f'We have an error: {e}') 
