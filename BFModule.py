#!/usr/bin/python
from Crypto.Cipher import Blowfish

class BFModule():
	def encrypt(self, key, mode, data, IV):
		if(mode == 1):
			obj = Blowfish.new(key, Blowfish.MODE_ECB, str(IV))
			return obj.encrypt(data)

		elif(mode == 2):
			obj = Blowfish.new(key, Blowfish.MODE_CBC, str(IV))
			return obj.encrypt(data)

		elif(mode == 3):
			obj = Blowfish.new(key, Blowfish.MODE_CFB, str(IV))
			return obj.encrypt(data)
			
		elif(mode == 4):
			obj = Blowfish.new(key, Blowfish.MODE_OFB, str(IV))
			return obj.encrypt(data)

