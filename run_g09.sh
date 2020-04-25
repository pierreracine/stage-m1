#! /bin/bash
#SBATCH -p xeonv1_mono -c 1 -n 1 -N 1

module load g09/d01
module load python3
a1=H
a2=H
N=2
m=1
b=6-31G**
f=B3LYP

python3 inp.py $a1 $a2 $N $m $b $f

#g09 $inp 

