#! /bin/bash

g++ HepMC2root_MDF_INPUT_NAME.cxx -o "output_MDF_INPUT_NAME" `root-config --cflags --glibs` `/home/ameliajb/workarea/SiMs_AtlasExternal_v2/FastJet/fastjet-3.1.0/bin/fastjet-config --cxxflags --libs --plugins`
