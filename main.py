from varModule import Vars
from AESModule import AESModule
from DESModule import DESModule
from TDESModule import TDESModule
from BFModule import BFModule
from RC2Module import RC2Module
import sys
import time


def main():
	runRC()
	runBF()
	runAES()
	runDES()
	runTDES()



def runAES():
	v = Vars()
	aes = AESModule()	
	key_list = ["G0BVHxuWJYReaw2m", "qu1oi0vuH4NR4ZdtrVrjIig9", str(v.get_key(256))]
	data_list = [str(v.get_data(16)), str(v.get_data(1024)),  str(v.get_data(2048)), str(v.get_data(4096))]
	iv = v.get_IV16byte()
	for mode_count in range(1,5):
		for key_count in range(0,3):
			for data_count in range(0,4):
					cipher = aes.encrypt(key_list[key_count], mode_count, data_list[data_count], iv)
						
#					time.sleep(1)
					
					print "AES! Encrypted - keycount: " + str(key_count) + " mode_count: " + str(mode_count) + " data_count: " + str(data_count)		
	
def runDES():
	v = Vars()
	des = DESModule()
	key = v.get_key(64)
	data_list = [str(v.get_data(16)), str(v.get_data(1024)),  str(v.get_data(2048)), str(v.get_data(4096))]
	iv = v.get_IV8byte()
	for mode_count in range(1,5):
		for data_count in range(0,4):
			cipher = des.encrypt(key, mode_count, data_list[data_count], iv)

#			time.sleep(1)

			print "DES! Encrypted = mode_count: " + str(mode_count) + " data_count: " + str(data_count)

def runTDES():
	v = Vars()
	tdes = TDESModule()
	key_list = ["G0BVHxuWJYReaw2m", "qu1oi0vuH4NR4ZdtrVrjIig9"]
	data_list = [str(v.get_data(16)), str(v.get_data(1024)), str(v.get_data(2048)), str(v.get_data(4096))]
	iv = v.get_IV8byte()
	for mode_count in range(1,5):
		for key_count in range(0,2):
			for data_count in range(0,4):
				cipher = tdes.encrypt(key_list[key_count],mode_count, data_list[data_count], iv)

#				time.sleep(1)
		
				print "TDES! Encrypted - keycount: " + str(key_count) + " mode_count: " + str(mode_count) + " data_count: " + str(data_count)


def runBF():
	v = Vars()
	bf = BFModule()
	key_list = [v.get_key(56), v.get_key(112), v.get_key(256)]
	data_list = [str(v.get_data(16)), str(v.get_data(1024)),  str(v.get_data(2048)), str(v.get_data(4096))]
	iv = v.get_IV8byte()
	for mode_count in range(1,5):
		for key_count in range(0,3):
			for data_count in range(0,4):
				cipher = bf.encrypt(key_list[key_count], mode_count, data_list[data_count], iv)

#				time.sleep(1)

				print "BF! Encrypted - keycount: " + str(key_count) + " mode_count: " + str(mode_count) + " data_count: " + str(data_count)


def runRC():
	v = Vars()
	rc = RC2Module()
	key_list = [v.get_key(40), v.get_key(64), v.get_key(128)]
	data_list = [str(v.get_data(16)), str(v.get_data(1024)), str(v.get_data(2048)), str(v.get_data(4096))]
	iv = v.get_IV8byte()
	for mode_count in range(1,5):
		for key_count in range(0,3):
			for data_count in range(0,4):
				cipher = rc.encrypt(key_list[key_count], mode_count, data_list[data_count], iv)

#				time.sleep(1)

				print "RC2! Encrypted - keycount: " + str(key_count) + " mode_count: " + str(mode_count) + " data_count: " + str(data_count)

main()
