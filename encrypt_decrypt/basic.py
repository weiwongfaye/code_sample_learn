from Crypto.Cipher import AES
import base64

secret_key = "this is password"
msg_text = "message to encry"

cipher = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
encoded = base64.b64encode(cipher.encrypt(msg_text))
decoded = cipher.decrypt(base64.b64decode(encoded))

print encoded
print decoded