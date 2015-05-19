import sys, os, inspect, subprocess, time, math

# want to import masspoints_2 which is in the parent directory. Do this by adding parent directory to the python path.
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
print parentdir
sys.path.insert(0,parentdir) 

import masspoints_2

localDir = "/home/ameliajb/workarea/SiMs_AtlasExternal_v2/"
limFile = localDir + "limits_store.txt"
storeDir = localDir + "Plotting/text_graphs/"

# create a dictionary from the limits_store.txt file, with the sample name and the minimum sigma limit
with open(limFile) as f:
    chunks = f.read().split('\n\n')                 # skip the first 7 lines of the file - not interesting

sigma_by_name = {}

for i,chunk in enumerate(chunks):
        if i > 1:
                min_sigma = 1000000
                for row in chunk.split('\n')[0:1]:              # take the first line
                        print row
                        i = row.index(':')
                        name = row[:i]
                        print name
                for row in chunk.split('\n')[1:]:               # skip the first line of the chunk
                        info = row.split()
                        print info[5]
                        if (float(info[5]) < min_sigma):
                                min_sigma = float(info[5])
                sigma_by_name[name] = str(min_sigma)

for modelType in masspoints_2.model:
        for iM in masspoints_2.Mdm:
                for iW in masspoints_2.widths:
                        output = storeDir + "limits_" + modelType + "_DM" + iM + "_" + iW + ".txt"
                        for iMe in masspoints_2.Mmed:
                                # find the basename
                                base = modelType + '_' + iM + '_' + iMe + '_' + iW
                                # find the dictionary entry for width
                                sigma_lim = sigma_by_name[base]
                                with open(output, "a") as g:
                                        g.write(str(iMe) + " " + sigma_lim + "\n")

	for iMe in masspoints_2.Mmed:
		for iW in masspoints_2.widths:
			output = storeDir + "limits_" + modelType + "_Med" + iMe + "_" + iW + ".txt"
			for iM in masspoints_2.Mdm:
				# find the basename
                                base = modelType + '_' + iM + '_' + iMe + '_' + iW
                                # find the dictionary entry for width
                                sigma_lim = sigma_by_name[base]
                                with open(output, "a") as g:
                                        g.write(str(iM) + " " + sigma_lim + "\n")
