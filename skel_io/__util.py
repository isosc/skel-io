from Cheetah.Template import Template
import glob
import json
import re
import sys

#import yaml

instantiated_templates = {}

def instantiate(template_filename, modelmap, args, outfilename):

    models = {}
    for name in modelmap.keys():
        with open (modelmap[name]) as modelfile:
            models[name] = json.load(modelfile)

    # Process the  template
    t = Template(file=template_filename)
    t.models = models
    t.arg = args
    t.instantiated_templates = instantiated_templates

    # Instantiate template
    instantiated_templates[outfilename] = str(t)

    with open (outfilename, 'w') as outfile:
      outfile.write(instantiated_templates[outfilename])
    return



# Merging in the original pipeline activites as utility functions...

#usage: trace2model <trace_dir> <outfile>

def trace_to_model(trace_dir, outfile):

#trace_dir = sys.argv[1]
#outfile = sys.argv[2]
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





def filter(subcommand, modelfile, outfile):

    if not subcommand in ['posixonly', 'addcompute']:
        raise ValueError('Unsupported filter type passed to __util.filter')

    if subcommand == 'posixonly':
        do_posixonly(modelfile, outfile)
    elif subcommand == 'addcompute':
        do_addcompute(modelfile, outfile)


def do_posixonly(model, outfile):

    #usage: filterposixonly <model> -o <outfile>

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
        json.dump (posix_model, out, indent=3)



def do_addcompute(model, outfile):
    #usage: filteraddcomputeevents <model> -o <outfile>

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
                gap = this_one['ts'] - (previous_one['ts'] + previous_one['dur'])
                if gap < threshold:
                    augmented_events.append (this_one)
                    continue # Skip small gaps
                compute_event = {}
                compute_event['cat'] = 'SKEL'
                compute_event['name'] = 'compute'
                compute_event['dur'] = gap
                augmented_events.append (compute_event)
                augmented_events.append (this_one)
            print ("Total {} events after augmenting".format(len(augmented_events) ) )
            posix_model['events'].append (augmented_events)
            print("Parsed a rank, found ", len(augmented_events), " posix events")

    posix_model['num_ranks'] = doc['num_ranks']

    with open (outfile, 'w') as out:
        json.dump (posix_model, out, indent=2)




