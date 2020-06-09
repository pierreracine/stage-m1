#! /usr/bin/env python3

#The purpose of this script is to produce a file listing all errors that occured during the calculations.
#For example geometry optimization for excited states could fail because this is not a bound state.

import sys

#Edition of errors file:

with open ("errors","w") as tofill:
	tofill.write("File containing all errors from gaussian calculations"+"\n"*2)


#Function that check if normal terminaison has occured during gaussian calculation.

def termination(afile):
	with open (afile,"r") as toread:
		lines=toread.readlines()
		if lines[-1].startswith(' Normal termination'):
			return ("Normal termination")
		else:
			return("Abnormal termination, please check the file for more information")

#Function that writes the errors detected in the errors file:

def edition_error(afile):
	normalornot=termination(afile)
	if normalornot!="Normal termination":
		with open ("errors","a") as tofill:
			tofill.write(afile+'	'+normalornot+"\n")

edition_error("optGS_DFT.log")
for m in ["s", "t"]:
	edition_error("scan_DFT_"+m+".log")
	edition_error("SP_DFT_"+m+".log")
	for k in range(1,6):
		edition_error("optES_TD_"+m+str(k)+".log")

