#! /bin/bash
#SBATCH -p xeonv1_mono -c 1 -n 1 -N 1

module load g09/d01

#please, fill the following informations to run the script

a1=H           #symbol of the first atom, Ex : H, Li
a2=Li           #symbol of the second atom
N=2            #number of excited states
m=1            #spin multiplicity
b=aug-cc-pvdz      #orbital basis set
f=B3LYP        #functional


python3 input.py $a1 $a2 $N $m $b $f         #execution of the script writing the input file for Gaussian
g09 inp.inp
python3 store.py $a1 $a2 $N $m $b $f
