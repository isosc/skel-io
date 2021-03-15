#!/usr/bin/env python3

import glob
import json
import re
import sys
#import yaml


#usage: trace2model <trace_dir> <outfile>

trace_dir = sys.argv[1]
outfile = sys.argv[2]
allevents = [] # List of all events by rank
posix_model = {}
posix_model['name'] = 'grey_scott'

print ("Extracting traces in {} to {}".format(trace_dir, outfile) )


trace_list = glob.glob("{}/*.trace".format(trace_dir) )
trace_list.sort()
print (trace_list)

for filename in trace_list:
    # Get the MPI rank index
    try:
        rank = int(re.search('{}/rank(.+?)\.trace'.format(trace_dir), filename).group(1))
    except AttributeError:
        sys.exit("Error, can't find rank in filename", filename)

    # Parse the trace
    with open(filename, 'r') as f: # open in readonly mode
        #inyaml = yaml.load(f, Loader=yaml.FullLoader)
        intrace = json.load(f)
        # Sort the entries by timestamp (because the ranks are multithreaded,
        # and because the events are recorded after the event finishes
        # there's a chance that events are slightly out of order
        # Because the timestamp is when the event was started.
        allevents.append (sorted(intrace, key=lambda k: k['ts']) )
        print("Parsed", filename, "found", len(intrace), "events")

posix_model['events'] = allevents
posix_model['num_ranks'] = len(allevents)

with open (outfile, 'w') as out:
    json.dump (posix_model, out)


