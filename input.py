#!/usr/bin/python3
# -*-coding: utf-8-*


#The goal of this script is to automatically write the input file for gaussian g09 calculation 

#Inputs : symbol for each atom, number of excited states, spin multiplicity, orbital basis set and functional
#Operation : creates a file that can be used as a gaussian calculation input file
#Output : file ready to be run with gaussian 09

import sys

a1=sys.argv[1]                 #first atom's symbol
a2=sys.argv[2]                 #second atom's symbol
N=sys.argv[3]                  #number of excited states studied
m=sys.argv[4]                  #spin multiplicity
b=sys.argv[5]                  #orbital basis set
f=sys.argv[6]                  #functional

#edition of the input file :

tofill=open("inp.inp","w")
tofill.write("#p {}/{} pop=full 6D scan TD(root={})".format(f,b,N)+"\n"*2+'title'
+"\n"*2+"0 {}".format(m)
+"\n"+"{}".format(a1)
+"\n"+"{} 1 R".format(a2)
+"\n"*2+"R 0.6 20 0.1"
+"\n"*2)

tofill.close()
