import os  
for fn in os.listdir('.'):
	if os.path.isfile(fn) and "TSD_3" in fn:
		found_out = "no"
        	with open(os.path.join("/home/ameliajb/workarea/SiMs_AtlasExternal_v2/CutFlow/txt_outputs", fn), 'r') as f:
			for line in f:
				if "MET stat" in line:
					found_out = "yes"
					break
		if found_out == "no": 
			print fn + " crashed"
					
