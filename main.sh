#! /bin/bash
#SBATCH -p xeonv1_mono -c 1 -n 8 -N 1


#Welcome to main.sh. This script uses all the other .py scripts and runs the calculations.
#To use the programm enter your parameters in the 'informations' file.
#Write the first and second atomic symbol and the basis set and functionnal, seperated by a blanck space.
#If you want to study several diatomic molecules, write the informations for each of them on different lines.
#An exemple is already written in the 'informations' file.

#Have fun !


module load gaussian/g16-b01
module load python/3.7.6-gcc-9.2.0
module load python/py-cycler-0.10.0-gcc-9.2.0
module load python/py-h5py-2.9.0-gcc-9.2.0
module load python/py-kiwisolver-1.1.0-gcc-9.2.0
module load python/py-matplotlib-3.2.1-gcc-9.2.0
module load python/py-numpy-1.18.1-gcc-9.2.0
module load python/py-pyparsing-2.4.2-gcc-9.2.0
module load python/py-python-dateutil-2.8.0-gcc-9.2.0
module load python/py-scipy-1.4.1-gcc-9.2.0
module load python/py-six-1.11.0-gcc-4.8.5
module load python/py-six-1.12.0-gcc-9.2.0
module load python/python-2.7.15-gcc-4.8.5
module load python/python-2.7.15-gcc-8.2.0
module load python/python-3.7.0-gcc-4.8.5
module load python/python-3.7.0-gcc-8.2.0

cat informations | while read line;do

        read -ra ADDR <<< "$line"
        a1=${ADDR[0]}
        a2=${ADDR[1]}
        b=${ADDR[2]}
        f=${ADDR[3]}
	dist_start=${ADDR[4]}
	gap=${ADDR[5]}
	step=${ADDR[6]}
	python3 inp.py $a1 $a2  $b $f $dist_start $gap $step		#Execution of the script writing the input files for Gaussian

	g16 optGS_DFT.inp						#Optimization of ground state
	g16 scan_DFT_s.inp						#Scan calculations
	g16 scan_DFT_t.inp 

	for m in s t
	do
		g16 SP_DFT_$m.inp

		for k in `seq 1 5`;					#Optimization for excited states
		do
			g16 optES_TD_s$k.inp
			g16 optES_TD_t$k.inp
		done
	done

	python3 errors.py						#Script to write the file listing all errors
	python3 exploitlog.py $dist_start $gap $step			#Script to extract energies and optimal geometries
	python3 graph.py $a1 $a2  $b $f $dist_start $gap $step		#Sript to plot the graphs of energies for 2N+1 states
#	python3 store.py $a1 $a2  $b $f					#Script to rename and store files of interest
#	rm *.inp Gau* scan_* opt* *.chk en* sym*			#Deletion of the last files

done
