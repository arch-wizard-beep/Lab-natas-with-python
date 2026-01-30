import base64

cookie = 'HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg=='

cookie = base64.b64decode(cookie).decode()
print(cookie)
# cookie = cookie.encode('utf-8').hex()
# print(cookie)
# cookie = bytes.fromhex(cookie)
# print(cookie)
# cookie = cookie.decode()
# print(cookie)

# unknownText = cookie

# decryptText = base64.b64decode(unknownText).decode()
# hexEncodedText = decryptText.encode('utf-8').hex()
#     # return hexEncodedText
# byteCode = bytes.fromhex(hexEncodedText) 
# print(byteCode)

def XOR_Operation(defaultData, cipher):
    key = bytearray()
    for i in range(len(defaultData)):
        key.append(defaultData[i] ^ cipher[i % len(cipher)])
    
    key = key.decode()
    return key

key = b'eDWo'
newDefaultData = b'{"showpassword":"yes","bgcolor":"#ffffff"}'
# print(type(key))
xorOperation = XOR_Operation(newDefaultData, key)
# print(xorOperation)
