MadGraph = 0
Pythia = 1
HepMC2root = 1
Cutflow = 0

monoX = 'WZ'		# Z for mono-Z, jet for mono-jet, WZ for mono-WZ

model = ['SAD']

couplings = [1]         # value of g_q		  # g_chi / g_q: 0.2, 0.5, 1, 2, 5     # REMEMBER ratios other than 1 are meaningless for TSD!
widths = ['min']

#Mdm = ['1', '3', '10', '30', '100', '300', '1000']
#Mmed = ['1', '2', '10', '20', '100', '200', '1000', '2000']
#coupling_ratio = [0.2, 0.5, 1, 2, 5]

###################   SVD/SAD masses   ###################
#If width > 50% of mass, not produced 
#SVD and SAD widths are not identical, but similar enough that the same points hold. UPDATE: actually not quite true, SAD has some additional masses. See below for SAD 3/30/300.

#Mdm = ['1']
#Mmed = ['1', '2']
#coupling_ratio = [1]
#coupling_ratio = [0.2, 0.5, 1, 2, 5]

Mdm = ['1']
#Mmed = ['10', '20']
Mmed = ['10']	# for systematics study
coupling_ratio = [1]
#coupling_ratio = [0.2, 0.5, 1, 2]

#Mdm = ['1']
#Mmed = ['100', '200', '1000']
#Mmed = ['1000']
#coupling_ratio = [1]
#coupling_ratio = [0.2, 0.5, 1]

#Mdm = ['1']
#Mmed = ['2000']
#coupling_ratio = [0.5]
#coupling_ratio = [0.2, 0.5]

#Mdm = ['3']
#Mmed = ['1', '2']
#coupling_ratio = [0.2, 0.5, 1, 2, 5] # 1
#coupling_ratio = [1]

#Mdm = ['3']
#Mmed = ['10']
#coupling_ratio = [0.2, 0.5, 1, 2] # 1

#Mdm = ['3']
#Mmed = ['20', '100', '200']
#coupling_ratio = [0.2, 0.5, 1]

#Mdm = ['3']
#Mmed = ['1000', '2000']
#coupling_ratio = [0.2, 0.5] 

#Mdm = ['10']
#Mmed = ['1', '2', '10', '20']
#coupling_ratio = [1]
#coupling_ratio = [0.2, 0.5, 1, 2, 5]

#Mdm = ['10']
#Mmed = ['100']
#coupling_ratio = [1]
#coupling_ratio = [0.2, 0.5, 1, 2]

#Mdm = ['10']
#Mmed = ['200', '1000']
#coupling_ratio = [0.5]
#coupling_ratio = [0.2, 0.5, 1]

#Mdm = ['10']
#Mmed = ['2000']
#coupling_ratio = [0.5]
#coupling_ratio = [0.2, 0.5]

#Mdm = ['30']
#Mmed = ['1', '2', '10', '20']
#coupling_ratio = [0.2, 0.5, 1, 2, 5] # 1

#Mdm = ['30']
#Mmed = ['100']
#coupling_ratio = [0.2, 0.5, 1, 2] # 1

#Mdm = ['30']
#Mmed = ['200']
#coupling_ratio = [0.2, 0.5, 1] # 1

#Mdm = ['30']
#Mmed = ['1000', '2000']
#coupling_ratio = [0.2, 0.5]

#Mdm = ['100']
#Mmed = ['1', '2', '10', '20', '100', '200']
#Mmed = ['10']  # for systematics study
#coupling_ratio = [1]
#coupling_ratio = [0.2, 0.5, 1, 2, 5]

#Mdm = ['100']
#Mmed = ['1000', '2000']
#coupling_ratio = [0.5]
#coupling_ratio = [0.2, 0.5, 1]

#Mdm = ['100']
#Mmed = ['20000']
#coupling_ratio = [0.5]
#coupling_ratio = [0.2, 0.5]

#Mdm = ['300']
#Mmed = ['1', '2', '10', '20', '100', '200']
#coupling_ratio = [0.2, 0.5, 1, 2, 5] # 1
#coupling_ratio = [1]

#Mdm = ['300']
#Mmed = ['1000', '2000']
#coupling_ratio = [0.2, 0.5]

#Mdm = ['300']
#Mmed = ['200']
#coupling_ratio = [0.5]

#Mdm = ['1000']
#Mmed = ['1', '2', '10', '20', '100', '200', '1000', '2000']
#Mmed = ['2000']
#coupling_ratio = [1]
#coupling_ratio = [0.2, 0.5, 1, 2, 5]

#Mdm = ['1000']
#Mmed = ['20000'] # for normal AND systematics study
#coupling_ratio = [0.5]
#coupling_ratio = [0.2]

###################   SAD masses (3/30/300)  ###################

#Mdm = ['3']
#Mmed = ['1', '2']
#coupling_ratio = [0.2, 0.5, 1, 2, 5]

#Mdm = ['3']
#Mmed = ['10', '20']
#coupling_ratio = [0.2, 0.5, 1, 2] 

#Mdm = ['3']
#Mmed = ['100', '200', '1000']
#coupling_ratio = [0.2, 0.5, 1]

#Mdm = ['3']
#Mmed = ['2000']
#coupling_ratio = [0.2, 0.5]

#Mdm = ['30']
#Mmed = ['1', '2', '10', '20']
#coupling_ratio = [0.2, 0.5, 1, 2, 5]

#Mdm = ['30']
#Mmed = ['100', '200']
#coupling_ratio = [0.2, 0.5, 1, 2]

#Mdm = ['30']
#Mmed = ['1000']
#coupling_ratio = [0.2, 0.5, 1]

#Mdm = ['30']
#Mmed = ['2000']
#coupling_ratio = [0.2, 0.5]

#Mdm = ['300']
#Mmed = ['1', '2', '10', '20', '100', '200']
#coupling_ratio = [0.2, 0.5, 1, 2, 5]

#Mdm = ['300']
#Mmed = ['1000', '2000']
#coupling_ratio = [0.2, 0.5, 1]

###################   TSD masses   ###################

#Mdm = ['1']
#Mmed = ['10', '20', '100', '200', '1000', '2000']
#coupling_ratio = [1]

#Mdm = ['3']
#Mmed = ['10', '20', '100', '200', '1000', '2000']
#coupling_ratio = [1]

#Mdm = ['10']
#Mmed = ['11', '20', '100', '200', '1000', '2000']
#coupling_ratio = [1]

#Mdm = ['30']
#Mmed = ['33', '100', '200', '1000', '2000']
#coupling_ratio = [1]

#Mdm = ['100']
#Mmed = ['110', '200', '1000', '2000']
#coupling_ratio = [1]

#Mdm = ['300']
#Mmed = ['330', '1000']
#coupling_ratio = [1]

#Mdm = ['1000']
#Mmed = ['1100', '2000']
#coupling_ratio = [1]

################ Resubmissions ###############
#Mdm = ['300']
#Mmed = ['200']
#coupling_ratio = [5]
#systematics = 1
#syst_list = ['scale'] # only want up

#Mdm = ['30']
#Mmed = ['2']
#coupling_ratio = [5]
#systematics = 1
#syst_list = ['PDF+tune'] # only want up

#Mdm = ['3']
#Mmed = ['1000']
#coupling_ratio = [1]
#systematics = 1
#syst_list = ['scale'] # only want up

#systematics = 0
systematics = 1

# For Z process, don't need qcut systematic
#syst_list = ['PDF+tune', 'scale', 'qcut']
syst_list = ['PDF+tune', 'scale']
