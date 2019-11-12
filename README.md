# bulk_update_tools

## AddResources.py
Bulk adds re-usable resources into LwM2M object XML files.     

This script imports a library (lwm2mv10_lib) that is generated with [generateDS](https://www.davekuhlman.org/generateDS.html) tool.
To re-generate this library, follow generateDS documentation how to install generateDS and then issue command:

  python generateDS.py -o lwm2mv10_lib.py LWM2M.xsd
 
where [LWM2M.xsd](http://www.openmobilealliance.org/tech/profiles/LWM2M.xsd) is the schema file which can be downloaded from OMA SpecWorks. Place the generated library in the same directory with AddResources.py.

To select objects to update, edit AddResources.py global variable SOURCES_TO_PROCESS. It contains definition of object id, name and an array of re-usable resources to add per object. 

To bulk process LwM2M object files, clone [lwm2m_registry](https://github.com/OpenMobileAlliance/lwm2m-registry) repository to the same directory 
where AddResources.py and lwm2mv10_lib.py are. Then issue the following command in the repository root directory:

  python ../AddResources.py ../output

where output is the generated folder for updated XML files. Check the output XML files by comparing with diff against the originals.
