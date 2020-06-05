#! /bin/env python3


#The goal of this script is to plot for each root the energy as a function of interatomic distance.
#The plot is stored as a pgn file.


#Classical modules import :
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy import interpolate
import sys

#Personal modules import :
import reading as r
import writting as w

matplotlib.use('TkAgg')

a1=sys.argv[1]
a2=sys.argv[2]
b=sys.argv[3]
f=sys.argv[4]
dist_start=float(sys.argv[5])
gap=float(sys.argv[6])
step=int(sys.argv[7])

#Plots of the ground state and singlets or triplets excited states

if __name__=="__main__":
	name=w.name_mol(a1,a2)	

	X=r.distances("energies_data_DFT_s", step)
	with open("sym_data_DFT_s") as toread:
		text0="Ground state"
	Y0=np.array(r.one_state("energies_data_DFT_s", 0, step))
	smooth0=interpolate.interp1d(X,Y0,kind="quadratic")
	for m in ["s","t"]:
		for root in range(1, 6):
			sym=w.symmetry("sym_data_DFT_"+m, root)
			text="root:{} Sym:{}".format(root,sym)
			Y=np.array(r.one_state("energies_data_DFT_"+m, root, step))
			smooth=interpolate.interp1d(X,Y,kind="quadratic")
			plt.plot(X,smooth(X),label=text)
		
		plt.plot(X,smooth0(X),label=text0)
	
		opt_distances=r.opt_informations("opt_DFT_"+m)[0]
		opt_energies=r.opt_informations("opt_DFT_"+m)[1]
		plt.scatter(opt_distances,opt_energies,c='k',marker='x',label="Optimized geometries")

		plt.xlabel('Interatomic distance (Angstrom)')
		plt.ylabel('Energy (Hartree)')
		plt.xlim=(dist_start,dist_start+gap*(step+1))
		plt.legend(loc='lower right')
		plt.title(w.multiplicity(m)[1]+' excited states of '+name+'\n'+'('+b+' and '+f+')')
		plt.savefig(name+'_'+b+'_'+f+'_'+m)
		plt.clf()
