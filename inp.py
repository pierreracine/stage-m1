#!/usr/bin/env python3


#The goal of this script is to automatically write the input files for gaussian g16 calculations.
#It uses the functions in the module 'writting.py' to do so.


#Standart module import :
import sys

#Personal module import:
import writting as w


a1=sys.argv[1]
a2=sys.argv[2]
b=sys.argv[3]
f=sys.argv[4]
dist_start=sys.argv[5]
gap=sys.argv[6]
step=sys.argv[7]

w.input_scan_DFT(a1, a2, b, f, dist_start, gap, step)
w.input_opt_GS_DFT(a1, a2, b, f)
w.input_opt_ES_TD(a1, a2, b, f)
w.input_SP_DFT(a1, a2, b, f)
