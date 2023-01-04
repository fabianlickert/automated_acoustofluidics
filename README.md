# automated_acoustofluidics
Automated control of an acoustofluidic setup

# Overview of the system
The acoustofluidic measurement setup consists of the following components:
- Camera (PCO.edge 5.5) 
- Switching valve (MX Series II™ 2 Position/6 Port PEEK Switching Valve)
- Signal generator (Digilent Analog Discovery 2)
- Amplifier (Toellner TOE 7607)
- Syringe pump (KdScientific Legato 110 )
- Linear Stage (

In this repository Python drivers are provided to interface all the system components in order to automate the process of an acoustofluidic measurement.

## Required packages
A list of the required packages can be found in the file requirements.txt. In particular make sure that the following packages are installed

- Digilent's DWF library wrapper dwf (pip install dwf)
- pco camera package (pip install pco)
- skimage (pip install scikit-image)
- .NET Common Language Runtime clr (pip install pythonnet)
- the usual (numpy, os, time, serial) as listed in the requirements.txt

## Testing of the sub-components
Driver interfaces are provided for the pco camera, the Analog Discovery 2, the syringe pump, the switching valve and the linear stage.

## Use of the main script
1.	The main script labeled “run_frequency_sweep_XXXX.ipnyb” can be opened using Jupyter Notebooks. The recommended procedure is:
a.	Start Anaconda Navigator
b.	Install the environment ENV.yml that is located on the T-drive, if not already done. This environment has all necessary Python packages pre-installed.
c.	Switch to the local environment 
d.	Run Jupyter Notebook
e.	Open the main script “run_frequency_sweep_XXXX.ipnyb”. There are several versions, all with slightly adjusted functionality. Chose the one fitting the experiment.
f.	Make sure that all devices are connected via USB to the lab computer, and that they are switched on:
i.	Camera
ii.	Analog Discovery
iii.	Syringe pump
iv.	Switching valve
v.	Amplifier
vi.	Light source
g.	Enter the correct COM-ports for the Syringe pump and the Switching valve in the Python script.
2.	Run the Python script in a specified frequency interval. Make the necessary adjustments to the settings in terms of
a.	Actuation voltage amplitude
b.	Delay time and exposure time of the camera
c.	Flushing flow rate and time
d.	Number of images acquired and resolution
3.	The resulting images will be stored in the folder … \automated_microfluidics\img

## Work flow
