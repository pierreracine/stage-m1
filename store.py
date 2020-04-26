#!/usr/bin/python3
# -*-coding: utf-8-*


#The goal of this script is to name the files with a title of the form
# molecule_orbitals_functional and store them into a dedicated directory

#Inputs : symbol for each atom, number of excited states, spin multiplicity, orbital basis set and functional
#Output : files renamed

import sys
import os

a1=sys.argv[1]                 #first atom's symbol
a2=sys.argv[2]                 #second atom's symbol
N=sys.argv[3]                  #number of excited states studied
m=sys.argv[4]                  #spin multiplicity
b=sys.argv[5]                  #orbital basis set
f=sys.argv[6]                  #functional

#creation of the repertory

def named (a1,a2,b,f):
        if a1==a2:
                named=a1+'2/'+b+'/'+f+'/'
        else :
                named=a1+a2+'/'+b+'/'+f+'/'
        return named

named=named(a1,a2,b,f)

os.makedirs(named)

#name of the input and log files for gaussian :

def name (a1,a2,b,f):
        if a1==a2 :
                name=a1+'2_'+b+'_'+f
        else :
                name=a1+a2+'_'+b+'_'+f
        return name

nameinp=name(a1,a2,b,f)+'.inp'
namelog=name(a1,a2,b,f)+'.log'

#edition of the title's files

os.rename('inp.inp',named+nameinp)
os.rename('inp.log',named+namelog)

