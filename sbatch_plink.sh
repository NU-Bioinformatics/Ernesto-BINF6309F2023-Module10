#!/usr/bin/env bash
# sbatch_plink.sh

#!/bin/bash
#SBATCH --partition=express # choose from debug, express, or short
#SBATCH --job-name=plink # change this name to be informative for what you are running (eg. name of key script)
#SBATCH --time=00:30:00 # max time to run in hh:mm:ss, must be at or below max for partition
#SBATCH -N 1 # nodes requested
#SBATCH -n 1 # task per node requested
#SBATCH --output="batch-%x-%j.output" # where to direct standard output
# output file will be batch-<job-name>-<job-ID>.output and include stdout and stderr

# Core script
echo "Starting script $(date)"

echo "Loading required modules"
module load anaconda3/2021.11
module load binf6309/01-14-2022
source activate BINF-12-2021

bash getExamples.sh

bash plinkHapmap1.sh

echo "analysis complete $(date)"
