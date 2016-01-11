#!/bin/bash

hDir="/home/ameliajb/workarea/SiMs_AtlasExternal_v2/CutFlow";

# remove + from PDF+tune for name

#for name in "SVD_300_1_min_rat1_1" "SVD_300_1_min_rat1_1_PDFtune_up" "SVD_300_1_min_rat1_1_PDFtune_down" "SVD_300_1_min_rat1_1_scale_up" "SVD_300_1_min_rat1_1_scale_down" "SVD_300_2_min_rat1_1" "SVD_300_2_min_rat1_1_PDFtune_up" "SVD_300_2_min_rat1_1_PDFtune_down" "SVD_300_2_min_rat1_1_scale_up" "SVD_300_2_min_rat1_1_scale_down" "SVD_300_10_min_rat1_1" "SVD_300_10_min_rat1_1_PDFtune_up" "SVD_300_10_min_rat1_1_PDFtune_down" "SVD_300_10_min_rat1_1_scale_up" "SVD_300_10_min_rat1_1_scale_down" "SVD_300_20_min_rat1_1" "SVD_300_20_min_rat1_1_PDFtune_up" "SVD_300_20_min_rat1_1_PDFtune_down" "SVD_300_20_min_rat1_1_scale_up" "SVD_300_20_min_rat1_1_scale_down" "SVD_300_100_min_rat1_1" "SVD_300_100_min_rat1_1_PDFtune_up" "SVD_300_100_min_rat1_1_PDFtune_down" "SVD_300_100_min_rat1_1_scale_up" "SVD_300_100_min_rat1_1_scale_down" "SVD_300_200_min_rat1_1" "SVD_300_200_min_rat1_1_PDFtune_up" "SVD_300_200_min_rat1_1_PDFtune_down" "SVD_300_200_min_rat1_1_scale_up" "SVD_300_200_min_rat1_1_scale_down"; do

#for name in "SVD_300_1000_min_rat1_1" "SVD_300_1000_min_rat1_1_PDFtune_up" "SVD_300_1000_min_rat1_1_PDFtune_down" "SVD_300_1000_min_rat1_1_scale_up" "SVD_300_1000_min_rat1_1_scale_down" "SVD_300_2000_min_rat1_1" "SVD_300_2000_min_rat1_1_PDFtune_up" "SVD_300_2000_min_rat1_1_PDFtune_down" "SVD_300_2000_min_rat1_1_scale_up" "SVD_300_2000_min_rat1_1_scale_down"; do

for name in "SVD_1_100_min_rat1_1" "SVD_1000_100_min_rat1_1"; do
#for name in ""; do
#for name in ""; do
#for name in ""; do
#for name in ""; do
#for name in ""; do
#for name in ""; do

echo $name

# define newname for the output txt file name
if [[ ${name} == *"PDFtune"* ]]; 
then
	newname=$(echo $name | sed 's/PDFtune/PDF+tune/g')
else
	newname=${name};
fi

cfb="${hDir}/batch_scripts/monoZ_cutflow_${name}.C";
cf="${hDir}/monoZ_cutflow_${name}.C";

if [ -f ${cfb} ]; 
then
	cp ${cfb} ${cf};
	echo "File exists";
else
	echo "Creating file";
	cp ${hDir}/monoZ_cutflow_template.C ${cf};
	sed -i "s/INPUT_ADAP_NAME/${name}/g" ${cf};
	sed -i "s/INPUT_NAME/${newname}/g" ${cf};
fi

root -l -q monoZ_cutflow_${name}.C &> txt_outputs/cutflow_output_${newname}.txt;

mv ${cf} ${cfb};

done
