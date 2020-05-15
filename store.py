#!/usr/bin/python3
# -*-coding: utf-8-*


#The goal of this script is to name the files with a title of the form
# molecule_orbitals_functional and store them into a dedicated directory

#Inputs : symbol for each atom, number of excited states, spin multiplicity, orbital basis set and functional
#Output : files renamed

import sys
import fnmatch
import os
import shutil

a1=sys.argv[1]                 #first atom's symbol
a2=sys.argv[2]                 #second atom's symbol
b=sys.argv[3]                  #orbital basis set
f=sys.argv[4]                  #functional

#creation of the repertory

def name_rep (a1,a2,b,f):
        if a1==a2:
                named=a1+'2/'+b+'/'+f+'/'
        else :
                named=a1+a2+'/'+b+'/'+f+'/'
        return named

rep=name_rep(a1,a2,b,f)

os.makedirs(rep)

#Removing some files

for file in os.listdir("."):
	for k in ["Gau*", "scan_*", "opt*", "*.chk", "en*", "sym*", "*.inp"]:
		if fnmatch.fnmatch(file,k):
			os.remove(file)

#Storage of the remaining files

for file in os.listdir("."):
	for k in ["*.png", "errors", "*.log"]:
		if fnmatch.fnmatch(file,k):
			shutil.move(file,rep)
