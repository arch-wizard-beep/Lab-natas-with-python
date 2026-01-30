import requests
import base64
import re
import binascii
#----------------------------------------#
# Don't follow along, itn't the solution #
#----------------------------------------#


userName = 'natas11'
url = f'http://{userName}.natas.labs.overthewire.org/'


fileContent = open("C:\\Users\\niroj\\Documents\\Natas\\password.txt")
password = fileContent.readlines()[10][8:40]


response = requests.get(url, auth = (userName, password))
htmlDoc = response.text


sessionCookies = requests.Session().get(url, auth=(userName, password))
sessionCookies = sessionCookies.cookies.get_dict()

print('[*] session cookies: ',sessionCookies)

try:
    with open("C:\\Users\\niroj\\Documents\\Natas\\scripts\\temp\\index.html", 'w') as htmlContain:
        htmlContain.writelines(htmlDoc)
        print("(+) html documentation has been saved!")
except IOError as e:
    print(f"(-) Error {e} has appeared")



response = requests.get(url + 'index-source.html', auth = (userName, password))
htmlSource = response.text

try:
    with open("C:\\Users\\niroj\\Documents\\Natas\\scripts\\temp\\index-source.html", 'w') as htmlContain:
        htmlContain.writelines(htmlSource)
        print("(+) html php-source documentation has been saved!")
except IOError as e:
    print(f"(-) Error {e} has appeared")

# ---------------------------- Encryption & Decryption ----------------------------
# Concept of XOR Operator
# remember Xor is also represented as '^' sign 
# (OK👌)
# It work as: a ^ b = c
# Interestingly: a ^ c = b
# password ^ key = encryptedOne 
# encryptedOne ^ key = password ..!

cipherText = sessionCookies['data'].replace('%3D', '==')

print(f'(+) Cookies cipher text {cipherText} type {type(cipherText)}')


def Unknown_2_Byte (unknownText):
    decryptText = base64.b64decode(unknownText)
    # hexEncodedText = decryptText.encode('utf-8').hex()
    # # return hexEncodedText
    # byteCode = bytes.fromhex(hexEncodedText)
    return decryptText


cipher = Unknown_2_Byte(cipherText)
print('(+) The xor cipher text is extracted successfully: ',cipher)

# form the $defaultdata of php source 
# defaultData = 'array( "showpassword"=>"no", "bgcolor"=>"#ffffff")'
# newData = json.encoder(defaultData)
# print(newData)

defaultData = b'{"showpassword":"no","bgcolor":"#ffffff"}'


# create a function for Xor operation 



def XOR_Operation(defaultData, cipher):
    key = bytearray()
    for i in range(len(defaultData)):
        key.append(cipher[i] ^ defaultData[i])
    
    key = key.decode()
    return key

defaultKey = XOR_Operation(defaultData, cipher)


# we have the $key <cencored> but in repeated manner  

def Repeated_Substring(key):
    match = re.search(r"(.+?)\1", key)
    key = match.group(1)
    return key
    
substring = Repeated_Substring(defaultKey)
print(f'(+) The KEY=>[ {substring} ] has been extracted successfully.')
# Goodness, finally I have actual😮‍💨 key 


defaultKey = defaultKey.encode()
newDefaultData = b'{"showpassword":"no","bgcolor":"#ffffff"}'


def New_XOR_Operation(defaultData, cipher):
    key = bytearray()
    for i in range(len(defaultData)):
        key.append(defaultData[i] ^ cipher[i % len(cipher)])
    
    key = key.decode()
    return key



newCipher = New_XOR_Operation(newDefaultData, defaultKey)
print(f'(+) The XOR Operation is performed successfully\n(+) The Encrypted cookie:  {newCipher} ')

def XOR_2_Cookie(inlet):
    binaryForm = inlet.encode()
    base64Form = base64.b64encode(binaryForm).decode()
    cookieConversion = base64Form.replace('=','%3D')
    return cookieConversion

cookie = XOR_2_Cookie(newCipher)
print(f'\n(+) Cipher is converted into cookie: {cookie}')

# ------------------------------ Done ----------------------------------

cookie = {
     'data': 'HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg'
 }

response = requests.post(url, auth = (userName, password), cookies=cookie)
htmlDoc = response.text
# print(htmlDoc)