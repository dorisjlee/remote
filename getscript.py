import sys

for arg in sys.argv: 
    nproc=arg
nproc = int(nproc)
print "#NPROC {} TEST".format(nproc)
print "#PBS -q regular"
print "#PBS -l mppwidth={}".format(((nproc/24)+1)*24)
print "#PBS -l walltime=05:00:00"
print "#PBS -N {}_test_L9_run3".format(nproc)
print "#PBS -e test.$PBS_JOBID.err"
print "#PBS -o test.$PBS_JOBID.out"
print "#PBS -A m2218"
print "module swap PrgEnv-gnu PrgEnv-intel"
print "cd /scratch2/scratchdirs/dorislee/3test{}".format(nproc)
print "pwd"
print "aprun -n {} /global/homes/d/dorislee/ramses/trunk/ramses/bin/ramses2d_mhd_otpatch ../orszag-tang.nml".format(nproc)
