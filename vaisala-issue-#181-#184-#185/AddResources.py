# Add new re-usable resources into LwM2M object XML files.
#
# This script imports a library (lwm2mv10_lib) that has been generated with generateDS tool.
# https://www.davekuhlman.org/generateDS.html
#
# To re-generate this library, follow generateDS documentation how to install generateDS and then issue command:
# 
#   python generateDS.py -o lwm2mv10_lib.py LWM2M.xsd
# 
# where LWM2M.xsd can be downloaded from http://www.openmobilealliance.org/tech/profiles/LWM2M.xsd 
# Place the generated library in the same directory with AddResources.py.
#
# To add re-usable resources, first edit global variable SOURCES_TO_PROCESS. 
# This variable contains an array of source object definitions consisting of object id, name and an array of re-usable resources to add per object. 
# Issue the following command in the directory containing object XML files:
#
#   python <your_path_to>/AddResources.py ../output
#
# where output is the generated folder for updated XML files.
# This software is covered by The MIT License: http://www.opensource.org/licenses/mit-license.php

import os
import sys
import lwm2mv10_lib


# parse re-usable resources
reusables = lwm2mv10_lib.parse("Common.xml", silence=True)

# re-usable resource constants
RR_APPLICATION_TYPE                 = 5750
RR_TIMESTAMP                        = 5518
RR_FRACTIONAL_TIMESTAMP             = 6050
RR_MEASUREMENT_QUALITY_INDICATOR    = 6042
RR_MEASUREMENT_QUALITY_LEVEL        = 6049

# re-usable resource attributes
RR_MULTIPLE_INSTANCES   = "Single"
RR_MANDATORY            = "Optional"

# namespace to use
NAMESPACE = ' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://openmobilealliance.org/tech/profiles/LWM2M.xsd"'

# container class for source objects
class SourceObject:

    def __init__(self, objId, name, rrIdsToAdd):
        self.objId = objId
        self.name = name
        self.rrIdsToAdd = rrIdsToAdd
    
    def getId(self):
        return self.objId

    def getName(self):
        return self.name

    def getFileName(self):
        return str(self.objId) + ".xml"

    def getRRIdsToAdd(self):
        return self.rrIdsToAdd 


# define list of LwM2M objects and resources per object to add
SOURCES_TO_PROCESS = [ \
    SourceObject( 3200, "Digital Input",       [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP,                                                                  ] ), \
    SourceObject( 3201, "Digital Output",      [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP                                                                   ] ), \
    SourceObject( 3202, "Analog Input",        [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3203, "Analog Output",       [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3300, "Generic Sensor",      [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3301, "Illuminance",         [RR_APPLICATION_TYPE,  RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3302, "Presence",            [RR_APPLICATION_TYPE,  RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3303, "Temperature",         [RR_APPLICATION_TYPE,  RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3304, "Humidity",            [RR_APPLICATION_TYPE,  RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3305, "Power Measurement",   [RR_APPLICATION_TYPE,  RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3306, "Actuation",           [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP                                                                   ] ), \
    SourceObject( 3308, "Set Point",           [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP                                                                   ] ), \
    SourceObject( 3310, "Load Control",        [RR_APPLICATION_TYPE,  RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP                                                                   ] ), \
    SourceObject( 3312, "Power Control",       [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP                                                                   ] ), \
    SourceObject( 3313, "Accelerometer",       [RR_APPLICATION_TYPE,  RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3314, "Magnetometer",        [RR_APPLICATION_TYPE,  RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3315, "Barometer",           [RR_APPLICATION_TYPE,  RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3316, "Voltage",             [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3317, "Current",             [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3318, "Frequency",           [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3319, "Depth",               [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3320, "Percentage",          [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3321, "Altitude",            [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3322, "Load",                [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3323, "Pressure",            [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3324, "Loudness",            [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3325, "Concentration",       [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3326, "Acidity",             [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3327, "Conductivity",        [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3328, "Power",               [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3329, "Power Factor",        [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3330, "Distance",            [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3331, "Energy",              [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3332, "Direction",           [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3333, "Time",                [                                                             RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3334, "Gyrometer",           [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3335, "Colour",              [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3336, "Location",            [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3337, "Positioner",          [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3338, "Buzzer",              [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP                                                                   ] ), \
    SourceObject( 3342, "On/Off switch",       [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP                                                                   ] ), \
    SourceObject( 3346, "Rate",                [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject( 3347, "Push button",         [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP                                                                   ] ), \
    SourceObject( 3348, "Multi-state Selector",[                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP                                                                   ] ), \
    SourceObject( 3349, "Bitmap",              [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP                                                                   ] ), \
    SourceObject( 3350, "Stopwatch",           [                      RR_TIMESTAMP, RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ), \
    SourceObject(10311, "Solar Radiation",     [                                    RR_FRACTIONAL_TIMESTAMP, RR_MEASUREMENT_QUALITY_INDICATOR, RR_MEASUREMENT_QUALITY_LEVEL   ] ) \
        ]

# re-define indentation with tabs
def tabIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('\t')


# overwrite default whitespace indentation with tab indentation
lwm2mv10_lib.showIndent = tabIndent

# read file header lines
# notice that the code-generated parser omits the header, so it needs to be read with a conventional style 
def readHeader(fileName):
    with open(fileName, "r", encoding="utf-8") as f:
        header = ""
        line = f.readline()
        while line:
            if "<LWM2M" in line:
                break
            header += line
            line = f.readline()
        return header

# search for the specified re-usable resource
def getReusableResource(rrId):
    objectList = reusables.get_Object()
    for obj in objectList:
        resources = obj.get_Resources()
        for item in resources.get_Item():
            if item.get_ID() == rrId:
                # trim description leading and tailing whitespaces
                description = item.get_Description()
                item.set_Description(description.strip())
                # add missing attributes
                item.set_MultipleInstances(RR_MULTIPLE_INSTANCES)
                item.set_Mandatory(RR_MANDATORY)
                return item
    return None

# process given source
def process(source):
    root = lwm2mv10_lib.parse(source.getFileName(), silence=True)
    objectList = root.get_Object()
    
    sys.stdout.write('{:<10d}{:<25s}'.format(source.getId(), source.getName()))

    for obj in objectList:
        resources = obj.get_Resources()
        for rrId in source.getRRIdsToAdd():
            rr = getReusableResource(rrId)
            assert rr is not None, "Re-usable resource %d not found." % rrId
            resources.add_Item(rr)
            sys.stdout.write('{:<5d}'.format(rrId))

    sys.stdout.write("\n")

    return root

# write header + object into a file
def writeFile(targetDirectory, fileName, header, obj):
    with open(os.path.join(targetDirectory, fileName), "w", encoding="utf-8") as f:
        f.write(header)
        obj.export(f, 0, '', NAMESPACE)


def main():

    args = sys.argv[1:]
    if len(args) == 1:
        targetDirectory = args[0]

        if not os.path.exists(targetDirectory):
            os.makedirs(targetDirectory)

        sys.stdout.write("Processing...\n")
        sys.stdout.write('{:<10s}{:<25s}{:<20s}\n'.format("Object ID", "Object Name", "Added Resources"))
        dash = '-' * 70
        print(dash)

        count = 0
        for source in SOURCES_TO_PROCESS:
            target = process(source)
            fileName = source.getFileName()
            header = readHeader(fileName)
            writeFile(targetDirectory, fileName, header, target)
            count = count + 1

        sys.stdout.write("Processed total of %d objects.\n" % count)

    else:
        sys.stdout.write("USAGE: AddResources.py <targetPath>\n")


if __name__ == '__main__':
    main()