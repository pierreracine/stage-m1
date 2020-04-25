#!/usr/bin/env python3

import sys

file_log=sys.argv[1]

def find_text(text):
	L=[]
	k=1
	filin=open(file_log,"r")
	for line in filin.readlines():
		if line=='text':
			L.append(k)
			k+=1
		else:
			k+=1
	if L==[] :
		return('not found')
	else :
		return L

print(find_text('Gaussian, Inc.'))
		
