from  Cryptodome.Cipher  import  AES
from  Cryptodome  import  Random

ciphertext = bytes.fromhex("07f631fe65dfd567ea16cefc8f7d7a2117d976935c81dff69587d7a60e79b99529c19d910e52f8e1fae1680ceb438ed461b6bf4ab655d390ee5329f89f458affec7fe3a7660c59374248326469e22b635e7f17abb1beb28dc4e401bf99b149d7b445215fdca7823677")
key = bytes.fromhex("6555d417a283161f440cfad518eb852845a6ff45f7e1b7623090b7714a5bbd5f")

iv = bytes.fromhex("9e6632df5a211060622769d9c2300753")

aes = AES.new(key , AES.MODE_CFB , iv)


plaintext = aes.decrypt(ciphertext)

print(plaintext)