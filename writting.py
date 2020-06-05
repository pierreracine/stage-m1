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
	with open("scan_DFT_s.inp","w") as tofill:
		tofill.write("%Nproc=8"
		+"\n"+"#p {}/{} pop=full 6D 10F scan TD=(Nstates=15,singlets) gfprint gfinput iop(6/7=3)".format(f,b)
		+"\n"*2+'scan between 0.6 and 2.6 A'
		+"\n"*2+"0 1"
		+"\n"+"{}".format(a1)
		+"\n"+"{} 1 R".format(a2)
		+"\n"*2+'R {} {} {}'.format(dist_start, step, gap)
		+"\n"*2)
	with open ("scan_DFT_t.inp","w") as tofill:
		tofill.write("%Nproc=8"
		+"\n"+"#p {}/{} pop=full 6D 10F scan TD=(Nstates=15,triplets) gfprint gfinput iop(6/7=3)".format(f,b)
		+"\n"*2+'scan between 0.6 and 2.6 A'
		+"\n"*2+"0 3"
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

#Note on the triplet states : T1 is obtained by forcing convergence of DFT calculation on the lowest
#excited state with multiplicity 3. Thus, root 1 in TD calculations correspond to the second lowest state
#of multiplicity 3. This is the reason why input files for triplets are written in two parts.

def input_opt_ES_TD(a1,a2,b,f):
	for k in range(1,6):
		with open("optES_TD_s"+str(k)+".inp","w") as tofill:
			tofill.write("%oldchk="+name_mol(a1, a2)+"_DFT"
			+"\n%Nproc=8"
			+"\n#p {}/{} pop=full 6D 10F opt=tight TD=(NStates=15,root={}) freq guess=read geom=check gfprint gfinput iop(6/7=3)".format(f,b,k)
			+"\n"*2+"optimization of the geometry of excited state S"+str(k)
			+"\n"*2+"0 1"
			+"\n"*2)
	with open("optES_TD_t1.inp","w") as tofill:
		tofill.write("%oldchk="+name_mol(a1, a2)+"_DFT"
		+"\n%Nproc=8"
		+"\n#p {}/{} pop=full 6D 10F opt=tight freq guess=read geom=check gfprint gfinput iop(6/7=3)".format(f,b)
		+"\n"*2+"optmization of geometry of excited state T1"
		+"\n"*2+"0 3"
		+"\n"*2)
	for k in range (2,6):
		with open("optES_TD_t"+str(k)+".inp","w") as tofill:
			tofill.write("%oldchk="+name_mol(a1, a2)+"_DFT"
			+"\n%Nproc=8"
			+"\n#p {}/{} pop=full 6D 10F opt=tight TD=(NStates=15,triplets,root={}) freq guess=read geom=check gfprint gfinput iop(6/7=3)".format(f,b,k-1)
			+"\n"*2+"optmization of the geometry of excited state T"+str(k)
			+"\n"*2+"0 3"
			+"\n"*2)


#Function to create an input file for single point calculation at ground state optimized geometry.

def input_SP_DFT(a1,a2,b,f):
	for m in ["s","t"]:
		with open ("SP_DFT_"+m+".inp","w") as tofill:
			tofill.write("%oldchk="+name_mol(a1,a2)+"_DFT"
			+"\n"+"%Nproc=8"
			+"\n"+"#p {}/{} pop=full 6D 10F TD=(Nstates=15, {}) Geom=Check guess=read gfprint gfinput iop(6/7=3)".format(f,b,multiplicity(m)[1])
			+"\n"*2+"Vertical transition calculation for {}".format(multiplicity(m)[1])
			+"\n"*2+"0 {}".format(multiplicity(m)[0])
			+"\n"*2)

