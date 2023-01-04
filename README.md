# automated_acoustofluidics
Automated control of an acoustofluidic setup

# Overview of the system
The acoustofluidic system consists of the following components:
- Camera
- Switching valve
- Digilent Analog Discovery 2
- Amplifier
- Syringe pump

In this repository Python drivers are provided to interface all the system components in order to automate the process of an acoustofluidic measurement.

## Required packages
A list of the required packages can be found in the file requirements.txt. In particular make sure that the following packages are installed

- Digilent's DWF library wrapper dwf (pip install dwf)
- pco camera packages (pip install pco)
