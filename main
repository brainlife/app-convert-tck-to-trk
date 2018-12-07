#!/bin/bash
#PBS -l nodes=1:ppn=8,walltime=0:10:00
#PBS -N trk2trk
#PBS -V

module load singularity 2> /dev/null

SINGULARITYENV_PYTHONNOUSERSITE=true singularity exec -e docker://brainlife/dipy:0.13 ./convert_tck_to_trk.py

if [ -s track.trk ] 
then
	mkdir -p trk
	mv track.trk trk/track.trk
	echo 0 > finished
else
	echo "failed"
	echo 1 > finished
	exit 1
fi
