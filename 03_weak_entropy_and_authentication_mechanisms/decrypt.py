#!/usr/bin/env python3

import random
import sys
import time
from Crypto.Cipher import AES


def decrypt(input_file, output_file):

	with open(input_file, 'rb') as f_in:
		data = f_in.read()
	
	nonce = data[:16]
	tag = data[16:32]
	cipher = data[32:]
	seed = 1676934000
	for seed in range (1676934000, 1677020401):
		print(seed)
		random.seed(seed)
		key = random.randbytes(16)
		aes = AES.new(key, AES.MODE_GCM, nonce)
		try:
			plaintext = aes.decrypt_and_verify(cipher, tag)
			with open(output_file, 'wb') as f_out:
				f_out.write(plaintext) # len(data) bytes
			break
		except:
			continue


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'usage: {sys.argv[0]} <src-file> <dst-file>', file=sys.stderr)
        exit(1)
    decrypt(sys.argv[1], sys.argv[2])
