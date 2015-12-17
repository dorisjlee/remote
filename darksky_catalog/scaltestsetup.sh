for k in $(seq 0 10) #50) # 136)
do
   #Call python script that generates output of new run.pbs
   #/global/homes/d/dorislee/anaconda/bin/python getscript_cori.py $k > run.pbs
   /global/homes/d/dorislee/anaconda/bin/python getscript.py $k > run.pbs
   echo "Submitting $k"
 #  sbatch run.pbs
   qsub run.pbs
done
