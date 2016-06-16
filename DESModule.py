#!/usr/bin/python
from Crypto.Cipher import DES

class DESModule():	
	def encrypt(self, key, mode, data, IV):
		if(mode == 1):
			obj = DES.new(str(key), DES.MODE_ECB, str(IV))
			return obj.encrypt(data)

		elif(mode == 2):
			obj = DES.new(key, DES.MODE_CBC, str(IV))
              		return obj.encrypt(data)
	
		elif(mode == 3):
			obj = DES.new(key, DES.MODE_CFB, str(IV))
			return obj.encrypt(data)
		
		elif(mode == 4):
			obj = DES.new(key, DES.MODE_OFB, str(IV))
			return obj.encrypt(data)

	def decrypt(self, key, mode, ciphertext, IV):
		if(mode == 1):
			obj = DES.new(str(key), DES.MODE_ECB, str(IV))
			return obj.decrypt(ciphertext)
		
		elif(mode == 2):
			obj = DES.new(str(key), DES.MODE_CBC, str(IV))
			return obj.decrypt(ciphertext)

		elif(mode == 3):
			obj = DES.new(str(key), DES.MODE_CFB, str(IV))
			return obj.decrypt(ciphertext)

		elif(mode == 4):
			obj = DES.new(str(key), DES.MODE_OFB, str(IV))
			return obj.decrypt(ciphertext)


