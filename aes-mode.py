from  Cryptodome.Cipher  import  AES
from  Cryptodome  import  Random

# Randomly  generated  keys  are  better  than  hardcoded  ones

key = Random.new().read(AES.key_size [1]) # 192  bits
plaintext1 = b"My love  for  Alice is  immeasurable" # length: 34
plaintext2 = b"It is  quite  true  that  Bob  loves  Alice" # length: 38

iv = Random.new().read(AES.block_size)


## Correct  usage: one  object  for  encryption , one for  decryption
## E.g. for  chat  between two , a pair of AES  objects  for  each  client

aes1 = AES.new(key , AES.MODE_CFB , iv)
aes2 = AES.new(key , AES.MODE_CFB , iv)

ciphertext1 = aes1.encrypt(plaintext1)
ciphertext2 = aes1.encrypt(plaintext2)

decrypted1 = aes2.decrypt(ciphertext1)
decrypted2 = aes2.decrypt(ciphertext2)

print(decrypted1 == plaintext1)

