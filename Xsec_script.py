import sys

import os
import subprocess
import masspoints_2
import time
import math

localDir = "/home/ameliajb/workarea/SiMs_AtlasExternal_v2/"
MGdir = localDir + "MG5_aMC_v2_2_2/"

# create the Xsec file
Xsec_script = localDir + "Xsec_store.txt"
with open(Xsec_script, "w") as f:
        f.write("This file is created with Xsec_script.py, it reads masses etc from masspoints_2.py and fills the cross sections by reading these from SiMs_XXX_monoZ_8TeV/Events/XXX/unweighted_events.lhe.\n\n")
	f.write("All values are in fb.\n\n")

# loop over models
for modelType in masspoints_2.model:
        for iM in masspoints_2.Mdm:
                fiM = float(iM)
                for iMe in masspoints_2.Mmed:
                        fiMe = float(iMe)
                        for iW in masspoints_2.widths:
				if masspoints_2.systematics == 0:
                                        num_scripts = 1
                                elif masspoints_2.systematics == 1:
                                        num_scripts = 2*len(masspoints_2.syst_list) + 1		# include the nominal value as well here
				x = 0
                                while (x < num_scripts):
					if x == 0:
						baseName = modelType + "_" + iM + "_" + iMe + "_" + iW
                                        else:
                                                iS = masspoints_2.syst_list[int(math.floor((x-1)/2))]
                                                if (x-1)%2 == 0:
                                                        iDir = '_up'
                                                else:
                                                        iDir = '_down'
                                                baseName = modelType + "_" + iM + "_" + iMe + "_" + iW + "_" + iS + iDir

                                        print "baseName is " + baseName

					with open(Xsec_script, "a") as f:
       						f.write(baseName + ": ")

					events_file = MGdir + "SiM_" + modelType + "_monoZ_8TeV/Events/" + baseName + "/unweighted_events.lhe"
					if os.path.exists(events_file):

						with open(events_file) as g:
    							for line in g:
        							if 'Integrated weight' in line:
									line = line.replace(" ", "")
									i = line.index(':')		# position of :
									xsec = str(float(line[i+1:])*1000)
            								break		# ensures doesn't continue reading the file after this line
                				with open(Xsec_script, "a") as f:
                        				f.write("               " + xsec + "\n")
        				else:
               	 				with open(Xsec_script, "a") as f:
                        				f.write("nonexistant!\n")					

					x = x + 1
