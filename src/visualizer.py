#! /usr/bin/env python2
from vis import visualizer as vis
from load_json import load_map_from_file as loadJson
import json
import argparse

# Define arguements
parser = argparse.ArgumentParser(
    description="Launches the visualizer")
parser.add_argument(
    "-f", "--logFile",
    help="Specifies a log file to use",
    default="src/gamerunner/log.json")
parser.add_argument(
    "-m", "--mapJson",
    help="The map file for the visualizer",
    default="src/gamerunner/map.json")
parser.add_argument("-d", "--debug", help="Turn on Debug", dest='debug', action='store_true')
parser.set_defaults(debug=False)
args = parser.parse_args()  # parse args

try:
    with open(args.mapJson) as json_file:
        mapJsonObject = loadJson(json_file)
    if(mapJsonObject is None):
        raise Exception
except IOError:
    print("File " + args.mapJson + " does not exist")
    raise
    exit(1)
except Exception:
    print("Failed to parse map json data")
    raise
    exit(1)

if (args.logFile is not None):
    try:
        teamJsonObject = None
        logJsonObject = []
        with open(args.logFile) as json_file:
            for line in json_file:
                if teamJsonObject is None:
                    teamJsonObject = json.loads(line)
                else:
                    logJsonObject.append(json.loads(line))
        if(logJsonObject is None):
            raise Exception
    except IOError:
        print("File " + args.logJson + " does not exist")
        raise
        exit(1)
    except Exception:
        print("Failed to parse log json data")
        raise
        exit(1)

print "Starting Visualizer"
# Initialize Visualizer
if (args.logFile is not None):
    visualizer = vis.Visualizer(mapJsonObject, args.debug, logJsonObject, alone=True)
else:
    visualizer = vis.Visualizer(mapJsonObject, args.debug, alone=True)
