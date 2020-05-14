#! /bin/python

#The goal of this script is to plot for each electronic
#state the energy as a function of interatomic distance

import sys

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

#import exploit.py as ex

a1=sys.argv[1]
a2=sys.argv[2]
b=sys.argv[3]
f=sys.argv[4]

def name_mol(a1,a2):
        if a1==a2:
                return(a1+'2')
        else:
                return(a1+a2)


def kth_term(string,k):
        kth_word=string.split()[k]
        return(kth_word)

#Function that gives the interatomic distance

def distance(k):
	d=0.55+k*0.1
	return(d)


#Function that plot the energy as a function of interatomic distance for one state:
#state is an integer : 0 for the ground state and an integer for an excited state

def one_state(afile,state):
	distances_list=[]
	energies_list=[]
	for k in range(50):
		d=distance(k)
		distances_list.append(d)
		with open (afile,"r") as toread:
			lines=toread.readlines()
			E=float(kth_term(lines[2+2*k],state))
			energies_list.append(E)
	return(distances_list,energies_list)


#Function to write correctly the symmetry of the state

def symmetry(string):
	if string.find("?")!=-1:
		return("not determined")
	else:
		if string[0]=="S":
			return(string[8:])
		if string[0]=="3":
			return(string[6:])


#Plots of the ground state and singlets or triplets excited states

if __name__=="__main__":
	name=name_mol(a1,a2)
	
	X=np.array(one_state("energies_data_DFT_s",0)[0])

	for m in ["s","t"]:
		if m=="s":
			multiplicity="Singlets"
		else:
			multiplicity="Triplets"
		with open("sym_data_DFT_"+m) as toread:
			text0="Ground state"
			Y0=np.array(one_state("energies_data_DFT_"+m,0)[1])
			smooth0=interpolate.interp1d(X,Y0,kind="quadratic")
			plt.plot(X,smooth0(X),label=text0)
		for k in range(1,4):
			with open("sym_data_DFT_"+m,"r") as toread:
				sym=symmetry(toread.readlines()[1+k])
				text="root:{} Sym:{}".format(k,sym)
				Y=np.array(one_state("energies_data_DFT_"+m,k)[1])
				smooth=interpolate.interp1d(X,Y,kind="quadratic")
				plt.plot(X,smooth(X),label=text)
	
		plt.xlabel('Interatomic distance (Angstrom)')
		plt.ylabel('Energy (Hartree)')
		plt.legend()
		plt.title(multiplicity+' excited states of '+name+'\n'+'('+b+' and '+f+')')
		plt.savefig(name+'_'+b+'_'+f+'_'+m)
		plt.show()

