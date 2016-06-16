#!/usr/bin/python
from Crypto.Cipher import DES3
from Crypto import Random
from Crypto.Util import Counter

class TDESModule():	
	def encrypt(self, key, mode, data, IV):
		if(mode == 1):
			obj = DES3.new(str(key), DES3.MODE_ECB, str(IV))
			return obj.encrypt(data)

		elif(mode == 2):
			obj = DES3.new(key, DES3.MODE_CBC, str(IV))
              		return obj.encrypt(data)
	
		elif(mode == 3):
			obj = DES3.new(key, DES3.MODE_CFB, str(IV))
			return obj.encrypt(data)
		
		elif(mode == 4):
			obj = DES3.new(key, DES3.MODE_OFB, str(IV))
			return obj.encrypt(data)

	def decrypt(self, key, mode, ciphertext, IV):
		if(mode == 1):
			obj = DES3.new(str(key), DES3.MODE_ECB, str(IV))
			return obj.decrypt(ciphertext)
		
		elif(mode == 2):
			obj = DES3.new(str(key), DES3.MODE_CBC, str(IV))
			return obj.decrypt(ciphertext)

		elif(mode == 3):
			obj = DES3.new(str(key), DES3.MODE_CFB, str(IV))
			return obj.decrypt(ciphertext)

		elif(mode == 4):
			obj = DES3.new(str(key), DES3.MODE_OFB, str(IV))
			return obj.decrypt(ciphertext)


