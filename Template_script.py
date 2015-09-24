#!/usr/bin/python
import os
import os.path
import subprocess
import datetime
import time
import sys
sys.path.append('/home/ameliajb/workarea/SiMs_AtlasExternal_v2/')

qcut_num = MDM_num/4
channel = 'CHANNEL'
runMG = RUNMG
runPythia = RUNPYTHIA
runCon = RUNCON
runCF = RUNCF
runSysts = RUNSYSTS


#dateandtime = str(datetime.datetime.now().strftime("%d%b%Y_%H.%M"))
outputName = "BASENAME"

localDir = "/home/ameliajb/workarea/SiMs_AtlasExternal_v2/"
trackStore = localDir + "tracking_scripts/"

track_script = localDir + "track_" + outputName + ".txt"
with open(track_script, "w") as f:
	f.write("Reading masspoints.py...\n")
	f.write("MadGraph = " + str(runMG) + "\n")
	f.write("Pythia = " + str(runPythia) + "\n")
	f.write("HepMC2root = " + str(runCon) + "\n")
	f.write("Cutflow = " + str(runCF) + "\n\n")

	f.write("Channel = mono" + channel + "\n")
	f.write("qcut_num = " + str(qcut_num) + "\n\n")
	
	f.write("Using systematics?... ")
	if runSysts == 1:
		f.write("Yes.\n\n")
	else:
		f.write("No.\n\n")

###############################      Running MadGraph      ################################

mgDirGen = localDir + "MG5_aMC_v2_2_2/"
mgDirGen2 = localDir + "MG5_aMC_v2_2_2_slim/"
if channel == 'Z':
	mgModelTem = mgDirGen + "SiM_MODELTYPE_monoZ_8TeV/"		# For mono-Z processes
elif channel == 'jet':
	mgModelTem = mgDirGen + "SiM_MODELTYPE_monojet_8TeV/"		# For mono-jet processes
else:
	sys.exit('What channel are you studying?? - abort!')
scriptDir = os.getenv("PBS_O_WORKDIR")
print "PBS_O_WORKDIR is " + str(scriptDir)

if runMG == 1:

	# make a temp directory
	tmp = subprocess.Popen(["mktemp -d --suffix=_ABrennan"], stdout=subprocess.PIPE, shell=True)
	(tmpdir, err) = tmp.communicate()
	tmpdir = tmpdir.strip()
	tmpdir = tmpdir + "/"
	node = subprocess.Popen(["hostname"], stdout=subprocess.PIPE, shell=True)
	(hostnode, err) = node.communicate()
	with open(track_script, "a") as f:
		f.write("Current time: " + str(datetime.datetime.now().strftime("%d%b%Y_%H.%M")) + "\n")
                f.write("Temp directory is " + tmpdir + ", on the node " + hostnode + "\n")
		f.write("Copying MadGraph and LHAPDF directories to temp folder... ")

        # copy all of MadGraph to here, and all of LHAPDF
	os.system("cp -r " + mgDirGen2 + " " + tmpdir)
	os.system("cp -r " + localDir + "LHAPDF_all/ " + tmpdir)

	with open(track_script, "a") as f:
                f.write("done.\n")

	# define this as the base directory - note that if there are problems, or want to run locally, we can just set mgModelTemTmp to mgModelTem
	mgDirGenTmp = tmpdir + "MG5_aMC_v2_2_2_slim/"
	if channel == 'Z':
		mgModelTemTmp = mgDirGenTmp + "SiM_MODELTYPE_monoZ_8TeV/" 		# For mono-Z processes
	elif channel == 'jet':
		mgModelTemTmp = mgDirGenTmp + "SiM_MODELTYPE_monojet_8TeV/"		# For mono-jet processes	

	with open(track_script, "a") as f:
		f.write("Creating param_card.dat.\n")

	# check the location is fixed
	# Cp the template param_card.dat in the folder, fill the parameters as desired
	os.system("cp " + mgModelTemTmp + "Cards/param_card_template.dat " + mgModelTemTmp + "Cards/param_card.dat")
	# change this to copying madgraph, remove the check
	os.system("sed -i 's/gxichi/COUPLING_DM/g' " + mgModelTemTmp + "Cards/param_card.dat")
	os.system("sed -i 's/gxiQ/COUPLING_SM/g' " + mgModelTemTmp + "Cards/param_card.dat")
	os.system("sed -i 's/M_med/MMED_num/g' " + mgModelTemTmp + "Cards/param_card.dat")
	os.system("sed -i 's/M_DM/MDM_num/g' " + mgModelTemTmp + "Cards/param_card.dat")
	if 'MODELTYPE' == 'TSD':
		os.system("sed -i 's/W_etaD/WIDTH_D_num/g' " + mgModelTemTmp + "Cards/param_card.dat")
		os.system("sed -i 's/W_etaU/WIDTH_U_num/g' " + mgModelTemTmp + "Cards/param_card.dat")
                os.system("sed -i 's/W_etaS/WIDTH_S_num/g' " + mgModelTemTmp + "Cards/param_card.dat")
                os.system("sed -i 's/W_etaC/WIDTH_C_num/g' " + mgModelTemTmp + "Cards/param_card.dat")
                os.system("sed -i 's/W_etaB/WIDTH_B_num/g' " + mgModelTemTmp + "Cards/param_card.dat")
                os.system("sed -i 's/W_etaT/WIDTH_T_num/g' " + mgModelTemTmp + "Cards/param_card.dat")
	else:
		os.system("sed -i 's/W_xi/WIDTH_num/g' " + mgModelTemTmp + "Cards/param_card.dat")
	# No need to store these param_cards (which are copied over each new run), as they are copied in the output LHE file. 

	# Cp the template run_card.dat in the folder, just to ensure the default parameters are set. This is a redundancy, as below.
        os.system("cp " + mgModelTemTmp + "Cards/run_card_template.dat " + mgModelTemTmp + "Cards/run_card.dat")

	with open(track_script, "a") as f:
                f.write("Checking the run_card.dat default options are set.\n")

	# This is fine, though include for redundancy - need to check that run_card.dat is correct in my local MG
	# Check the default values are set correctly
	if not '1        = scalefact' in open(mgModelTemTmp + "Cards/run_card.dat").read():
		with open(track_script, "a") as f:
                        f.write("\nThe scale factor is not the default value - abort!")
		sys.exit('The scale factor is not the default value - abort!')
	
	if (not "'lhapdf'    = pdlabel" in open(mgModelTemTmp + "Cards/run_card.dat").read()) or (not '21000       = lhaid' in open(mgModelTemTmp + "Cards/run_card.dat").read()):
                with open(track_script, "a") as f:
                        f.write("\nThe PDF is not set to 21000 (MSTW2008lo68cl) - abort!")
                sys.exit('The PDF is not set to 21000 (MSTW2008lo68cl) - abort!')

	if (not 'XQCUT     = xqcut' in open(mgModelTemTmp + "Cards/run_card.dat").read()):
		with open(track_script, "a") as f:
                        f.write("\nrun_card.dat is not correct - abort!")
                sys.exit('run_card.dat is not correct - abort!')

	if channel == 'Z':
        	if (not '0        = ickkw' in open(mgModelTemTmp + "Cards/run_card.dat").read()):
        	       with open(track_script, "a") as f:
        	                f.write("\nickkw is turned on - abort!")
        	       sys.exit('ickkw is turned on - abort!')
	elif channel == 'jet':
		if (not '1        = ickkw' in open(mgModelTemTmp + "Cards/run_card.dat").read()):
			with open(track_script, "a") as f:
        	        	f.write("\nickkw is not on - abort!")
        		sys.exit('ickkw is not on - abort!')

	with open(track_script, "a") as f:
                f.write("Filling XQCUT values.\n")

	# Filling in XQCUT and adjusting for systematics if necessary
        if 'qcut' in outputName:
		qcut_up = qcut_num*2.
		qcut_down = qcut_num/2.
		if 'up' in outputName:
	        	os.system("sed -i 's/XQCUT/" + str(qcut_up) + "/g' " + mgModelTemTmp + "Cards/run_card.dat")
		elif 'down' in outputName:
			os.system("sed -i 's/XQCUT/" + str(qcut_down) + "/g' " + mgModelTemTmp + "Cards/run_card.dat")
		else:
                        print 'No "up" or "down" in outputName'
        else:
		if channel == 'Z':
			os.system("sed -i 's/XQCUT/0/g' " + mgModelTemTmp + "Cards/run_card.dat")                      
		elif channel == 'jet':
			#os.system("sed -i 's/XQCUT/" + str(qcut_num) + "/g' " + mgModelTemTmp + "Cards/run_card.dat")
			os.system("sed -i 's/XQCUT/80/g' " + mgModelTemTmp + "Cards/run_card.dat")
	
	if runSysts == 1: 
		with open(track_script, "a") as f:
                	f.write("Filling systematic variable in run_card.dat.\n")

	if 'scale' in outputName:
		# remove this as run_card is now a copy:os.system("cp " + mgModelTem + "/Cards/run_card.dat " + mgModelTem + "/Cards/run_card_orig.dat")
		if 'up' in outputName:
			os.system("sed -i 's/1        = scalefact/2        = scalefact/g' " + mgModelTemTmp + "Cards/run_card.dat")
		elif 'down' in outputName:
			os.system("sed -i 's/1        = scalefact/0.5      = scalefact/g' " + mgModelTemTmp + "Cards/run_card.dat")
		else:
			print 'No "up" or "down" in outputName'

	if 'PDF' in outputName:
		# remove like above: os.system("cp " + mgModelTem + "/Cards/run_card.dat " + mgModelTem + "/Cards/run_card_orig.dat")
                if 'up' in outputName:
			os.system("sed -i 's/lhapdf/nn23lo1/g' " + mgModelTemTmp + "Cards/run_card.dat")   # This is nn23lo1 (the default), removes link to LHAPDF
                elif 'down' in outputName:
                	os.system("sed -i 's/21000/10042/g' " + mgModelTemTmp + "Cards/run_card.dat")     # This is cteq6l1
		else:
                        print 'No "up" or "down" in outputName'
	
	# Run MG with an appropriate run name
	cmd = "cd " + mgModelTemTmp
	cmd += "; unset PBS_O_WORKDIR"
	cmd += "; localSetupROOT"
	cmd += "; export LHAPDF_DATA_PATH=" + tmpdir + "LHAPDF_all/share/LHAPDF/PDFsets"
	cmd += "; echo $LHAPDF_DATA_PATH"
	#cmd += "; export LHAPDF_DATA_PATH=" + localDir + "LHAPDF_all/share/LHAPDF/PDFsets"
	#cmd += "; ./bin/generate_events 2 6 " + outputName					# changed from 0 to '2 0' as 2 is multicore (with 0 = maximum cores), 0 is single_machine. See bin/generate_events (old input section).
	cmd += "; ./bin/generate_events 0 " + outputName
	cmd += "; wait"
	cmd += "; cd Events/" + outputName
	cmd += "; gunzip -f unweighted_events.lhe.gz"
	cmd += "; wait"

	with open(track_script, "a") as f:
                f.write("Running MadGraph... ")

	# Runs the command defined above, puts output straight into outfile
	with open(mgModelTemTmp + "mg5out_" + outputName + ".txt", "w") as outfile:
	        with open(mgModelTemTmp + "mg5out_" + outputName + "_err.txt", "w") as outfileerr:
	                subprocess.call(str(cmd), shell = True, stdout = outfile, stderr = outfileerr)

	with open(track_script, "a") as f:
                f.write("done.\n")
		f.write("Attempting to copy over results to local UI... ")

	# copy from the tmp folder the output into here 
	os.system("cp -r " + mgModelTemTmp + "Events/" + outputName + "/ " + mgModelTem + "Events/")
	os.system("cp " + mgModelTemTmp + "mg5out_" + outputName + "*.txt " + mgModelTem)

	if os.path.exists(mgModelTem + "Events/" + outputName + "/unweighted_events.lhe"):
		with open(track_script, "a") as f:
			f.write("done. The LHE file should now be accessible.\n Current time is" + str(datetime.datetime.now().strftime("%d%b%Y_%H.%M")) + "\n")
	else:
		with open(track_script, "a") as f:
                        f.write("There was a problem copying the results over!\n\n")

	with open(track_script, "a") as f:
		f.write("Removing " + tmpdir + "...")
	os.system("rm -r " + tmpdir)

	if not os.path.exists(tmpdir):
		with open(track_script, "a") as f:
			f.write("done. " + tmpdir + " should have been removed.\n\n")
	else:
		with open(track_script, "a") as f:
			f.write("There was a problem deleting " + tmpdir + "!\n\n")


###############################      Running Pythia      ################################

pythiaDir = localDir + "pythia8201/share/Pythia8/examples/"
mgDirGen = localDir + "MG5_aMC_v2_2_2/"
if channel == 'Z':
	mgModelTem = mgDirGen + "SiM_MODELTYPE_monoZ_8TeV/"		# For mono-Z processes
elif channel == 'jet':
	mgModelTem = mgDirGen + "SiM_MODELTYPE_monojet_8TeV/"           # For mono-jet processes
else:
	sys.exit('What channel are you studying?? - abort!')
mgPath = mgModelTem + "Events/" + outputName
main_name = "main_SiMs_" + outputName

mgPath_adapted = mgPath.replace("/", "\/")

if runPythia == 1:

	with open(track_script, "a") as f:
                f.write("Beginning Pythia...\n")
                f.write("Creating main_SiMs_XXX details, editing makefile... ")

	if not os.path.exists(mgPath + "/unweighted_events.lhe"):
		with open(track_script, "a") as f:
			f.write("\nMadGraph output does not exist, Pythia cannot execute.")
		sys.exit("MadGraph output does not exist, Pythia cannot execute.")

	# cp the main_SiMs_template.cc script
	os.system("cp " + pythiaDir + "main_SiMs_template.cc " + pythiaDir + "main_SiMs_" + outputName + ".cc")
	pythiaScript = pythiaDir + "main_SiMs_" + outputName + ".cc"
	os.system("sed -i 's/path/" + mgPath_adapted + "/g' " + pythiaScript)

	# Check the makefile, if not here, then add to list:
	main_name_space = main_name + ' '		# Needed to ensure it doesn't find the main_name embedded in a main_name_syst, as this won't run.
	if not main_name_space in open(pythiaDir + "Makefile").read():
	        os.system("sed -i 's/main_SiMs /main_SiMs " + main_name + " /g' " + pythiaDir + "Makefile")

	# Check the default values are set correctly

        if not 'LHAPDF6:MSTW2008lo68cl.LHgrid' in open(pythiaScript).read():
                with open(track_script, "a") as f:
                        f.write("\nMSTW2008LO is not the default PDF - abort!")
                sys.exit('MSTW2008LO is not the default PDF - abort!')

        if not 'Tune:ee = 3' in open(pythiaScript).read():
                with open(track_script, "a") as f:
                        f.write("\nTune:ee is not set to 3 - abort!")
                sys.exit('Tune:ee is not set to 3 - abort!')

	if not 'Tune:pp = 10' in open(pythiaScript).read():
                with open(track_script, "a") as f:
                        f.write("\nTune:pp is not set to 10 - abort!")
                sys.exit('Tune:pp is not set to 10 - abort!')

	# set matching according to if monoZ or monojet - default is on, as if events are removed in mono-Z this will show up immediately
	if channel == 'Z':	
		os.system("sed -i 's/JetMatching:merge = on/JetMatching:merge = off/g' " + pythiaScript)
		os.system("sed -i 's/pythia.setUserHooksPtr(matching)/\/\/pythia.setUserHooksPtr(matching)/g' " + pythiaScript)
		os.system("sed -i 's/delete matching/\/\/delete matching/g' " + pythiaScript)					# TODO should this also include setMad = on vs off??

        # Adjusting for systematics if necessary
        if 'PDF' in outputName:
                if 'up' in outputName:
                        os.system("sed -i 's/Tune:preferLHAPDF = 2/Tune:preferLHAPDF = 0/g' " + pythiaScript)			# Use internal Pythia PDF, don't access LHAPDF
			os.system("sed -i 's/PDF:pSet = LHAPDF6:MSTW2008lo68cl.LHgrid/PDF:pSet = 13/g' " + pythiaScript)	# This is NNPDF2.3, use default Pythia option
                elif 'down' in outputName:
                        os.system("sed -i 's/PDF:pSet = LHAPDF6:MSTW2008lo68cl.LHgrid/PDF:pSet = LHAPDF6:cteq6l1.LHgrid/g' " + pythiaScript)
                else:
                        print 'No "up" or "down" in outputName'

	if 'tune' in outputName:
                if 'up' in outputName:
                        os.system("sed -i 's/Tune:preferLHAPDF = 2/Tune:preferLHAPDF = 0/g' " + pythiaScript)                   # Use internal Pythia PDF, don't access LHAPDF
                        os.system("sed -i 's/Tune:ee = 3/Tune:ee = 7/g' " + pythiaScript)        				# Alternative ee tune, needed for Monash tune
			os.system("sed -i 's/Tune:pp = 10/Tune:pp = 14/g' " + pythiaScript)                                     # Monash tune
                elif 'down' in outputName:
                        os.system("sed -i 's/Tune:pp = 10/Tune:pp = 9/g' " + pythiaScript)					# ATLAS UE Tune AU2-CTEQ6L1
                else:
                        print 'No "up" or "down" in outputName'

	with open(track_script, "a") as f:
                f.write("done.\n")
		f.write("Running Pythia... ")

	cmd = "cd " + pythiaDir
	cmd += "; export LHAPDF_DATA_PATH=" + localDir + "LHAPDF_all/share/LHAPDF/PDFsets"
	cmd += "; unset PBS_O_WORKDIR"
	cmd += "; make " + main_name
	cmd += "; wait"
	cmd += "; ./" + main_name + " HepMC_out/" + outputName + ".dat > pythia_running/PYTHIA_" + outputName + ".txt"
	cmd += "; wait"
	cmd += "; mv " + main_name + "* ccs_and_exes/"

	print cmd

	with open(pythiaDir + "pythiaout.txt", "w") as outfile:
	        with open(pythiaDir + "pythiaout_err.txt", "w") as outfileerr:
	                subprocess.call(str(cmd), shell = True, stdout = outfile, stderr = outfileerr)

	with open(track_script, "a") as f:
                f.write("done.\n")
		f.write("HepMC output should now exist in HepMC_out/ folder.\n")
		f.write("Pythia step is complete.\n\n")

###############################      Running HepMC to ROOT conversion      ################################

convDir = localDir + "ConvertHepMC2root/"
batchDir = convDir + "cxx_and_sh"	# location of automatically-created scripts after running
batchDir2 = convDir + "output_exes"

if runCon == 1:

	with open(track_script, "a") as f:
                f.write("Beginning HepMC2root...\n")

	if not os.path.exists(pythiaDir + "HepMC_out/BASENAME.dat"):
		with open(track_script, "a") as f:
                        f.write("Pythia output does not exist, HepMC2root cannot execute.\n")
                sys.exit("Pythia output does not exist, HepMC2root cannot execute.")

	with open(track_script, "a") as f:
                f.write("Creating .cxx and compile scripts... ")

	# cp the HepMC2root_MDF_template.cxx script
	os.system("cp " + convDir + "HepMC2root_MDF_template.cxx " + convDir + "HepMC2root_MDF_" + outputName + ".cxx")
	convScript = convDir + "HepMC2root_MDF_" + outputName + ".cxx"
	os.system("sed -i 's/INPUT_NAME/" + outputName + "/g' " + convScript)

	os.system("cp " + convDir + "compile_MDF_template.sh " + convDir + "compile_MDF_" + outputName + ".sh")
	compScript = convDir + "compile_MDF_" + outputName + ".sh"
	os.system("sed -i 's/INPUT_NAME/" + outputName + "/g' " + compScript)

	with open(track_script, "a") as f:
                f.write("done.\n")
		f.write("Compiling and running... ")

	cmd = "cd " + convDir
	#cmd += "; export LHAPDF_DATA_PATH=" + localDir + "LHAPDF_all/share/LHAPDF/PDFsets"
	cmd += "; unset PBS_O_WORKDIR"
	cmd += "; sh " + compScript
	cmd += "; wait"
	cmd += "; ./output_MDF_" + outputName
	cmd += "; wait"
	cmd += "; mv " + convScript + " " + batchDir
	cmd += "; mv " + compScript + " " + batchDir
	cmd += "; mv output_MDF_" + outputName + " " + batchDir2

	print cmd

	with open(convDir + "HepMCout.txt", "w") as outfile:
	        with open(convDir + "HepMCout_err.txt", "w") as outfileerr:
	                subprocess.call(str(cmd), shell = True, stdout = outfile, stderr = outfileerr)

	with open(track_script, "a") as f:
                f.write("done.\n")
                f.write("The relevant output_XXX folder should now be in ConvertHepMC2root/ folder.\n")
		f.write("HepMC2oot step is complete.\n\n")

	if os.path.exists(convDir + "rootFiles/OUTPUT_" + outputName + ".root"):
		os.system("rm " + pythiaDir + "HepMC_out/BASENAME.dat")
	else:
		f.write("Problem with this step! HepMC file has not been deleted.\n\n")

###############################      Running cutflow script      ################################

cutflowDir = localDir + "CutFlow/"
batchDir = cutflowDir + "batch_scripts"       # location of automatically-created scripts after running
outputStore = cutflowDir + "txt_outputs"	

if runCF == 1:

        with open(track_script, "a") as f:
                f.write("Beginning cutflow...\n")

        if not os.path.exists(convDir + "rootFiles/OUTPUT_BASENAME.root"):
                with open(track_script, "a") as f:
                        f.write("HepMC2root output does not exist, cutflow cannot execute.\n")
                sys.exit("HepMC2root output does not exist, cutflow cannot execute.")

        with open(track_script, "a") as f:
                f.write("Copying template cutflow script... ")

	outputNameadap = outputName.replace("+", "")			# NEW

        # cp the monoZ_cutflow_template.C script
        os.system("cp " + cutflowDir + "monoZ_cutflow_template.C " + cutflowDir + "monoZ_cutflow_" + outputNameadap + ".C")
        cutflowScript = cutflowDir + "monoZ_cutflow_" + outputNameadap + ".C"
	os.system("sed -i 's/INPUT_ADAP_NAME/" + outputNameadap + "/g' " + cutflowScript)		# NEW - need to do INPUT_NAME -> INPUT_ADAP_NAME in the void bit of the template cutflow
        os.system("sed -i 's/INPUT_NAME/" + outputName + "/g' " + cutflowScript)

        with open(track_script, "a") as f:
                f.write("done.\n")
                f.write("Running... \n")

	cmd = "cd " + cutflowDir
        cmd += "; root -l " + cutflowScript + " &> cutflow_output_" + outputName + ".txt"		
        cmd += "; wait"
        cmd += "; mv " + cutflowScript + " " + batchDir
	cmd += "; mv cutflow_output_" + outputName + ".txt " + outputStore				

        print cmd

        with open(track_script, "a") as outfile:
                with open(convDir + "cutflow_out_err.txt", "w") as outfileerr:
                        subprocess.call(str(cmd), shell = True, stdout = outfile, stderr = outfileerr)

        with open(track_script, "a") as f:
                f.write("\n... done.\n")
                f.write("The relevant output rootfile should be in the CutFlow/rootFiles/ folder.\n")
                f.write("Cutflow step is complete.")

os.system("mv " + track_script + " " + trackStore)
