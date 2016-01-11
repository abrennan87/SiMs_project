import sys

import os
import subprocess
#import masspoints_2
import time
import math

# list below should be completed
#modelType = 'SVD'
modelType = 'TSD'
#points = ['SVD_10_10_min_rat', 'SVD_10_200_min_rat', 'SVD_10_500_min_rat', 'SVD_10_700_min_rat', 'SVD_10_1000_min_rat', 'SVD_10_1200_min_rat', 'SVD_200_10_min_rat', 'SVD_200_200_min_rat', 'SVD_200_220_min_rat', 'SVD_200_500_min_rat', 'SVD_200_700_min_rat', 'SVD_200_1000_min_rat', 'SVD_200_1200_min_rat', 'SVD_400_10_min_rat', 'SVD_400_200_min_rat', 'SVD_400_400_min_rat', 'SVD_400_420_min_rat', 'SVD_400_500_min_rat', 'SVD_400_700_min_rat', 'SVD_400_1000_min_rat', 'SVD_400_1200_min_rat', 'SVD_1000_10_min_rat', 'SVD_1000_200_min_rat', 'SVD_1000_400_min_rat', 'SVD_1000_500_min_rat', 'SVD_1000_700_min_rat', 'SVD_1000_1000_min_rat', 'SVD_1000_1100_min_rat', 'SVD_1000_1200_min_rat']
#points = ['SVD_1_1_min_rat', 'SVD_1_2_min_rat', 'SVD_1_10_min_rat', 'SVD_1_20_min_rat', 'SVD_1_100_min_rat', 'SVD_1_200_min_rat', 'SVD_1_1000_min_rat', 'SVD_1_2000_min_rat', 'SVD_1_20000_min_rat', 'SVD_10_1_min_rat', 'SVD_10_2_min_rat', 'SVD_10_10_min_rat', 'SVD_10_20_min_rat', 'SVD_10_100_min_rat', 'SVD_10_200_min_rat', 'SVD_10_1000_min_rat', 'SVD_10_2000_min_rat', 'SVD_10_20000_min_rat', 'SVD_100_1_min_rat', 'SVD_100_2_min_rat', 'SVD_100_10_min_rat', 'SVD_100_20_min_rat', 'SVD_100_100_min_rat', 'SVD_100_200_min_rat', 'SVD_100_1000_min_rat', 'SVD_100_2000_min_rat', 'SVD_100_20000_min_rat', 'SVD_1000_1_min_rat', 'SVD_1000_2_min_rat', 'SVD_1000_10_min_rat', 'SVD_1000_20_min_rat', 'SVD_1000_100_min_rat', 'SVD_1000_200_min_rat', 'SVD_1000_1000_min_rat', 'SVD_1000_2000_min_rat', 'SVD_1000_20000_min_rat']
points = ['TSD_1_1.1_min_rat', 'TSD_1_2_min_rat', 'TSD_1_10_min_rat', 'TSD_1_20_min_rat', 'TSD_1_100_min_rat', 'TSD_1_200_min_rat', 'TSD_1_1000_min_rat', 'TSD_1_2000_min_rat', 'TSD_1_20000_min_rat', 'TSD_10_11_min_rat', 'TSD_10_20_min_rat', 'TSD_10_100_min_rat', 'TSD_10_200_min_rat', 'TSD_10_1000_min_rat', 'TSD_10_2000_min_rat', 'TSD_10_20000_min_rat', 'TSD_100_110_min_rat', 'TSD_100_200_min_rat', 'TSD_100_1000_min_rat', 'TSD_100_2000_min_rat', 'TSD_100_20000_min_rat', 'TSD_1000_1100_min_rat', 'TSD_1000_2000_min_rat', 'TSD_1000_20000_min_rat']
ratio = [0.2, 0.5, 1, 2, 5]
#ratio = [1]
#systs = []
systs = ['PDF+tune', 'scale']
gq_nom = 1

localDir = "/home/ameliajb/workarea/SiMs_AtlasExternal_v2/"
MGdir = localDir + "MG5_aMC_v2_2_2/"
cutflowDir = localDir + "CutFlow/txt_outputs/"

# create the limits file
#limits = localDir + "limits_store_SVD_Wmin.txt"

lumi = 20.3
eff = 1.0               # real efficiency already taken into account in acceptance
#N_exp = {'150': 22.3, '250': 8.6, '350':4.5, '450': 3.4} - taken from the note, not useable
#N_obs = {'150': 20.9, '250': 6.6, '350': 3.0, '450': 3.0} 
N_exp = {'150': 34.7, '250': 6.8} # calculated with HistFitter and info from the published paper
N_obs = {'150': 32.2, '250': 5.9}

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
