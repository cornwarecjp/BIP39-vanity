#!/usr/bin/env python3
#    Copyright (C) 2019 by CJP
#
#    This file is part of the BIP39 Vanity generator.
#
#    The BIP39 Vanity generator is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    The BIP39 Vanity generator is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with the BIP39 Vanity generator. If not, see <http://www.gnu.org/licenses/>.

import hashlib

def sha256(data):
	m = hashlib.sha256()
	m.update(data)
	return m.digest()



ENT = 128
CS = ENT // 32
MS = (ENT+CS) // 11

with open('english.txt', 'r') as f:
	wordlist = f.read()
wordlist = wordlist.strip().split('\n')

firstwords = input().strip().split(' ')
assert len(firstwords) == MS - 1

indices = [wordlist.index(fw) for fw in firstwords]

firstbits = ''.join('{:011b}'.format(i) for i in indices)

numFreebits = ENT - len(firstbits)
assert numFreebits + CS == 11

def getLastWord(freeIndex):
	freebits = '{:011b}'.format(freeIndex)[-numFreebits:]
	entbits = firstbits + freebits
	entbytes = (entbits[i:i+8] for i in range(0,len(entbits),8))
	entbytes = (int(b, 2) for b in entbytes)
	entbytes = bytes(entbytes)
	h = sha256(entbytes)
	csbyte = h[0]
	csbits = '{:08b}'.format(csbyte)[:CS]

	wordbits = freebits + csbits
	wordIndex = int(wordbits, 2)

	return(wordlist[wordIndex])

lastwords = [getLastWord(freeIndex) for freeIndex in range(2**numFreebits)]
lastwords = list(set(lastwords))
lastwords.sort()
for w in lastwords:
	print(w)

