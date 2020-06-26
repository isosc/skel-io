##!/usr/bin/env python3

import adios2 as ad
import argparse
import json
import sys

use = "low level" #The high level adios python api does not currently support block info

def parse_command_line():
  parser = argparse.ArgumentParser(prog='bp-extract')
  parser.add_argument('-b,--bpfile', dest="bpfile", required="true")
  parser.add_argument('-o,--outfile', dest="outfile", required="true")
  parser.add_argument('-n,--name', dest="appname", required=False, default="appname")

  return (parser.parse_args(sys.argv[1:])) # Skip the program name, and pass the rest to the parser


def detect_serial_write(var):

    if len(var['blocks']) > 1:
      return None

    rank = var['blocks'][0]['WriterID']

    var.pop('blocks', None)
    var['decomp'] = {}
    var['decomp']['type'] = 'serial'
    var['decomp']['rank'] = rank
    return var


def detect_irregular_list(var):
  """
  Look for  the situation where each process writes a chunk in one dimension
  where the chunks may be of different sizes.
  """
  if var['shape'] == '':
      return None


  return None


def detect_simple_decomp(var):
  """
  Look for a simple domain decomposition in the blocks of this variable. This is defined
  as a situation where each process writes an equal sized block of an array, and one of
  the array dimensions is used to separate data written by the ranks. If found, return
  a variable descriptor (dictionary) that replaces the raw block data with a simple
  description of the domain decomposition. Return None otherwise.
  """
  if var['shape'] == '':
      return None
  ndims = len(var['shape'])
  for dim in range(ndims):
      print ("Checking dim {}".format(dim) )
      have_counterexample = False
      for block in var['blocks']:
        if not int(block['WriterID']) == int(block['Start'].split(',')[dim]):
          print ("Found counterexample at block")
          print (block)
          print ("Owner is {}".format(block['WriterID']))
          print ("Comparing to {}".format(block['Start'][dim]))
          have_counterexample = True
          break
      if not have_counterexample:
        print ("Found simple decomposition for dim {}.".format(dim))
        # Prepare return value and return it
        var.pop('blocks', None)
        var['decomp'] = {}
        var['decomp']['type'] = 'simple'
        var['decomp']['dim'] = dim
        return var

  # Didn't find a simple decomposition
#  print ("Failed to find a simple decomposition")
  return None



# This is probably defunct, but leaving it in for now.
def high_level(config):
  model_dict = {}
  model_dict['vars'] = []
  with ad.open(config.bpfile, 'r') as f:
    vars = f.available_variables()
#    print (vars)
    for key in vars.keys():
      var_dict = {}
      print (key)
      var_dict['name'] = key
      var_dict['type'] = vars[key]['Type']
      model_dict['vars'].append (var_dict)

    attrs = f.available_attributes()
#    print (attrs)

    return model_dict



def low_level(config):
  model_dict = {}
  model_dict['vars'] = []
  task_dict = {}
  task_dict['vars'] = []
  adios_obj = ad.ADIOS()
  io = adios_obj.DeclareIO("the_IO")
  engine = io.Open(config.bpfile, 2) # 2 = read
  #print (dir(io))
  #print (dir(engine))
  vars = io.AvailableVariables()
  #print (vars)
  for key in vars.keys():
    var_dict = {}
    #print (key)
    var = io.InquireVariable(key)
    #print (var)
    #print (dir(var))
    #print (var.BlockID())
    var_dict['name'] = key
    var_dict['type'] = vars[key]['Type']
    model_dict['vars'].append (var_dict)
    var_dict['blocks'] = engine.BlocksInfo(key, 0)
    var_dict['shape'] = var.Shape()

    # Pull the blocks here
#    print (dir(io))
#    print ("DETECTING:::")
#    print (var_dict)

    # Make the calls to the decomp detectors
    outvar=detect_serial_write(var_dict)
    if outvar:
      task_dict["vars"].append(outvar)
      continue

    outvar=detect_simple_decomp(var_dict)
    if outvar:
      task_dict["vars"].append(outvar)
      continue

    outvar=detect_irregular_list(var_dict)
    if outvar:
      task_dict['vars'].append(outvar)
      continue

    print ("Unable to detect domain decomposition for {}, aborting.".format(var_dict["name"]))
    quit()

  task_dict['filename'] = config.bpfile

  # Now create the rest of the structure for the json
  root = {}
  root['name'] = config.appname
  root['num_tasks'] = 4
  root['iotasks'] = []
  root['iotasks'].append(task_dict)


#  print ("OUTPUT:::")
#  print (task_dict)
  return root


def main(config):
#  print ("bpextract") 
  #print (config)

  if use == "high level":
    model_dict = high_level(config)
  else:
    model_dict = low_level(config)

#  print ("Here's what we got")
#  print (model_dict)

  # Write out the result
  with open (config.outfile, 'w') as out:
      json.dump(model_dict, out, indent=4)
      out.write('\n')

if __name__=="__main__":
  config = parse_command_line()
  main (config)
