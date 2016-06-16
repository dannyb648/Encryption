#!/usr/bin/python
from Crypto.Cipher import ARC2 #Check Docs

class RC2Module():
	def encrypt(self, key, mode, data, IV):
		if(mode == 1):
			obj = ARC2.new(str(key), ARC2.MODE_ECB, str(IV))
			return obj.encrypt(data)

		elif(mode == 2):
			obj = ARC2.new(str(key), ARC2.MODE_CBC, str(IV))	
			return obj.encrypt(data)

		elif(mode == 3):
			obj = ARC2.new(str(key), ARC2.MODE_CFB, str(IV))
			return obj.encrypt(data)

		elif(mode == 4):
			obj = ARC2.new(str(key), ARC2.MODE_OFB, str(IV))
			return obj.encrypt(data)
