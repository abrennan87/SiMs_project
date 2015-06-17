import sys

import os
import subprocess
#import masspoints_2
import time
import math

# list below should be completed
modelType = 'SVD'
points = ['SVD_10_10_min_rat', 'SVD_200_500_min_rat']#, 'SVD_10_200_min_rat02', 'SVD_200_500_min_rat02']
ratio = [0.2, 2]
systs = ['scale']
gq_nom = 1

localDir = "/home/ameliajb/workarea/SiMs_AtlasExternal_v2/"
MGdir = localDir + "MG5_aMC_v2_2_2/"
cutflowDir = localDir + "CutFlow/txt_outputs/"

# create the limits file
#limits = localDir + "limits_store_SVD_Wmin.txt"
limits = localDir + "limits_store_testing.txt"
with open(limits, "w") as f:
        f.write("This file is created with sigma_limit_script.py, it reads the sample names in from above (ie, NOT from masspoints(_2).py), cross sections from the LHEs, acceptances from the Cutflow/txt_outputs/cutflow_output_XXX.txt outputs, and calculates the limit on sigma and the coupling (sqrt(g_chi*g_q) = g_q*sqrt(rat)).\n\n")

defs = ['best SR', 'sig_lim_exp', 'del_sig_lim_exp', 'sig_lim_exp_95syst', 'sig_lim_obs', 'del_sig_lim_obs', 'sig_lim_obs_95syst', 'f_lim_exp_95', 'del_f_lim_exp', 'f_lim_exp_95syst', 'f_lim_obs_95', 'del_f_lim_obs', 'f_lim_obs_95syst']
with open(limits, "a") as f:
        f.write('{:<10}  {:<20}  {:<20}  {:<20}  {:<20}  {:<20}  {:<20}  {:<20}  {:<20}  {:<20}  {:<20}  {:<20}  {:<20}'.format(defs[0], defs[1], defs[2], defs[3], defs[4], defs[5], defs[6], defs[7], defs[8], defs[9], defs[10], defs[11], defs[12]))

lumi = 20.3
eff = 1.0		# TODO: an arbitrary efficiency for now
N_exp = {'150': 22.3, '250': 8.6, '350':4.5, '450': 3.4}
N_obs = {'150': 20.9, '250': 6.6, '350': 3.0, '450': 3.0} 
delN = 0 # TODO find a value for this, or define a dictionary (more likely)
delN_obs = 0

# define the dictionaries
acc = {}
acc_stat = {}
sig_gen = {}
best_SR = {}

for name in points:
	for rat in ratio:
		ratstr = str(rat).replace('.', '')
		num_scripts = 2*len(systs) + 1
		x = 0
		while (x < num_scripts):
			x = x+1
			if (x-1) == 0:
				baseName = name + ratstr
			else:
				if (x-2)%2 == 0:
					baseName = name + ratstr + '_' + systs[int(math.floor((x-2)/2))] + '_up'
				else:
					baseName = name + ratstr + '_' + systs[int(math.floor((x-2)/2))] + '_down'

        	       	print "Looking for baseName " + baseName

			# want to continue if it can't find a sample
			events_file = MGdir + "SiM_" + modelType + "_monoZ_8TeV/Events/" + baseName + "/unweighted_events.lhe"
			if not os.path.isfile(events_file):
				print "Can't find LHE for " + baseName + "! Continuing..."
				continue
		
			#with open(limits, "a") as f:
       			#	f.write("\n\n" + baseName + ": ")

			if os.path.exists(events_file):
				with open(events_file) as g:
    					for line in g:
        					if 'Integrated weight' in line:
							line = line.replace(" ", "")
							i = line.index(':')				# position of :
							sigma_gen = float(line[i+1:])*pow(10,3)         # saving this as a float, scientific notation is handled
							xsec = str(sigma_gen)				# store as string for printing
        	    					break						# ensures doesn't continue reading the file after this line
        	        	#with open(limits, "a") as f:
        	                #	f.write(" Xsec = " + xsec + ", ")

				# define the dictionary entry
				sig_gen[baseName] = sigma_gen
        		#else:
        	       		#with open(limits, "a") as f:
        	        	#	f.write("can't find LHE!\n")				
	
			acc_file = cutflowDir + "cutflow_output_" + baseName + ".txt"

			# define a value for the limit on sigma in the best SR, define to be very large so will be easily replaced by a smaller value
			bestSR = 'noSR'
        	        bestSR_val = 10000

			if os.path.exists(acc_file):
				with open(acc_file) as h:
        	                	for line in h:
        	                        	if 'nevent' in line:
							line = line.replace(" ", "")	# strip spaces
							i = line.index('s')
							j = len(line)
							nevent = line[i+1:j-1]
							#with open(limits, "a") as f:
        	                                   	#	f.write("nevents = " + nevent)
						for cut in ['150', '250', '350', '450']:
							if 'MET > ' + cut in line:
								line = line.replace(" ", "")
							 	i = line.index(':')
								j = len(line)
								acc_val = line[i+1:j-1]
	
								# fill dictionary entry
								acc[baseName+cut] = float(acc_val)
	
								# for nominal value, find the best SR and store
								print 'x: ' + str(x)
								if x==1:
									if (float(acc_val)==0):
										sigma_lim_exp = 0.
									else:
										sigma_lim_exp = N_exp[cut]/(lumi * eff * float(acc_val))
										print 'sigma_lim_exp: ' + str(sigma_lim_exp)
										if sigma_lim_exp < bestSR_val:
											print 'lower sigma value'
											print 'bestSR is ' + bestSR
											bestSR = cut
											bestSR_val = sigma_lim_exp
											print 'bestSR is now ' + bestSR
	
							if 'stat > ' + cut in line:
								line = line.replace(" ", "")
        	                                                i = line.index(':')
        	                       	                        j = len(line)
        	                       	                        stat_acc = line[i+1:j-1]
								acc_stat[baseName + cut] = float(stat_acc)
	
						best_SR[baseName] = bestSR

# define useful dictionaries 
del_sig_gen = {}
A_nom_p_systs = {}
del_Ap = {}

for sh_name in points:
	for rat in ratio:
		ratstr = str(rat).replace('.', '')
		name = sh_name + ratstr
		#print 'sig_gen[' + name + ']: ' + sig_gen[name]
		#print 'acc[' + name + '150]: ' + acc[name + '150']
		#print 'acc_stat[' + name + '150]: ' + acc_stat[name + '150']
		#print 'acc[' + name + '250]: ' + acc[name + '250']
        	#print 'acc_stat[' + name + '250]: ' + acc_stat[name + '250']
		#print 'acc[' + name + '350]: ' + acc[name + '350']
        	#print 'acc_stat[' + name + '350]: ' + acc_stat[name + '350']
		#print 'acc[' + name + '450]: ' + acc[name + '450']
        	#print 'acc_stat[' + name + '450]: ' + acc_stat[name + '450']
		#print 'best_SR[' + name + ']: ' + best_SR[name]
		#print 'In best SR, the acc and stat are: ' + acc[name + best_SR[name]] + ', ' + acc_stat[name + best_SR[name]]
	
		# A_nom_p is the nominal acceptance - the stat error
		A_nom_p = max(0, acc[name + best_SR[name]] - acc_stat[name + best_SR[name]])	# set to 0 is acc_stat > acc

		# sig_lim_95 is the limit on sigma calculated with A_nom_p, ie it is the limit with the statistical uncertainty included but not the systematics. sig_lim is the limit calculated with the nominal acceptance.
		# f_lim_95 is the same but for the coupling. Here, f = sqrt(g_q g_chi) = g_q * sqrt(ratio).
		if A_nom_p == 0:
			print 'No limits exist for ' + name
			break
		else:
			sig_lim = N_exp[best_SR[name]] / (lumi * eff * acc[name + best_SR[name]])
			sig_lim_obs = N_obs[best_SR[name]] / (lumi * eff * acc[name + best_SR[name]])
			sig_lim_95 = N_exp[best_SR[name]] / (lumi * eff * A_nom_p)
			sig_lim_95_obs = N_obs[best_SR[name]] / (lumi * eff * A_nom_p)
			f_lim_95 = gq_nom * pow(rat, 0.5) * pow(sig_gen[name]/sig_lim_95, 0.25)
			f_lim_95_obs = gq_nom * pow(rat, 0.5) * pow(sig_gen[name]/sig_lim_95_obs, 0.25)
		del_sig_gen_tot = 0
		del_Ap_tot = 0
		for iS in systs:
			for iD in ['_up', '_down']:
				#print 'sig_gen[' + name + '_' + iS + iD + ']: ' + sig_gen[name + '_' + iS + iD]
				#print 'acc[' + name + '_' + iS + iD + '150]: ' + acc[name + '_' + iS + iD + '150']
				#print 'acc_stat[' + name + '_' + iS + iD + '150]: ' + acc_stat[name + '_' + iS + iD + '150']
        	                #print 'acc[' + name + '_' + iS + iD + '250]: ' + acc[name + '_' + iS + iD + '250']
        	                #print 'acc_stat[' + name + '_' + iS + iD + '250]: ' + acc_stat[name + '_' + iS + iD + '250']
        	                #print 'acc[' + name + '_' + iS + iD + '350]: ' + acc[name + '_' + iS + iD + '350']
        	                #print 'acc_stat[' + name + '_' + iS + iD + '350]: ' + acc_stat[name + '_' + iS + iD + '350']
        	                #print 'acc[' + name + '_' + iS + iD + '450]: ' + acc[name + '_' + iS + iD + '450']
        	                #print 'acc_stat[' + name + '_' + iS + iD + '450]: ' + acc_stat[name + '_' + iS + iD + '450']
	
				A_nom_p_systs[iS + iD] = str(float(acc[name + '_' + iS + iD + best_SR[name]]) - float(acc_stat[name + '_' + iS + iD + best_SR[name]]))

			# find the syst components for sig_gen
			del_sig_gen[iS] = (math.fabs(float(sig_gen[name + '_' + iS + '_up']) - float(sig_gen[name])) + math.fabs(float(sig_gen[name + '_' + iS + '_down']) - float(sig_gen[name])))/2
			del_sig_gen_tot += pow(del_sig_gen[iS],2)

			# find the syst components for del(A')
			del_Ap[iS] = (math.fabs(float(A_nom_p_systs[iS + '_up']) - A_nom_p) + math.fabs(float(A_nom_p_systs[iS + '_down']) - A_nom_p))/2
			del_Ap_tot += pow(del_Ap[iS], 2)
	
		# take the square root of the sum of the pieces of del_sig_gen and of del_Ap_tot
		del_sig_gen_tot = pow(del_sig_gen_tot, 0.5)
		del_Ap_tot = pow(del_Ap_tot, 0.5)
	
		# define the final limits
		# TODO: add the obs values as well
		del_sig_lim_95 = sig_lim_95 * pow(pow(del_Ap_tot/A_nom_p, 2) + pow(delN/N_exp[best_SR[name]],2), 0.5)
		del_sig_lim_95_obs = sig_lim_95_obs * pow(pow(del_Ap_tot/A_nom_p, 2) + pow(delN_obs/N_obs[best_SR[name]],2), 0.5)
		sig_lim_95_syst = sig_lim_95 + del_sig_lim_95
		sig_lim_95_syst_obs = sig_lim_95_obs + del_sig_lim_95_obs

		del_f_lim_95 = f_lim_95 / 4 * pow(pow(del_sig_gen_tot/sig_gen[name], 2) + pow(del_sig_lim_95/sig_lim_95, 2), 0.5)
		del_f_lim_95_obs = f_lim_95_obs / 4 * pow(pow(del_sig_gen_tot/sig_gen[name], 2) + pow(del_sig_lim_95_obs/sig_lim_95_obs, 2), 0.5)
		f_lim_95_syst = f_lim_95 + del_f_lim_95
		f_lim_95_syst_obs = f_lim_95_obs + del_f_lim_95_obs

		# for the sigma limit plots, we want the nominal value +/- the uncertainty, where the uncertainty includes both stat and syst uncertainties. Calculate this by subtracting the nominal value from sig_lim_95_syst.
		del_sig_lim = math.fabs(sig_lim_95_syst - sig_lim)
		del_sig_lim_obs = math.fabs(sig_lim_95_syst_obs - sig_lim_obs)

		print 'sig_lim_95_syst: ' + str(sig_lim_95_syst)
		print 'f_lim_95_syst: ' + str(f_lim_95_syst)
		print 'sig_lim_95_syst_obs: ' + str(sig_lim_95_syst_obs)
                print 'f_lim_95_syst_obs: ' + str(f_lim_95_syst_obs)
	
		output = [best_SR[name], str(sig_lim), str(del_sig_lim), str(sig_lim_95_syst), str(sig_lim_obs), str(del_sig_lim_obs), str(sig_lim_95_syst_obs), str(f_lim_95), str(del_f_lim_95), str(f_lim_95_syst), str(f_lim_95_obs), str(del_f_lim_95_obs), str(f_lim_95_syst_obs)] 
		line_new = '{:<10}  {:<20}  {:<20}  {:<20}  {:<20}  {:<20}  {:<20}  {:<20}  {:<20}  {:<20}  {:<20}  {:<20}  {:<20}'.format(output[0], output[1], output[2], output[3], output[4], output[5], output[6], output[7], output[8], output[9], output[10], output[11], output[12])
		with open(limits, "a") as f:
			f.write("\n\n" + name + ": Xsec = " + str(sig_gen[name]))
			f.write("\n" + line_new)

											# fill dictionary entry
											#acc_stat[baseName + cut] = str

											# vary the nominal acceptance downwards, this will give a larger variation in sigma which is more conservative
											#var_acc = abs(float(list_acc[cut])- float(stat_acc))		# inserted abs here for temp fix - NEED TO FIX THIS
											#print str(list_acc[cut]) + ' ' + str(stat_acc)		# problem here is that stat_acc > list_acc for SR4 - how to handle this??
											#if (float(var_acc)==0):
											#	sigma_lim_obs_stat = 0
											#else:
											#	sigma_lim_obs_stat = N_obs/(lumi * eff * float(var_acc))
											#f_est_obs_stat = f_gen * pow(sigma_lim_obs_stat/sigma_gen,0.25)

											# re-write this code - store the above as a dictionary


											# only do this once for each cut and file, so doing once the MET stat > cut line is found works well.
											#output = ['MET > ' + cut, str(list_acc[cut]), str(round(sig_exp[cut], 2)), str(round(sig_obs[cut],2)), str(round(f_exp[cut], 4)), str(round(f_obs[cut], 4)), str(round(var_acc, 4)), str(round(sigma_lim_obs_stat, 2)), str(round(f_est_obs_stat,4))]
											#line_new = '{:<20}  {:<20}  {:<20}  {:<20}  {:<20}  {:<20}  {:<20}  {:<20}  {:<20}'.format(output[0], output[1], output[2], output[3], output[4], output[5], output[6], output[7], output[8])
											#with open(limits, "a") as f:
											#	f.write("\n" + line_new)

#						else:
#                                        	        with open(limits, "a") as f:
#                                        	                f.write("can't find cutflow output!\n") 	

