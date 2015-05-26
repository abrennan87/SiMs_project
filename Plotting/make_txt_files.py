import sys, os, inspect, subprocess, time, math, operator

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

# loop through the limits_store file, break into chunks separated by the double line space. Each chunk has the form:

#SVD_400_1000_1_scale_down:  Xsec = 475.55, nevents = 10000
#MET > 150       0.0531          20.69           19.39           0.4567          0.4494
#MET > 250       0.0128          33.1            25.4            0.5136          0.4807
#MET > 350       0.0044          50.38           33.59           0.5705          0.5155
#MET > 450       0.001           167.49          147.78          0.7704          0.7466

with open(limFile) as f:
    chunks = f.read().split('\n\n')                 # skip the first 7 lines of the file - not interesting

# creates empty dictionaries. sigma_by_name will be filled by 'name : sigma_obs', where sigma_obs is the lowest of the four values of sigma_obs from four signal regions, when name does not include a systematic variance (eg 'SVD_10_200_min'). If it does (ie 'SVD_10_200_min_scale_up'), the value is instead the sigma_obs in the SR that is found to give the best value for the nominal name (SVD_10_200_min). For example, if SVD_10_200_min has the best limit in SR2, SVD_10_200_min_scale_up will extract the limit in SR2 regardless of whether this is the best limit (though usually it should match up). SR_by_name just stores the SR for each nominal value.
sigma_by_name = {}
coupling_by_name = {}
SR_by_name = {}
stat_sigma = {}

# loop over the chunks - skip the first, since it is the header of the limits_store file.
for i,chunk in enumerate(chunks):
        if i > 1:
                min_sigma = 1000000
		j = 0
		j_min = 0
		# look at the first line of the chunk
                for row in chunk.split('\n')[0:1]:              # take the first line
                        print row
			#extract the name (everything before the ':', so SVD_10_1000_1 or SVD_10_1000_1_PDF+tune_up forms both accepted
                        i = row.index(':')
                        name = row[:i]
                        print name
			# if it's a systematic sample, extract the base part of the name
			short_name = '_'.join(name.split('_')[:4])
		# read the rest of the lines in the chunk, extract the fifth element (sigma_obs), compare to sigma_lim. Also store the SR which gives the minimum value.
                for row in chunk.split('\n')[1:]:               # skip the first line of the chunk
			j = j + 1
                        info = row.split()
			# info[5] is the value of sigma_obs from that line
                        #print info[5]
			# only do comparison with min_sigma if NOT a systematic sample
			if ('up' not in name and 'down' not in name):
				# compare with min_sigma, fill min_sigma if smaller. Also store j which refers to the appropriate signal region (j=1 -> SR1, for eg).
                        	if (float(info[5]) < min_sigma):
                                	min_sigma = float(info[5])
					min_couple = float(info[7])
					j_min = j
					sigma_stat = float(info[9])
				
			else:
				# if it is a systematic sample, compares the row number (as loops from row 1 (SR1) to row 4(for SR4)) with j_min found above for the relevant non-syst sample. This obtains the corresponding value for the systematic, and fills sigma_by_name.
				if (j == int(SR_by_name[short_name])):
					sigma_by_name[name] = info[5]
		# fills the dictionary with the name and the min_sigma.
		if ('up' not in name and 'down' not in name):
                	sigma_by_name[name] = str(min_sigma)
			SR_by_name[name] = str(j_min)
			stat_sigma[name] = str(sigma_stat)
			coupling_by_name[name] = str(min_couple)

		#print 'sigma_by_name[' + name + ']: ' + sigma_by_name[name]

# Now for each base name, define the total systematic. Do this by looping over the systematic types, and taking the largest difference from the nominal between the 'up' and 'down' variations. Add this difference in quadrature.
err_by_name = {}			
for modelType in masspoints_2.model:
        for iM in masspoints_2.Mdm:
		for iMe in masspoints_2.Mmed:
			for iW in masspoints_2.widths:
				total_err_sq = 0.
				base = modelType + '_' + iM + '_' + iMe + '_' + iW 
				# add the statistical error in quad
				stat_err_2 = pow(abs(float(stat_sigma[base]) - float(sigma_by_name[base])),2)
				total_err_sq += stat_err_2
				print 'total_err_sq = ' + str(total_err_sq)
				for iSyst in masspoints_2.syst_list:
					max_diff = 0
					for dir in ['up', 'down']:
						fullname = base + '_' + iSyst + '_' + dir
						nominal = float(sigma_by_name[base])
						var = float(sigma_by_name[fullname])
						diff = abs(var - nominal)
						if diff > max_diff:
							max_diff = diff
					max_diff_sq = pow(max_diff,2)
					total_err_sq += max_diff_sq
					print 'iSyst: ' + iSyst
					print 'total_err_sq = ' + str(total_err_sq)
				total_err = pow(total_err_sq, 0.5)
				print 'final total_err_sq = ' + str(total_err_sq)
				print total_err
				err_by_name[base] = total_err
				# also, create a text file with the coupling limit as a function of med + DM masses. A different one for each model + width.
				flim_out = storeDir + "couplinglimits_" + modelType + "_" + iW + ".txt"
				with open(flim_out, "a") as f:
					f.write(str(iM) + " " + str(iMe) + " " + str(coupling_by_name[base]) + "\n")
						

for modelType in masspoints_2.model:
        for iM in masspoints_2.Mdm:
                for iW in masspoints_2.widths:
                        output = storeDir + "limits_" + modelType + "_DM" + iM + "_" + iW + ".txt"
			os.system("rm " + output) 
                        for iMe in masspoints_2.Mmed:
                                # find the basename
                                base = modelType + '_' + iM + '_' + iMe + '_' + iW
                                # find the dictionary entry for width
                                sigma_lim = sigma_by_name[base]
                                with open(output, "a") as g:
                                        g.write(str(iMe) + " " + sigma_lim + " 0 " + str(err_by_name[base]) + "\n")

	for iMe in masspoints_2.Mmed:
		for iW in masspoints_2.widths:
			output = storeDir + "limits_" + modelType + "_Med" + iMe + "_" + iW + ".txt"
			os.system("rm " + output)
			for iM in masspoints_2.Mdm:
				# find the basename
                                base = modelType + '_' + iM + '_' + iMe + '_' + iW
                                # find the dictionary entry for width
                                sigma_lim = sigma_by_name[base]
                                with open(output, "a") as g:
                                        g.write(str(iM) + " " + sigma_lim + " 0 " + str(err_by_name[base]) + "\n")
