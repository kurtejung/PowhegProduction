#!/bin/bash 

export LHAPDFSYS=/afs/cern.ch/sw/lcg/external/MCGenerators/lhapdf/5.8.9/x86_64-slc6-gcc46-opt
export PATH=${PATH}:${LHAPDFSYS}/bin
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${LHAPDFSYS}/lib
export LHAPATH=/afs/cern.ch/sw/lcg/external/MCGenerators/lhapdf/5.8.9/share/PDFsets 
#export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/afs/cern.ch/sw/lcg/external/fastjet/2.4.2p1/slc4_amd64_gcc34/lib:/afs/cern.ch/sw/lcg/external/MCGenerators/lhapdf/5.8.4/slc4_amd64_gcc34/lib
#export FASTJET_CONFIG=/cvmfs/cms.cern.ch/slc6_amd64_gcc472/external/fastjet/3.0.1-cms2/bin/fastjet-config
