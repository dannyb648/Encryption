from varModule import Vars
from AESModule import AESModule
from DESModule import DESModule
from TDESModule import TDESModule
from BFModule import BFModule
from RC2Module import RC2Module
import sys
import time


def main():
	runAES()
	runDES()
	runTDES()
	runBF()
	runRC()



def runAES():
	v = Vars()
	aes = AESModule()	
	key_list = ["G0BVHxuWJYReaw2m", "qu1oi0vuH4NR4ZdtrVrjIig9", str(v.get_key(256))]
	data_list = [str(v.get_data(16)), str(v.get_data(1024)),  str(v.get_data(2048)), str(v.get_data(4096))]
	iv = v.get_IV16byte()
	for mode_count in range(1,5):
		for key_count in range(0,3):
			for data_count in range(0,4):
					t = time.clock()
					cipher = aes.encrypt(key_list[key_count], mode_count, data_list[data_count], iv)
					
					print time.clock() - t
	
def runDES():
	v = Vars()
	des = DESModule()
	key = v.get_key(64)
	data_list = [str(v.get_data(16)), str(v.get_data(1024)),  str(v.get_data(2048)), str(v.get_data(4096))]
	iv = v.get_IV8byte()
	for mode_count in range(1,5):
		for data_count in range(0,4):
			time.clock()
			cipher = des.encrypt(key, mode_count, data_list[data_count], iv)
			print time.clock() 	

def runTDES():
	v = Vars()
	tdes = TDESModule()
	key_list = ["G0BVHxuWJYReaw2m", "qu1oi0vuH4NR4ZdtrVrjIig9"]
	data_list = [str(v.get_data(16)), str(v.get_data(1024)), str(v.get_data(2048)), str(v.get_data(4096))]
	iv = v.get_IV8byte()
	for mode_count in range(1,5):
		for key_count in range(0,2):
			for data_count in range(0,4):
				time.clock()
				cipher = tdes.encrypt(key_list[key_count],mode_count, data_list[data_count], iv)
				print time.clock()	


def runBF():
	v = Vars()
	bf = BFModule()
	key_list = [v.get_key(56), v.get_key(112), v.get_key(256)]
	data_list = [str(v.get_data(16)), str(v.get_data(1024)),  str(v.get_data(2048)), str(v.get_data(4096))]
	iv = v.get_IV8byte()
	for mode_count in range(1,5):
		for key_count in range(0,3):
			for data_count in range(0,4):
				time.clock()
				cipher = bf.encrypt(key_list[key_count], mode_count, data_list[data_count], iv)
				print time.clock()
			


def runRC():
	v = Vars()
	rc = RC2Module()
	key_list = [v.get_key(40), v.get_key(64), v.get_key(128)]
	data_list = [str(v.get_data(16)), str(v.get_data(1024)), str(v.get_data(2048)), str(v.get_data(4096))]
	iv = v.get_IV8byte()
	for mode_count in range(1,5):
		for key_count in range(0,3):
			for data_count in range(0,4):
				time.clock()
				cipher = rc.encrypt(key_list[key_count], mode_count, data_list[data_count], iv)
				print time.clock()
			

main()
