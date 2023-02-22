#!/usr/bin/env python3

import random
import sys
import time
from Crypto.Cipher import AES


def decrypt(input_file, output_file):

	with open(input_file, 'rb') as f_in:
		data = f_in.read()
	
	dataclean = data[32:]
	found = False
	while (not found):
		seed = 1676329200
		random.seed(seed)
		key = random.randbytes(16)
		aes = AES.new(key, AES.MODE_GCM)

		try:
			plaintext, tag = aes.decrypt_and_verify(dataclean)
		except:
			if (seed > 1676415600):
				print("failed")
				found = True
			seed = seed + 1
			continue
		found = True

	with open(output_file, 'wb') as f_out:
		f_out.write(aes.nonce)  # 16 bytes
		f_out.write(tag)        # 16 bytes
		f_out.write(plaintext) # len(data) bytes


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'usage: {sys.argv[0]} <src-file> <dst-file>', file=sys.stderr)
        exit(1)
    decrypt(sys.argv[1], sys.argv[2])
