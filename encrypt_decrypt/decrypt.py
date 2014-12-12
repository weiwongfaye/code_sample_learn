

from Crypto.Cipher import AES
import base64
import os
def decryption(encryption_key,encryptedString):
     PADDING = '{'
     DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
     #Key is FROM the printout of 'secret' in encryption
     #below is the encryption.
     encryption = encryptedString
     key = encryption_key.decode('hex')
     cipher = AES.new(key)
     decoded = DecodeAES(cipher, encryption)
     print decoded


if __name__ == '__main__':
     encryption_key = 'xxx'
     encryptedString = 'xxx'

     decryption(encryption_key,encryptedString)

