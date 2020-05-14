#!/usr/bin/python3
# -*-coding: utf-8-*


#The goal of this script is to automatically write the input files for gaussian g16 calculations.

#standart module :
import sys

#Personal module :
#from store.py import name_mol

a1=sys.argv[1]
a2=sys.argv[2]
b=sys.argv[3]
f=sys.argv[4]

def name_mol(a1,a2):
	if a1==a2:
		return(a1+'2')
	else:
		return(a1+a2)

#Function to write the input file for the scan using DFT :

def input_scan_DFT(a1,a2,b,f):
	tofill=open("scan_DFT_s.inp","w")
	tofill.write("#p {}/{} pop=full 6D 10F scan TD=(Nstates=5,singlets) ".format(f,b)
	+"\n"*2+'scan between 0.6 and 2.6 A'
	+"\n"*2+"0 1"
	+"\n"+"{}".format(a1)
	+"\n"+"{} 1 R".format(a2)
	+"\n"*2+'R 0.5 100 0.05'
	+"\n"*2)
	tofill.close()
	tofill=open("scan_DFT_t.inp","w")
	tofill.write("#p {}/{} pop=full 6D 10F scan TD=(Nstates=5,triplets) ".format(f,b)
	+"\n"*2+'scan between 0.6 and 2.6 A'
	+"\n"*2+"0 3"
	+"\n"+"{}".format(a1)
	+"\n"+"{} 1 R".format(a2)
	+"\n"*2+'R 0.5 100 0.05'
	+"\n"*2)
	tofill.close()

input_scan_DFT(a1,a2,b,f)


#Function to write the input file for the optimisation of the ground state using DFT :

def input_opt_GS_DFT(a1,a2,b,f):
        tofill=open("optGS_DFT.inp","w")
        tofill.write('%chk='+name_mol(a1,a2)+"_DFT"
        +'\n'"#p {}/{} pop=full 6D 10F opt=tight  ".format(f,b)
        +"\n"*2+'optimization of ground state geometry'
        +"\n"*2+"0 1"
        +"\n"+"{}".format(a1)
        +"\n"+"{} 1 1.0".format(a2)
        +"\n"*2)
        tofill.close()

input_opt_GS_DFT(a1,a2,b,f)


#Function that writes the input file for vertical transition energies determination using TD-DFT :

def input_vert_trans_TD(a1,a2,f,b):
        with open ("vert_trans_TD.inp","w") as fillin:
                fillin.write("%oldchk="+name_mol(a1,a2)+"_DFT"
                +"\n"+"#p {}/{} pop=full 6D 10F TD=(NStates=5,50-50) freq, Geom=check Guess=Read".format(f,b)
                +"\n"*2+"Determination of vertical transition energies"
                +"\n"*2+"0 1"
                +"\n"*2)

input_vert_trans_TD(a1,a2,f,b)


#Function that creates input files for geometry optimization of singlets and triplets using TD-DFT.
#The initial goemetry is the optimized geometry for the ground state : 

def input_opt_ES_TD(a1,a2,b,f):
	for k in range(3):
		tofill=open("optES_TD_s"+str(k+1)+".inp","w")
		tofill.write("%oldchk="+name_mol(a1,a2)+"_DFT"
		+"\n"+"#p {}/{} pop=full 6D 10F opt=tight TD=(NStates=5,singlets,root={}) freq, Geom=check Guess=Read".format(f,b,k+1)
		+"\n"*2+"optimization of excited state's geometry"
		+"\n"*2+"0 1"
		+"\n"*2)
		tofill.close()
	for k in range (3):
		tofill=open("optES_TD_t"+str(k+1)+".inp","w")
		tofill.write("%oldchk="+name_mol(a1,a2)+"_DFT"
		+"\n"+"#p {}/{} pop=full 6D 10F opt=tight TD=(NStates=5,triplets,root={}) freq Geom=Check Guess=Read".format(f,b,k+1)
		+"\n"*2+"optmization of excited state's geometry"
		+"\n"*2+"0 3"
		+"\n"*2)
		tofill.close()

input_opt_ES_TD(a1,a2,b,f)

