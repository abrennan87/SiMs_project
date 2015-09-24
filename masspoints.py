MadGraph = 1
Pythia = 1
HepMC2root = 1
Cutflow = 0

monoX = 'jet'		# Z for mono-Z, jet for mono-jet

model = ['SVD']

#TSD masses
#Mdm = ['1']
#Mmed = ['10', '20', '100', '200', '1000', '2000', '20000']
#coupling_ratio = [1]

#Mdm = ['500']
#Mmed = ['550']

#Mdm = ['10']
#Mmed = ['11', '20', '100', '200', '1000', '2000', '20000']

#Mdm = ['100']
#Mmed = ['110', '200', '1000', '2000', '20000']

#Mdm = ['1000']
#Mmed = ['1100', '2000', '20000']

#Mdm = ['100']
#Mmed = ['500']

#couplings = [1]         # value of g_q
widths = ['min']

#SAD/SVD masses, if width > 80% of mass, not produced (see missing rat=5) (Widths are not identical, but similar enough that the same points hold)
#Mdm = ['1']
#Mmed = ['1', '2']
#coupling_ratio = [0.2, 0.5, 1, 2, 5]
#coupling_ratio = [5]

#Mdm = ['1']
#Mmed = ['10', '20', '100', '200', '1000', '2000', '20000']
#coupling_ratio = [0.2, 0.5, 1, 2]

#Mdm = ['10']
#Mmed = ['1', '2', '10', '20']
#Mmed = ['20000']
#coupling_ratio = [0.2, 0.5, 1, 2, 5]
#coupling_ratio = [2]

#Mdm = ['10']
#Mmed = ['100', '200', '1000', '2000', '20000']
#coupling_ratio = [0.2, 0.5, 1, 2]

#Mdm = ['100']
#Mmed = ['1', '2', '10', '20', '100', '200']
#coupling_ratio = [0.2, 0.5, 1, 2, 5]
#coupling_ratio = [5]

#Mdm = ['100']
#Mmed = ['1000', '2000', '20000']
#coupling_ratio = [0.2, 0.5, 1, 2]

#Mdm = ['1000']
#Mmed = ['1', '2', '10', '20', '100', '200', '1000', '2000']
#coupling_ratio = [0.2, 0.5, 1, 2, 5]
#coupling_ratio = [5]

#Mdm = ['1000']
#Mmed = ['20000']
#coupling_ratio = [0.2, 0.5, 1, 2]

# study of width dependence of MET
# SVD
#Mdm = ['1', '1000']
Mdm = ['1000']
Mmed = ['500']
coupling_ratio = [1]
couplings = [0.1]
#TSD
#Mdm = ['1', '400']
#Mdm = ['1', '1000']
#Mdm = ['1']
#Mdm = ['400']
#Mmed = ['500']
#coupling_ratio = [1]
#couplings = [0.1]

# testing speeds
#Mdm = ['100']
#Mmed = ['500']
#couplings = [1]

#coupling_ratio = [0.2, 0.5, 1, 2, 5]	# g_chi / g_q: 0.2, 0.5, 1, 2, 5     # REMEMBER	ratios other than 1 are meaningless for TSD!
coupling_ratio = [1]

systematics = 0

# For Z process, don't need qcut systematic
syst_list = ['PDF+tune', 'scale']
#syst_list = ['scale']

# failed jobs

'''
Mdm = ['1']
Mmed = ['1']
coupling_ratio = [0.5]
systematics = 0

Mdm = ['1']
Mmed = ['1']
coupling_ratio = [5]
systematics = 1
syst_list = ['scale']

Mdm = ['1']
Mmed = ['100']
coupling_ratio = [2]
systematics = 1
syst_list = ['PDF+tune']

Mdm = ['1']
Mmed = ['200']
coupling_ratio = [1]
systematics = 1
syst_list = ['scale']

Mdm = ['1']
Mmed = ['200']
coupling_ratio = [2]
systematics = 1
syst_list = ['PDF+tune']

Mdm = ['1']
Mmed = ['200']
coupling_ratio = [0.5]
systematics = 1
syst_list = ['scale']

Mdm = ['1']
Mmed = ['2000']
coupling_ratio = [1]
systematics = 1
syst_list = ['PDF+tune']

Mdm = ['1']
Mmed = ['2000']
coupling_ratio = [2]
systematics = 0

Mdm = ['1']
Mmed = ['20000']
coupling_ratio = [1]
systematics = 1
syst_list = ['PDF+tune']

Mdm = ['10']
Mmed = ['10']
coupling_ratio = [2]
systematics = 1
syst_list = ['PDF+tune']

Mdm = ['10']
Mmed = ['20']
coupling_ratio = [1]
systematics = 1
syst_list = ['scale']

Mdm = ['10']
Mmed = ['2000']
coupling_ratio = [1]
systematics = 1
syst_list = ['PDF+tune']

Mdm = ['100']
Mmed = ['100']
coupling_ratio = [2]
systematics = 1
syst_list = ['scale']

Mdm = ['100']
Mmed = ['200']
coupling_ratio = [0.2]
systematics = 1
syst_list = ['scale']

Mdm = ['100']
Mmed = ['1000']
coupling_ratio = [1]
systematics = 1
syst_list = ['scale']

Mdm = ['100']
Mmed = ['20000']
coupling_ratio = [0.5]
systematics = 1
syst_list = ['PDF+tune']
'''
