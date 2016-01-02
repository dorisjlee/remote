import sys
import os
# for example, reclone folder  from ramses5 to ramses
# enter : python  reclone.py 5 
num = int(sys.argv[2])
os.system("git clone https://bitbucket.org/rteyssie/ramses.git")
os.system("cp -r ~/project/ramses{}/trunk/ramses/patch/hydro/isothermal_sphere/ ~/project/ramses/trunk/ramses/patch/hydro/".format(num))
os.system("cp -r ramses{}/trunk/ramses/bin/Makefile  ramses/trunk/ramses/bin/".format(num))
os.system("cp -r ramses{}/trunk/ramses/bin/srun.pbs  ramses/trunk/ramses/bin/".format(num))

