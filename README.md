# Synergy studies for neutrinos from Core-Collapse Supernovae (CCSNe)

This is an analysis framework to obtain neutrino light curves for various CCSN models using the [SNEWPY](https://github.com/SNEWS2/snewpy) software.
Here, we use a simple rate calculation which assumes a perfect detector so the codes in this folder can be used out of the box and installing SNoWGLoBES and GLoBES is not necessary. The `snowglobes` folder contains only the detector, channel and cross-section information needed to compute the rates.

The codes require at least Python 3.7 to run. To compute the neutrino interaction rates associated with a given CCSN model in all the SNEWPY-available media (notably water and liquid argon), just run

        python get_CCSN_rates.py
        
The CCSN model folder, the model file prefix, the supernova distance, the flavor transformation type, and the detector type can be set by editing the file. In this simple example we use all available SNEWPY detectors, the "Bollig 2016" model (based on Garching CCSN simulations), with a 11 solar mass progenitor, and adiabatic MSW flavor transformation assuming normal mass ordering.

To add a new model file, just put it in the `SNEWPY_models` folder (I have not committed all the available SNEWPY models since we will probably need only a few of them), and change the paths accordingly in `get_CCSN_rates.py`.
