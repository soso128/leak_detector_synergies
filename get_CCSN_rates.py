#!/usr/bin/env python

import sys
import os
current_dir = os.getcwd()
sys.path=[f"{current_dir}/snewpy/python/"]+sys.path
from snewpy import snowglobes
import astropy.units as u

SNOwGLoBES_path = f"{current_dir}/snowglobes/"  # where the detector and cross-section files are located

# arguments for generate_time_series
model_dir = f"{current_dir}/SNEWPY_models/Bollig_2016/"
model_prefix = "s11.2c"
model_file = f"{model_dir}/{model_prefix}"
modeltype = 'Bollig_2016'
transformation = 'AdiabaticMSW_NMO'
d = 10  # Supernova distance in kpc
deltat = 0.1 * u.s
output_folder = "."
detector="wc100kt15prct"

# Running the modules
outfile = snowglobes.generate_time_series(model_file, modeltype, transformation, d, deltat = deltat)
snowglobes.simulate(SNOwGLoBES_path, outfile, detector_input=detector, detector_effects=False)
snowglobes.collate(SNOwGLoBES_path, outfile, detector_input=detector, smearing=False, skip_plots=True)

# Save to ROOT histograms
infile=outfile.replace('.tar.bz2', '_SNOprocessed.tar.gz')
os.system(f"{current_dir}/snewpy/python/snewpy/scripts/Convert_to_ROOT.py '{infile}'")

# Copy in safe place and cleanup
os.system(f"mv {model_dir}/*_unsmeared_weighted.root {output_folder}")
os.system(f"mv {model_dir}/*.tar.bz2 {output_folder}")
os.system(f"rm {model_dir}/*.root")
os.system(f"rm {model_dir}/*.tar*")
os.system(f"rm {model_dir}/*.npy")
