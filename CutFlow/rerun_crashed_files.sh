#!/bin/bash

hDir="/home/ameliajb/workarea/SiMs_AtlasExternal_v2/CutFlow";

# from PDFtune for name

for name in "TSD_3_2000_min_rat1_1_PDFtune_down"; do

# define newname for the output txt file name
if [[ ${name} == *"PDFtune"* ]]; then
	newname=$(echo $name | sed 's/PDFtune/PDF+tune/g')
else
	newname=${name};
fi

echo ${newname}

cp ${hDir}/batch_scripts/monoZ_cutflow_${name}.C ./;

root -l -q monoZ_cutflow_${name}.C &> txt_outputs/cutflow_output_${newname}.txt;

#rm monoZ_cutflow_${name}.C

#Generate_trf.py --omitvalidation=testEventMinMax ecmEnergy=13000 runNumber=158969 firstEvent=1 maxEvents=10000 randomSeed=1002 jobConfig=${hDir}MC12.000001.test.py inputGeneratorFile=${hDir}/inFiles/madgraph.${name}._0001.tar.gz outputEVNTFile=${name}.EVNT.root;

#mv ${name}.EVNT.root ${hDir}/rootFiles;

done
