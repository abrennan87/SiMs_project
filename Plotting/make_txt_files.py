import sys, os, inspect, subprocess, time, math, operator

# want to import masspoints_2 which is in the parent directory. Do this by adding parent directory to the python path.
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
print parentdir
sys.path.insert(0,parentdir) 

import masspoints_2

localDir = "/home/ameliajb/workarea/SiMs_AtlasExternal_v2/"
MGdir = localDir + "MG5_aMC_v2_2_2/"
#limFile = localDir + "limits_store_SVD_Wmin.txt"
limFile = localDir + "limits_store_testing.txt"
storeDir = localDir + "Plotting/text_graphs/"

# loop through the limits_store file, break into chunks separated by the double line space. Each chunk has the form:

#SVD_10_10_min_rat02: Xsec = 39.804
#150         913.335229658         458.178754722         1371.51398438         855.995798199         429.414169224         1285.40996742         0.204333288623        0.0257266616102       0.230059950233        0.207672393821        0.0261470729396       0.233819466761

with open(limFile) as f:
    chunks = f.read().split('\n\n')                 

# creates empty dictionaries
sig_exp = {}
sig_exp_unc = {}
sig_obs = {}
sig_obs_unc = {}
f_exp_95 = {}
f_obs_95 = {}

# loop over the chunks - skip the first, since it is the header of the limits_store file.
for i,chunk in enumerate(chunks):
        if i > 1:
		print chunk
		# look at the first line of the chunk
                for row in chunk.split('\n')[0:1]:              # take the first line
			#extract the name (everything before the ':', so SVD_10_1000_1 or SVD_10_1000_1_PDF+tune_up forms both accepted
                        i = row.index(':')
                        name = row[:i]
                        print name
		# read the rest of the chunk (1 line), extract the useful values
                for row in chunk.split('\n')[1:]:               # skip the first line of the chunk
                        info = row.split()
			sig_exp[name] = float(info[1])
			sig_exp_unc[name] = float(info[2])
			sig_obs[name] = float(info[4])
			sig_obs_unc[name] = float(info[5])
			f_exp_95[name] = float(info[9])
			f_obs_95[name] = float(info[12])

# For each base name, create and fill text files with the graph values.
for modelType in masspoints_2.model:
        for iM in masspoints_2.Mdm:

		for iMe in masspoints_2.Mmed:
                        for iW in masspoints_2.widths:
                                for ratio in masspoints_2.coupling_ratio:
                                        rat_st = str(ratio).replace('.', '')
                                        base = modelType + '_' + iM + '_' + iMe + '_' + iW + '_rat' + rat_st
                                        # check if this set of variables is meant to be included or now - check if exists in MG output
                                        events_file = MGdir + "SiM_" + modelType + "_monoZ_8TeV/Events/" + base + "/unweighted_events.lhe"
                                        if not os.path.isfile(events_file):
                                                continue 
                                        # create a text file with the coupling limit as a function of med + DM masses. A different one for each model + width.
                                        flim_out = storeDir + "couplinglimits_" + modelType + "_" + iW + "_rat" + rat_st + ".txt"
                                        with open(flim_out, "a") as f:
                                                f.write(str(iM) + " " + str(iMe) + " " + str(f_obs_95[base]) + "\n")

                for iW in masspoints_2.widths:
			for ratio in masspoints_2.coupling_ratio:
                        	rat_st = str(ratio).replace('.', '')
                        	output_exp = storeDir + "limits_" + modelType + "_DM" + iM + "_" + iW + "_rat" + rat_st + "_exp.txt"
				output_obs = storeDir + "limits_" + modelType + "_DM" + iM + "_" + iW + "_rat" + rat_st + "_obs.txt"
				if os.path.isfile(output_exp): 
					os.system("rm " + output_exp)
				if os.path.isfile(output_obs): 
					os.system("rm " + output_obs) 
                        	for iMe in masspoints_2.Mmed:
                        	        # find the basename
                        	        base = modelType + '_' + iM + '_' + iMe + '_' + iW + '_rat' + rat_st
                        	        # find the dictionary entry for width
					# check if this set of variables is meant to be included or now - check if exists in MG output
                                        events_file = MGdir + "SiM_" + modelType + "_monoZ_8TeV/Events/" + base + "/unweighted_events.lhe"
                                        if not os.path.isfile(events_file):
                                                continue
                        	        with open(output_exp, "a") as g:
                        	                g.write(str(iMe) + " " + str(sig_exp[base]) + " 0 " + str(sig_exp_unc[base]) + "\n")
					with open(output_obs, "a") as h:
                                                h.write(str(iMe) + " " + str(sig_obs[base]) + " 0 " + str(sig_obs_unc[base]) + "\n")

	for iMe in masspoints_2.Mmed:
		for iW in masspoints_2.widths:
			for ratio in masspoints_2.coupling_ratio:
                                rat_st = str(ratio).replace('.', '')
				output_exp = storeDir + "limits_" + modelType + "_Med" + iMe + "_" + iW + "_rat" + rat_st + "_exp.txt"
				output_obs = storeDir + "limits_" + modelType + "_Med" + iMe + "_" + iW + "_rat" + rat_st + "_obs.txt"
				if os.path.isfile(output_exp): 
                                        os.system("rm " + output_exp)
                                if os.path.isfile(output_obs):
                                        os.system("rm " + output_obs)
				for iM in masspoints_2.Mdm:
					# find the basename
                        	        base = modelType + '_' + iM + '_' + iMe + '_' + iW + '_rat' + rat_st
					# check if this set of variables is meant to be included or now - check if exists in MG output
                                        events_file = MGdir + "SiM_" + modelType + "_monoZ_8TeV/Events/" + base + "/unweighted_events.lhe"
                                        if not os.path.isfile(events_file):
                                                continue
                        	        # find the dictionary entry for width
                        	        with open(output_exp, "a") as g:
                             	           g.write(str(iM) + " " + str(sig_exp[base]) + " 0 " + str(sig_exp_unc[base]) + "\n")
					with open(output_obs, "a") as h:
                                           h.write(str(iM) + " " + str(sig_obs[base]) + " 0 " + str(sig_obs_unc[base]) + "\n")
