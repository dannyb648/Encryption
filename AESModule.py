#!/usr/bin/python
from Crypto.Cipher import AES

class AESModule():	
	def encrypt(self, key, mode, data, IV):
		if(mode == 1):
			obj = AES.new(str(key), AES.MODE_ECB, str(IV))
			return obj.encrypt(data)

		elif(mode == 2):
			obj = AES.new(key, AES.MODE_CBC, str(IV))
              		return obj.encrypt(data)
	
		elif(mode == 3):
			obj = AES.new(key, AES.MODE_CFB, str(IV))
			return obj.encrypt(data)
		
		elif(mode == 4):
			obj = AES.new(key, AES.MODE_OFB, str(IV))
			return obj.encrypt(data)

	def decrypt(self, key, mode, ciphertext, IV):
		if(mode == 1):
			obj = AES.new(str(key), AES.MODE_ECB, str(IV))
			return obj.decrypt(ciphertext)
		
		elif(mode == 2):
			obj = AES.new(str(key), AES.MODE_CBC, str(IV))
			return obj.decrypt(ciphertext)

		elif(mode == 3):
			obj = AES.new(str(key), AES.MODE_CFB, str(IV))
			return obj.decrypt(ciphertext)

		elif(mode == 4):
			obj = AES.new(str(key), AES.MODE_OFB, str(IV))
			return obj.decrypt(ciphertext)


