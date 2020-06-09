#! /usr/bin/env python3


#This module contains functions to write input files for gaussian 16 with title.


#Function to name the molecule.

def name_mol(a1,a2):
	if a1==a2:
		name=a1+'2'
	else:
		name=a1+a2
	return (name)


#Function to write the ms value and the mutiplicity in the title.

def multiplicity(m):
	if m=="s":
		multiplicity=[1, "singlets"]
	else:
		multiplicity=[3, "triplets"]
	return (multiplicity)


#Function to write correctly the symmetry of the state.

def symmetry(afile, root):
	with open(afile,"r") as toread:
		string=toread.readlines()[1+root]
	if string.find("?")!=-1:
		return("not determined")
	else:
		if string[0]=="S":
			return(string[8:].strip())
		else:
			return(string[6:].strip())


#Functions for (TD-)DFT calculations :

#Function to write the input files for the scan using DFT.

def input_scan_DFT(a1, a2, b, f, dist_start, gap, step):
	for m in ["s", "t"]:
		with open("scan_DFT_"+m+".inp","w") as tofill:
			tofill.write("%Nproc=8"
			+"\n"+"#p {}/{} pop=full 6D 10F scan TD=(Nstates=15, {}) gfprint gfinput iop(6/7=3)".format(f, b, multiplicity(m)[1])
			+"\n"*2+'scan between 0.6 and 2.6 A'
			+"\n"*2+"0 1"
			+"\n"+"{}".format(a1)
			+"\n"+"{} 1 R".format(a2)
			+"\n"*2+'R {} {} {}'.format(dist_start, step, gap)
			+"\n"*2)


#Function to write the input file for the optimisation of the ground state using DFT.

def input_opt_GS_DFT(a1,a2,b,f):
	with open("optGS_DFT.inp","w") as tofill:
		tofill.write('%chk='+name_mol(a1,a2)+"_DFT"
		+"\n"+"%Nproc=8"
		+'\n'"#p {}/{} pop=full 6D 10F opt=tight freq gfprint gfinput iop(6/7=3)".format(f,b)
		+"\n"*2+'optimization of ground state geometry'
		+"\n"*2+"0 1"
		+"\n"+"{}".format(a1)
		+"\n"+"{} 1 1.0".format(a2)
		+"\n"*2)


#Function that creates input files for geometry optimization of singlets and triplets using TD-DFT.
#The initial goemetry is the optimized geometry for the ground state.

def input_opt_ES_TD(a1,a2,b,f):
	for m in ["s", "t"]:
		for k in range(1,6):
			with open("optES_TD_"+m+str(k)+".inp","w") as tofill:
				tofill.write("%oldchk="+name_mol(a1, a2)+"_DFT"
				+"\n%Nproc=8"
				+"\n#p {}/{} pop=full 6D 10F opt=tight TD=(NStates=15, {}, root={}) freq ".format(f, b, multiplicity(m)[1], k)
				+"\nguess=read geom=check gfprint gfinput iop(6/7=3)"
				+"\n"*2+"optimization of the geometry of excited state {} {}".format(m, k)
				+"\n"*2+"0 1"
				+"\n"*2)


#Function to create an input file for single point calculation at ground state optimized geometry.

def input_SP_DFT(a1,a2,b,f):
	for m in ["s","t"]:
		with open ("SP_DFT_"+m+".inp","w") as tofill:
			tofill.write("%oldchk="+name_mol(a1,a2)+"_DFT"
			+"\n"+"%Nproc=8"
			+"\n"+"#p {}/{} pop=full 6D 10F TD=(Nstates=15, {}) Geom=Check guess=read gfprint gfinput iop(6/7=3)".format(f,b,multiplicity(m)[1])
			+"\n"*2+"Vertical transition calculation for {}".format(multiplicity(m)[1])
			+"\n"*2+"0 1"
			+"\n"*2)

