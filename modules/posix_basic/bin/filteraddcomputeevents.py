#!/usr/bin/env python3

import glob
import json
import re

#usage: filteraddcomputeevents <model> -o <outfile>

model = '../model/grey-scott-posix-only.json'
outfile = '../model/grey-scott-posix-compute.json'
threshold = 1000
allevents = [] # List of all events by rank
posix_model = {}
posix_model['name'] = 'grey_scott_posix_compute'
posix_model['events'] = []
print ("Filtering model {} to {}".format(model, outfile) )

# Parse the yaml
with open(model, 'r') as f: # open in readonly mode
    doc = json.load(f)

    for rank_events in doc['events']:
        # Insert compute events into this rank's event list
        print ("Preparing to add compute events to {} existing events".format (len(rank_events) ) )
        augmented_events = []
        augmented_events.append (rank_events[0])
        for this_one, previous_one in zip(rank_events[1:], rank_events):
            gap = this_one['timestamp'] - (previous_one['timestamp'] + previous_one['duration'])
            if gap < threshold:
                augmented_events.append (this_one)
                continue # Skip small gaps
            compute_event = {}
            compute_event['type'] = 'SKEL'
            compute_event['function'] = 'compute'
            compute_event['duration'] = gap
            augmented_events.append (compute_event)
            augmented_events.append (this_one)
        print ("Total {} events after augmenting".format(len(augmented_events) ) )
        posix_model['events'].append (augmented_events)
        print("Parsed a rank, found ", len(augmented_events), " posix events")

posix_model['num_ranks'] = doc['num_ranks']

with open (outfile, 'w') as out:
    json.dump (posix_model, out)


