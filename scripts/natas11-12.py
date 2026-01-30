import requests
import base64
import re
import binascii


userName = 'natas11'
url = f'http://{userName}.natas.labs.overthewire.org/'


fileContent = open("C:\\Users\\niroj\\Documents\\Natas\\password.txt")
password = fileContent.readlines()[10][8:40]


response = requests.get(url, auth = (userName, password))
htmlDoc = response.text


sessionCookies = requests.Session().get(url, auth=(userName, password))
sessionCookies = sessionCookies.cookies.get_dict()

print(f'(*) session cookies: {sessionCookies}\n')

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

cipher = base64.b64decode(cipherText)
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
print(f'(+) The KEY=>[{substring}] has been extracted successfully.')
# Goodness, finally I have actual😮‍💨 key 


defaultKey = substring.encode('utf-8')
newDefaultData = '{"showpassword":"yes","bgcolor":"#ffffff"}'
newDefaultData = newDefaultData.encode('utf-8')

print(defaultKey, newDefaultData)

def New_XOR_Operation(defaultData, cipher):
    key = bytearray()
    for i in range(len(defaultData)):
        key.append(defaultData[i] ^ cipher[i % len(cipher)])
    
    key = key.decode()
    return key


newCipher = New_XOR_Operation(newDefaultData, defaultKey)
print(f'(+) The XOR Operation is performed successfully\n(*) The Encrypted cookie has been extracted : {newCipher} ')

def XOR_2_Cookie(inlet):
    binaryForm = inlet.encode()
    # hexForm = binaryForm.hex().encode()
    base64Form = base64.b64encode(binaryForm).decode('utf-8')
    # cookieConversion = base64Form.replace('=','%3D')
    # return cookieConversion
    return base64Form
    # return hexForm

cookie = XOR_2_Cookie(newCipher)
print(f'\n(+) Encrypted cookie is encoded with base64: {cookie}')

# ------------------------------ Done ----------------------------------

cookie = {
     'data': cookie
 }

response = requests.get(url, auth = (userName, password), cookies = cookie)
htmlDoc = response.text

try:
    with open('C:\\Users\\niroj\\Documents\\Natas\\scripts\\temp\\result.html', 'w') as htmlContain:
        htmlContain.writelines(htmlDoc)
        print('(+) final Documentation is collected!')
except IOError as e:
    print(f"(-) Unexpectedly: {e}")

solution = re.findall('password(.*)',htmlDoc)
print(solution)