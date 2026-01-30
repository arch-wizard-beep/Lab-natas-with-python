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

print(sessionCookies)

response = requests.get(url + 'index-source.html', auth = (userName, password))
htmlSource = response.text

try:
    with open("C:\\Users\\niroj\\Documents\\Natas\\scripts\\temp\\index.html", 'w') as htmlContain:
        htmlContain.writelines(htmlDoc)
        print("Operation Successfully accomplished!")
except IOError as e:
    print(f"Error {e} has appeared")

try:
    with open("C:\\Users\\niroj\\Documents\\Natas\\scripts\\temp\\index-source.html", 'w') as htmlContain:
        htmlContain.writelines(htmlSource)
        print("Source operation Successfully accomplished!")
except IOError as e:
    print(f"Error {e} has appeared")

# ---------------------------- Encryption & Decryption ----------------------------
# Concept of XOR Operator
# remember Xor is also represented as '^' sign (OK👌)
# It work as: a ^ b = c
# Interestingly: a ^ c = b
# password ^ key = encryptedOne 
# encryptedOne ^ key = password ..!

cipherText = sessionCookies['data'].replace('%3D', '==')

print(cipherText)


def Unknown_2_Byte (unknownText):
    decryptText = base64.b64decode(unknownText)
    # hexEncodedText = decryptText.encode('utf-8').hex()
    # # return hexEncodedText
    # byteCode = bytes.fromhex(hexEncodedText)
    return decryptText




cipher = Unknown_2_Byte(cipherText)
print(cipher)

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

# print(f'cipher: {type(cipher)}\ndefaultData: {type(defaultData)}')
defaultKey = XOR_Operation(defaultData, cipher)
print(defaultKey)

# we have the $key <cencored> but in repeated manner  
# create a function to get the repeated substring

def Repeated_Substring(key):
    match = re.search(r"(.+?)\1", key)
    key = match.group(1)
    return key
    
substring = Repeated_Substring(defaultKey)
print(substring)
# Goodness, finally I have actual😮‍💨 key 

 # to match the sequence 
defaultKey = defaultKey.encode()
newDefaultData = b'{"showpassword":"no","bgcolor":"#ffffff"}'


def New_XOR_Operation(defaultData, cipher):
    key = bytearray()
    for i in range(len(defaultData)):
        key.append(defaultData[i] ^ cipher[i % len(cipher)])
    
    key = key.decode()
    return key



newCipher = New_XOR_Operation(newDefaultData, defaultKey)
print(newCipher)

cookie = newCipher.encode()
print(cookie)
cookie = base64.b64encode(cookie).decode()
print(cookie)
cookie = cookie.replace('=','%3D')
print(cookie)
# newCipher = newCipher.encode('utf-8')
# print(newCipher)
# newCipher = newCipher.hex()
# newCipher = newCipher.encode('utf-8')
# newCipher = base64.b64encode(newCipher)
# print(newCipher)
# newCookie = base64.b64encode(newCipher)
# hexEncodedText = newCookie.hex()
# byteCode = hexEncodedText.encode('utf-8')
# print(newCipher)

# Unknown_2_Byte(newCipher)

# ------------------------------ Done ----------------------------------

cookie = {
     'data': 'HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg'
 }

response = requests.post(url, auth = (userName, password), cookies=cookie)
htmlDoc = response.text
print(htmlDoc)