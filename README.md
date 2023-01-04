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

- Digilent's DWF library wrapper dwf ('pip install dwf')
- pco camera package (pip install pco)
- skimage (pip install scikit-image)
- .NET Common Language Runtime clr (pip install pythonnet)
- the usual (numpy, os, time, serial) as listed in the requirements.txt

## Testing of the sub-components
Driver interfaces are provided for the pco camera, the Analog Discovery 2, the syringe pump, the switching valve and the linear stage.

## Use of the main script
1.	Open the main script “run_frequency_sweep_XXXX.ipnyb” using Jupyter Notebooks.
2.	Make sure that all devices are connected via USB to the lab computer, and that they are switched on:
  -	Camera
  -	Analog Discovery
  -	Syringe pump
  -	Switching valve
  -	Amplifier
  -	Light source
3.	Enter the correct COM-ports for the Syringe pump and the Switching valve in the Python script.
4.	Run the Python script in a specified frequency interval. Make the necessary adjustments to the settings in terms of
  -	Actuation voltage amplitude
  -	Delay time and exposure time of the camera
  -	Flushing flow rate and time
  -	Number of images acquired and resolution
5.	The resulting images will be stored in the folder \img

## Work flow
