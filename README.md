# bulk_update_tool

This repository contains Python scripts to bulk update LwM2M object XML files. 

Scripts import a library (lwm2mv10_lib) that is generated with [generateDS](https://www.davekuhlman.org/generateDS.html) tool.
The library is provided readily generated. To re-generate this library, follow generateDS documentation how to install generateDS and then issue command:

  python generateDS.py -o lwm2mv10_lib.py LWM2M.xsd
 
where [LWM2M.xsd](http://www.openmobilealliance.org/tech/profiles/LWM2M.xsd) is the schema file which can be downloaded from OMA SpecWorks. 

The generated library provides all the boiler plate code to parse LwM2M object XML file into a type safe tree model. 
In your bulk update script you can use the functionality of the library to edit and validate the tree model and finally write
it into a XML file, all with a reasonably small number of code lines.  

