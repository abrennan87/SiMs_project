MadGraph = 1
Pythia = 1
HepMC2root = 1
Cutflow = 1

monoX = 'Z'		# Z for mono-Z, jet for mono-jet

model = ['SVD']#, 'SSD', 'TSD']#, 'SVD', 'TSD']


Mdm = ['10', '200', '400', '1000']#, '350']		
Mmed = ['1000', '1200']#, '5000']#, '20', '100', '200', '1000', '2000', '20000']

widths = ['1']
#widths = ["1", "M8pi", "M3"]  # M3 = M/3, M8pi = M/8pi, 1=1.
#widths = ["1"]
#widths = ["M8pi"]
#widths = ["min"]

couplings = [1]

systematics = 1 

# For Z process, don't need qcut systematic
syst_list = ['PDF+tune', 'scale', 'qcut'] #qcut not needed for monoZ

