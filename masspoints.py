MadGraph = 0 
Pythia = 0
HepMC2root = 0
Cutflow = 0

monoX = 'Z'		# Z for mono-Z, jet for mono-jet

model = ['SVD']#, 'TSD']#, 'SSD', 'TSD']#, 'SVD', 'TSD']


#Mdm = ['200']#, '200', '400', '1000']#, '350']		
#Mmed = ['1000', '1200']#, '5000']#, '20', '100', '200', '1000', '2000', '20000']

#Mdm = ['10']
#Mmed = ['10', '200', '500', '700', '1000', '1200']
#Mmed = ['700', '1000', '1200']

#Mdm = ['400']
#Mmed = ['1994']

#Mdm = ['200']
#Mmed = ['10', '200']
#Mmed = ['220', '500', '700', '1000', '1200']

#Mdm = ['400']
#Mmed = ['10', '200', '400']
#Mmed = ['420', '500', '700', '1000', '1200']

#Mdm = ['1000']
#Mmed = ['400', '500', '700', '1000']
#Mmed = ['500']
#Mmed = ['1100', '1200']

#Mdm = ['400']
#Mmed = ['700']

#SVD masses
#Mdm = ['1', '10', '100', '1000']
#Mmed = ['1', '2', '10', '20', '100', '200', '1000', '2000', '20000']

#TSD masses
Mdm = ['1']
#Mmed = ['1.1', '2', '10', '20', '100', '200', '1000', '2000', '20000']
Mmed = ['10', '20', '100', '200', '1000', '2000', '20000']

#Mdm = ['10']
#Mmed = ['11', '20', '100', '200', '1000', '2000', '20000']
#Mmed = ['100']

#Mdm = ['100']
#Mmed = ['110', '200', '1000', '2000', '20000']

#Mdm = ['1000']
#Mmed = ['1100', '2000', '20000']

#Mdm = ['1']
#Mmed = ['2']

#widths = ['1']
#widths = ["1", "M8pi", "M3"]  # M3 = M/3, M8pi = M/8pi, 1=1.
#widths = ["1"]
#widths = ["M8pi"]
widths = ['min']


#Mdm = ['1']
#Mmed = ['1000']
#couplings = [1]
#coupling_ratio = [1]

couplings = [1]		# value of g_q
#coupling_ratio = [0.2, 0.5, 1, 2]#, 5]	# g_chi / g_q: 0.2, 0.5, 1, 2, 5     # REMEMBER	ratios other than 1 are meaningless for TSD!
#coupling_ratio = [0.2, 0.5, 2]#, 5]
coupling_ratio = [2, 5]
#coupling_ratio = [1]

systematics = 0

# For Z process, don't need qcut systematic
syst_list = ['PDF+tune', 'scale']#, 'qcut'] #qcut not needed for monoZ
#syst_list = ['scale']
