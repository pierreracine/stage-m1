#! /usr/bin/env python3
# -*-coding: utf-8-*


#The goal of this script is to name the files with a title of the form
#molecule_orbitals_functional and store them into a dedicated directory.


#Standart modules import :
import fnmatch
import os
import shutil
import sys

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


#Storage of the files of interest

for afile in os.listdir("."):
	for k in ["sy*", "*.inp", "en*", "*.png", "errors", "*.log", "DFT_ES_summary"]:
		if fnmatch.fnmatch(afile,k):
			shutil.move(afile,rep)
