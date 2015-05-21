import sys

import os
import subprocess
import masspoints_2
import time
import math

localDir = "/home/ameliajb/workarea/SiMs_AtlasExternal_v2/"
MGdir = localDir + "MG5_aMC_v2_2_2/"
cutflowDir = localDir + "CutFlow/txt_outputs/"

# create the limits file
limits = localDir + "limits_store.txt"
with open(limits, "w") as f:
        f.write("This file is created with sigma_limit_script.py, it reads masses etc from masspoints_2.py, cross sections from the LHEs, acceptances from the Cutflow/txt_outputs/cutflow_output_XXX.txt outputs, and calculates the limit on sigma which is output to limits_store.txt. All values are in fb. 'stat-vary acc' is the acceptance varied downwards by the statistical uncertainty, stat_sig_obs and stat_f_obs are the limits calculated with this new acceptance.\n\n")

defs = ['SR', 'acceptance', 'sigma_lim_exp', 'sigma_lim_obs', 'f_est_exp', 'f_est_obs', 'stat-vary acc', 'stat_sig_obs', 'stat_f_obs']
with open(limits, "a") as f:
        f.write('{:<14}  {:<14}  {:<14}  {:<14}  {:<14}  {:<14}  {:<14}  {:<14}  {:<14}'.format(defs[0], defs[1], defs[2], defs[3], defs[4], defs[5], defs[6], defs[7], defs[8]))

lumi = 20.3
eff = 1.0		# TODO: an arbitrary efficiency for now

# extract f_gen from masspoints_2.py
f_gen = masspoints_2.couplings[0]

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

                                        print "Looking for baseName " + baseName

					with open(limits, "a") as f:
       						f.write("\n\n" + baseName + ": ")

					# this should be changed for mono-jet!
					events_file = MGdir + "SiM_" + modelType + "_monoZ_8TeV/Events/" + baseName + "/unweighted_events.lhe"
					if os.path.exists(events_file):

						with open(events_file) as g:
    							for line in g:
        							if 'Integrated weight' in line:
									line = line.replace(" ", "")
									i = line.index(':')		# position of :
									sigma_gen = float(line[i+1:])*pow(10,3)         # saving this as a float, scientific notation is handled
									xsec = str(sigma_gen)				# store as string for printing
            								break		# ensures doesn't continue reading the file after this line
                				with open(limits, "a") as f:
                        				f.write(" Xsec = " + xsec + ", ")
        				else:
               	 				with open(limits, "a") as f:
                        				f.write("can't find LHE!\n")				

					acc_file = cutflowDir + "cutflow_output_" + baseName + ".txt"
					if os.path.exists(acc_file):
				
						with open(acc_file) as h:
							# define dictionaries
							list_acc = {}
							sig_exp = {}
							sig_obs = {}
							f_exp = {}
							f_obs = {}
                                                        for line in h:
                                                                if 'nevent' in line:
									line = line.replace(" ", "")	# strip spaces
									i = line.index('s')
									j = len(line)
									nevent = line[i+1:j-1]
									with open(limits, "a") as f:
                                                                		f.write("nevents = " + nevent)
								for cut in ['150', '250', '350', '450']:
									if cut == '150':
                                                                                N_exp = 22.3
                                                                                N_obs = 20.9
                                                                        if cut == '250':
                                                                                N_exp = 8.6
                                                                                N_obs = 6.6
                                                                        if cut == '350':
                                                                                N_exp = 4.5
                                                                                N_obs = 3.0
                                                                        if cut == '450':
                                                                                N_exp = 3.4
                                                                                N_obs = 3.0

									if 'MET > ' + cut in line:
										line = line.replace(" ", "")
									 	i = line.index(':')
										j = len(line)
										acc = line[i+1:j-1]

										sigma_lim_exp = N_exp/(lumi * eff * float(acc))
										sigma_lim_obs = N_obs/(lumi * eff * float(acc))

										f_est_exp = f_gen * pow(sigma_lim_exp/sigma_gen,0.25)		# Note these are estimations of the limit on the coupling
										f_est_obs = f_gen * pow(sigma_lim_obs/sigma_gen,0.25)

										list_acc[cut] = acc
										sig_exp[cut] = sigma_lim_exp
										sig_obs[cut] = sigma_lim_obs
										f_exp[cut] = f_est_exp
										f_obs[cut] = f_est_obs

									if 'stat > ' + cut in line:
										line = line.replace(" ", "")
                                                                                i = line.index(':')
                                                                                j = len(line)
                                                                                stat_acc = line[i+1:j-1]
										# vary the nominal acceptance downwards, this will give a larger variation in sigma which is more conservative
										var_acc = float(list_acc[cut])- float(stat_acc)
										sigma_lim_obs_stat = N_obs/(lumi * eff * float(var_acc))
										f_est_obs_stat = f_gen * pow(sigma_lim_obs_stat/sigma_gen,0.25)


										# only do this once for each cut and file, so doing once the MET stat > cut line is found works well.
										output = ['MET > ' + cut, str(list_acc[cut]), str(round(sig_exp[cut], 2)), str(round(sig_obs[cut],2)), str(round(f_exp[cut], 4)), str(round(f_obs[cut], 4)), str(round(var_acc, 4)), str(round(sigma_lim_obs_stat, 2)), str(round(f_est_obs_stat,4))]
										line_new = '{:<14}  {:<14}  {:<14}  {:<14}  {:<14}  {:<14}  {:<14}  {:<14}  {:<14}'.format(output[0], output[1], output[2], output[3], output[4], output[5], output[6], output[7], output[8])
										with open(limits, "a") as f:
											f.write("\n" + line_new)

					else:
                                                with open(limits, "a") as f:
                                                        f.write("can't find cutflow output!\n") 	

					x = x + 1
