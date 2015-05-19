#########################################################################################
#											#
#											#
#											#
#   Jan 7, 2015. Amelia Brennan, Uni of Melbourne.					#
#											#
#											#
#   This script should read in masspoints.py, which contains the model type, masses     #
#   etc that are to be submitted. It should also have a list of options (MadGraph,      #
#   Pythia and HepMC2root) which can be switched on or off. For each instance, a        #
#   template script (Template_script.py) is copied, filled and submitted. This 		#
#   template script also reads in the list of options to determine which steps to run, 	#
#   and checks that each step can be run, ie that any required previous output is 	#
#   present. The template script also writes a tracking script, which notes at each 	#
#   point what step is being done, and can be used for debugging.			#
#											#
#											#
#   IMPORTANT: Before running for the first time in a new shell, ROOT and an updated    #
#   version of gfortran need to be set up. For Melbourne users, this is done in one     #
#   step with localSetupROOT. Note that the worker node to which the job is submitted   #
#   (and where MG is run) takes the environment from the local UI, ie localSetupROOT    #
#   needs to be run here for it to work on the worker node.				#
#											#
#   IMPORTANT 2: If the MG process has a jet (mono-jet, mono-W/Z (had)), make sure the  #
#   relevant run_card.dat has icwwk set to 1, and xqcut set to 150. For mono-Z, ickkw 	#
#   and xqcut should be set to 0.							#
#											#
#   TODO: Fix this after the matching scheme has been updated				#
#											#
#########################################################################################

import sys
print(sys.version)

import os
import subprocess
import masspoints
import time
import math

### IMPORTANT ###
# Before starting, make sure to run localSetupROOT (NO LONGER NEEDED: localSetupGcc gcc462_x86_64_slc6)

# start loop, define string, number names

homeDir = "/home/ameliajb/workarea/SiMs_AtlasExternal_v2/"
number_coupling = str(masspoints.couplings[0])		# coupling to DM
number_coupling2 = number_coupling			# coupling to SM, currently set equal to above
fg = float(masspoints.couplings[0])			# float value for width calculation
fg2 = pow(fg,2)						# squared, useful below

pi = 3.1415
m_u = 0.0023
m_d = 0.0048
m_c = 1.275
m_s = 0.095
m_t = 176.7
m_b = 4.18

for modelType in masspoints.model:
	for iM in masspoints.Mdm:
        	fiM = float(iM)
        	for iMe in masspoints.Mmed:
                	fiMe = float(iMe)
                	for iW in masspoints.widths:
				print 'iW is ' + iW
                        	if iW == 'M3':
					number_width = fiMe/3.
                        	elif iW == 'M8pi':
					number_width = fiMe/(8.*3.1415)
                        	elif iW == '1':
					number_width = 1.
                        	elif iW == 'min':
                                	if modelType == 'SSD':
						number_width = 0.
						if (fiMe >= 2*fiM):
							DM_piece = fiMe*fg2/(8*pi)*pow((1-4*pow(fiM,2)/(pow(fiMe,2))),1.5)
							number_width += DM_piece
						if (fiMe >= 2*m_u):
							u_piece = 3*fiMe*fg2/(8*pi)*pow((1-4*pow(m_u,2)/(pow(fiMe,2))),1.5);
							number_width += u_piece;
						if (fiMe >= 2*m_d):
                                                        d_piece = 3*fiMe*fg2/(8*pi)*pow((1-4*pow(m_d,2)/(pow(fiMe,2))),1.5);
                                                        number_width += d_piece;
						if (fiMe >= 2*m_c):
                                                        c_piece = 3*fiMe*fg2/(8*pi)*pow((1-4*pow(m_c,2)/(pow(fiMe,2))),1.5);
                                                        number_width += c_piece;
						if (fiMe >= 2*m_s):
                                                        s_piece = 3*fiMe*fg2/(8*pi)*pow((1-4*pow(m_s,2)/(pow(fiMe,2))),1.5);
                                                        number_width += s_piece;
						if (fiMe >= 2*m_t):
                                                        t_piece = 3*fiMe*fg2/(8*pi)*pow((1-4*pow(m_t,2)/(pow(fiMe,2))),1.5);
                                                        number_width += t_piece;
						if (fiMe >= 2*m_b):
                                                        b_piece = 3*fiMe*fg2/(8*pi)*pow((1-4*pow(m_b,2)/(pow(fiMe,2))),1.5);
                                                        number_width += b_piece;
						print 'width is calculated to be: ' + str(number_width)
					elif modelType == 'SVD':
						number_width = 0.
						if (fiMe >= 2*fiM):
							DM_piece = fiMe*fg2/(12*pi)*(1+2*pow(fiM,2)/(pow(fiMe,2)))*pow((1-4*pow(fiM,2)/(pow(fiMe,2))),0.5)
                                                        number_width += DM_piece
						if (fiMe >= 2*m_u):
							u_piece = 3*fiMe*fg2/(12*pi)*(1+2*pow(m_u,2)/(pow(fiMe,2)))*pow((1-4*pow(m_u,2)/(pow(fiMe,2))),0.5)
                                                        number_width += u_piece
						if (fiMe >= 2*m_d):
							d_piece = 3*fiMe*fg2/(12*pi)*(1+2*pow(m_d,2)/(pow(fiMe,2)))*pow((1-4*pow(m_d,2)/(pow(fiMe,2))),0.5)
							number_width += d_piece
						if (fiMe >= 2*m_c):
							c_piece = 3*fiMe*fg2/(12*pi)*(1+2*pow(m_c,2)/(pow(fiMe,2)))*pow((1-4*pow(m_c,2)/(pow(fiMe,2))),0.5)
                                                        number_width += c_piece
						if (fiMe >= 2*m_s):
							s_piece = 3*fiMe*fg2/(12*pi)*(1+2*pow(m_s,2)/(pow(fiMe,2)))*pow((1-4*pow(m_s,2)/(pow(fiMe,2))),0.5)
                                                        number_width += s_piece
						if (fiMe >= 2*m_t):
							t_piece = 3*fiMe*fg2/(12*pi)*(1+2*pow(m_t,2)/(pow(fiMe,2)))*pow((1-4*pow(m_t,2)/(pow(fiMe,2))),0.5)
                                                        number_width += t_piece
						if (fiMe >= 2*m_b):
							b_piece = 3*fiMe*fg2/(12*pi)*(1+2*pow(m_b,2)/(pow(fiMe,2)))*pow((1-4*pow(m_b,2)/(pow(fiMe,2))),0.5)
                                                        number_width += b_piece
						print 'width is calculated to be: ' + str(number_width)
					elif modelType == 'TSD':
						number_width_U = 0.
						number_width_D = 0.
						if ((pow(fiM,2) + pow(m_u,2) <= pow(fiMe,2)) and (pow((1-pow(m_u,2)/pow(fiMe,2) + pow(fiM,2)/pow(fiMe,2)),2) >= 4*pow(fiM,2)/pow(fiMe,2))):
							u_piece = fiMe*fg2/(16*pi)*(1-pow(m_u,2)/pow(fiMe,2) - pow(fiM,2)/pow(fiMe,2))*pow((pow((1-pow(m_u,2)/pow(fiMe,2) + pow(fiM,2)/pow(fiMe,2)),2) - 4*pow(fiM,2)/pow(fiMe,2)),0.5)
							number_width_U += u_piece
						if ((pow(fiM,2) + pow(m_d,2) <= pow(fiMe,2)) and (pow((1-pow(m_d,2)/pow(fiMe,2) + pow(fiM,2)/pow(fiMe,2)),2) >= 4*pow(fiM,2)/pow(fiMe,2))):
                                                        d_piece = fiMe*fg2/(16*pi)*(1-pow(m_d,2)/pow(fiMe,2) - pow(fiM,2)/pow(fiMe,2))*pow((pow((1-pow(m_d,2)/pow(fiMe,2) + pow(fiM,2)/pow(fiMe,2)),2) - 4*pow(fiM,2)/pow(fiMe,2)),0.5)
                                                        number_width_D += d_piece
						if ((pow(fiM,2) + pow(m_c,2) <= pow(fiMe,2)) and (pow((1-pow(m_c,2)/pow(fiMe,2) + pow(fiM,2)/pow(fiMe,2)),2) >= 4*pow(fiM,2)/pow(fiMe,2))):
                                                        c_piece = fiMe*fg2/(16*pi)*(1-pow(m_c,2)/pow(fiMe,2) - pow(fiM,2)/pow(fiMe,2))*pow((pow((1-pow(m_c,2)/pow(fiMe,2) + pow(fiM,2)/pow(fiMe,2)),2) - 4*pow(fiM,2)/pow(fiMe,2)),0.5)
                                                        number_width_U += c_piece
						if ((pow(fiM,2) + pow(m_s,2) <= pow(fiMe,2)) and (pow((1-pow(m_s,2)/pow(fiMe,2) + pow(fiM,2)/pow(fiMe,2)),2) >= 4*pow(fiM,2)/pow(fiMe,2))):
                                                        s_piece = fiMe*fg2/(16*pi)*(1-pow(m_s,2)/pow(fiMe,2) - pow(fiM,2)/pow(fiMe,2))*pow((pow((1-pow(m_s,2)/pow(fiMe,2) + pow(fiM,2)/pow(fiMe,2)),2) - 4*pow(fiM,2)/pow(fiMe,2)),0.5)
                                                        number_width_D += s_piece
						if ((pow(fiM,2) + pow(m_t,2) <= pow(fiMe,2)) and (pow((1-pow(m_t,2)/pow(fiMe,2) + pow(fiM,2)/pow(fiMe,2)),2) >= 4*pow(fiM,2)/pow(fiMe,2))):
                                                        t_piece = fiMe*fg2/(16*pi)*(1-pow(m_t,2)/pow(fiMe,2) - pow(fiM,2)/pow(fiMe,2))*pow((pow((1-pow(m_t,2)/pow(fiMe,2) + pow(fiM,2)/pow(fiMe,2)),2) - 4*pow(fiM,2)/pow(fiMe,2)),0.5)
                                                        number_width_U += t_piece
						if ((pow(fiM,2) + pow(m_b,2) <= pow(fiMe,2)) and (pow((1-pow(m_b,2)/pow(fiMe,2) + pow(fiM,2)/pow(fiMe,2)),2) >= 4*pow(fiM,2)/pow(fiMe,2))):
                                                        b_piece = fiMe*fg2/(16*pi)*(1-pow(m_b,2)/pow(fiMe,2) - pow(fiM,2)/pow(fiMe,2))*pow((pow((1-pow(m_b,2)/pow(fiMe,2) + pow(fiM,2)/pow(fiMe,2)),2) - 4*pow(fiM,2)/pow(fiMe,2)),0.5)
                                                        number_width_D += b_piece
						print 'width (EtaU) is calculated to be: ' + str(number_width_U)
						print 'width (EtaD) is calculated to be: ' + str(number_width_D)	
                                	else:   # Need to add other widths here!
						number_width = 1.
                                        	print 'Warning - using NWA (width = 1)'


				if (modelType == 'TSD' and iW == 'min'):
					width_U = "{0:.2f}".format(number_width_U)
					width_D = "{0:.2f}".format(number_width_D)
					print 'width_U is ' + width_U
					print 'width_D is ' + width_D
				else:
					width = "{0:.2f}".format(number_width)
					print 'width is ' + width

				if masspoints.systematics == 0:
					num_scripts = 1
				elif masspoints.systematics == 1:
					num_scripts = 2*len(masspoints.syst_list)
				else:
					print 'Do you want systematics on or not??'
					break

				print 'num_scripts is ' + str(num_scripts)

				x = 0
				while (x < num_scripts):
					if masspoints.systematics == 0:
						baseName = modelType + "_" + iM + "_" + iMe + "_" + iW
					else:
						iS = masspoints.syst_list[int(math.floor(x/2))]
						if x%2 == 0:
							iDir = '_up'
						else:
							iDir = '_down'
						baseName = modelType + "_" + iM + "_" + iMe + "_" + iW + "_" + iS + iDir

					print "baseName is " + baseName

					scriptName = "MC_generation_" + baseName + ".py"

					# Copy Template_script.py, rename it
                                	#if os.path.exists(homeDir + scriptName):
                                	#        print "MC generation script already exists, will not overwrite"
                                	#else:
                                	os.system("cp " + homeDir + "Template_script.py " + homeDir + scriptName)
					os.system("sed -i 's/BASENAME/" + baseName + "/g' " + homeDir + scriptName)
					os.system("sed -i 's/MODELTYPE/" + modelType + "/g' " + homeDir + scriptName)
                                	os.system("sed -i 's/MDM_str/" + iM + "/g' " + homeDir + scriptName)
                                	os.system("sed -i 's/MMED_str/" + iMe + "/g' " + homeDir + scriptName)
                                	os.system("sed -i 's/WIDTH_str/" + iW + "/g' " + homeDir + scriptName)
                                	os.system("sed -i 's/COUPLING_DM/" + number_coupling + "/g' " + homeDir + scriptName)
                                	os.system("sed -i 's/COUPLING_SM/" + number_coupling2 + "/g' " + homeDir + scriptName)
                                	os.system("sed -i 's/MDM_num/" + str(fiM) + "/g' " + homeDir + scriptName)
                                	os.system("sed -i 's/MMED_num/" + str(fiMe) + "/g' " + homeDir + scriptName)
					if modelType == 'TSD':
						if iW == 'min':
							os.system("sed -i 's/WIDTH_U_num/" + width_U + "/g' " + homeDir + scriptName)
							os.system("sed -i 's/WIDTH_D_num/" + width_D + "/g' " + homeDir + scriptName)
						else:
							os.system("sed -i 's/WIDTH_U_num/" + width + "/g' " + homeDir + scriptName)
                                                        os.system("sed -i 's/WIDTH_D_num/" + width + "/g' " + homeDir + scriptName)
					else:
                                		os.system("sed -i 's/WIDTH_num/" + width + "/g' " + homeDir + scriptName)

					########################  Submit job  ########################

					scrDir = "." #directory where your run script is
        	                	logDir = "./logFiles/"  #directory for log files
                	        	script = scriptName #name of the script to submit
                        		jobName = "MCGenJob" #"RecoJob"; #"EvGenJob"; #job name to appear on the queue and log files

	                        	# selection of queue
        	                	#queue = "mel_short"
                	        	#walt = "walltime=01:00:00"
					queue = "mel_long"
                                        walt = "walltime=24:00:00"

					#os.system("qsub -q " + queue + " -l " + walt + " -V -N " + jobName + " -e " + logDir + " -o " + logDir + " " + scrDir + "/" + script)	
	                       		os.system("qsub -q " + queue + " -l " + walt + " -l ncpus=6 -V -N " + jobName + " -e " + logDir + " -o " + logDir + " " + scrDir + "/" + script)	# will only run if 6 cpus available

					os.system("mv " + scriptName + " batch_scripts/")

				 	#time.sleep(2.7)	# ~3 seconds between each job submission as a precaution against running two similar instances of MadGraph simultaneously	
					x = x + 1
