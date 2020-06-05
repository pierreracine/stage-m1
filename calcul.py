#! /usr/bin/env python3


#This module contains functions to compute energies, based on the quantities extracted from th g16 output files.


H=27.2114		#value of 1 hartree in ev

#Function that calculates the energy of the excited state from
#ground state energy and difference of energy between them

def energy(E_GS,delta_E):
	E_ES=float(E_GS)+float(delta_E)/H
	return(str(E_ES))


#Function to compute the kth distance for scan starting at dist_start.

def distance(dist_start, gap, k):
	d=dist_start+gap*k
	return(d)

