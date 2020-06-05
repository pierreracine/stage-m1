#! /usr/bin/env python3


#This module contains functions to extract the informations from the .log files created after a g16 calculation.
#The first functions are general purpose functions, for example listing the lines of a file begining with a certain string.
#The second ones are more specific of gaussian output file and use the previous functions.The last ones are used to draw the plot.


#Standart module import :
import numpy as np

#Personal function import :
from calcul import energy

#General purpose functions :

#Function that returns the list of the lines where text is at the begining of the line.

def lines_begin(afile,text):
	L=[]
	k=1
	with open(afile,"r") as tofill:
		for line in tofill.readlines():
			if line.startswith(text):
				L.append(k)
			k+=1
	return(L)


#Function that extract the text of the nth line of the file.

def extract(afile,n):
	with open(afile,"r")as filin:
		text=filin.readlines()[n-1]
		return(text)


#Function that returns the kth "word" of the string (first word for k=0).

def kth_term(string,k):
	kth_word=string.split()[k]
	return(kth_word)


#Functions specific to gaussian output files :

#Function to extract the calculated distance of an optimization of geometry.

def optimized_distance(afile):
	lines=lines_begin(afile," "*27+"!   "+"Optimized Parameters")
	if lines!=[]:
		distance=kth_term(extract(afile,lines[-1]+5),3)
	else:
		distance="not found"
	return(distance)


#Function to extract the electronic energy of the kth ground state energy calculation in a file.
#It is usefull for the exploitation of scan calculation.

def Eelec(afile, k):
	lines=lines_begin(afile," SCF Done:  E(")
	if lines!=[]:
		E0=kth_term(extract(afile,lines[k]),4)
	else:
		E0="not found"
	return(E0)


#Function to compute the kth calculation of the energy of a root.
#It is usefull for the exploitation of scan calculation.

def root(afile, k, state, E0):
	lines=lines_begin(afile," Excited states from <AA,BB:AA,BB> singles matrix:")
	with open(afile,"r") as toread:
		text=toread.readlines()[lines[k]-4]
	if text.startswith(" Root")==True:
		text_parameter=18
	else:
		text_parameter=19
	dE=kth_term(extract(afile,lines[k]+state-text_parameter),3)
	E=energy(E0,dE)
	return(E)


#Function to extract an energy from the summary at the end of a scan output file.

def scan(afile, line, column):
	lines=lines_begin(afile," Summary of the potential surface scan:")
	E=kth_term(extract(afile,lines[-1]+line+3),column)
	return(E)


#Function to extract the harmonic frequency.
#Here works only for diatomic molecules.

def freq(afile):
	lines=lines_begin(afile," Frequencies --")
	f=kth_term(extract(afile,lines[-1]),2)
	return(f)


#Function to extract the ZPE correction.

def ZPE(afile):
	lines=lines_begin(afile," Zero-point correction=")
	if lines!=[]:
		ZPE=kth_term(extract(afile,lines[-1]),2)
	else:
		ZPE="not found"
	return(ZPE)


#Function to extract the electronic energy with ZPE correction.

def Eelec_ZPE(afile):
	lines=lines_begin(afile," Sum of electronic and zero-point Energies=")
	if lines!=[]:
		E=kth_term(extract(afile,lines[-1]),6)
	else:
		E="not found"
	return(E)


#Function to extract the symmetry of an excited state.
#Here works only when applied to single point .log file.

def ES_symmetry(afile, state):
	line=lines_begin(afile," Excited State   "+str(state))[-1]
	symmetry=kth_term(extract(afile, line), 3)
	return(symmetry)


#Functions used for the plot edition :
#Function to extract energies of one root from a file.
#Here it is used on the files 'energies_data_DFT' created before.
#State is an integer : 0 for the ground state and k for the kth excited state.

def one_state(afile,state, step):
	energies_list=[]
	with open (afile,"r") as toread:
		lines=toread.readlines()
	for k in range(step):
		E=float(kth_term(lines[2+k],state+1))
		energies_list.append(E)
	return(energies_list)


#Function to extract the list of distances from energies data files.

def distances(afile, step):
	distances_list=[]
	with open (afile,"r") as toread:
		lines=toread.readlines()
	for k in range(step):
		d=float(kth_term(lines[2+k],0))
		distances_list.append(d)
	return(np.array(distances_list))


#Function to turn the files about optimized parameters and their corresponding energies
#into lists for a scatter plot.

def opt_informations(afile):
	energies_list=[]
	distances_list=[]
	with open (afile,"r") as toread:
		lines=toread.readlines()
	for k in range(2,8):
		if lines[k]!="\n":
			opt_distance=float(kth_term(lines[k],0))
			opt_energy=float(kth_term(lines[k],1))
			distances_list.append(opt_distance)
			energies_list.append(opt_energy)
		else:
			continue
	return(np.array(distances_list),np.array(energies_list))

