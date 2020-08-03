#!/usr/bin/env python3

import glob
import json
import re

#usage: filterposixonly <model> -o <outfile>

model = '../model/grey-scott.json'
outfile = '../model/grey-scott-posix-only.json'
allevents = [] # List of all events by rank
posix_model = {}
posix_model['name'] = 'grey_scott_posix_only'
posix_model['events'] = []
print ("Filtering model {} to {}".format(model, outfile) )

# Parse the yaml
with open(model, 'r') as f: # open in readonly mode
    doc = json.load(f)

    for rank_events in doc['events']:
        posix_model['events'].append ([event for event in rank_events if event['type'] == 'POSIX'] )
        print("Parsed a rank, found ", len(posix_model['events']), " posix events")

posix_model['num_ranks'] = doc['num_ranks']

with open (outfile, 'w') as out:
    json.dump (posix_model, out)


