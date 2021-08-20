import argparse
from Cheetah.Template import Template
import json
from skel_io import __util, __path

def process (config):

    template_dir = f"{__path.get_project_root()}/tmpl"
    dumped_model_filename = f"{config.outdir}/model.json"
    filtered_model_filename = f"{config.outdir}/filtered_model.json"

    modelmap = {}
    modelmap['config'] = f"{config.tracedir}/skel-io.json"
    modelmap['posix-model'] = f"{filtered_model_filename}"

    # Load the config
    model_config = None
    with open(modelmap['config'], 'r') as model_config_file:
        model_config = json.load(model_config_file)

    cmakelists_template_filename = f"{template_dir}/CMakeLists_txt.tmpl"
    cmakelists_outfilename = f"{config.outdir}/CMakeLists.txt"

    main_template_filename = f"{template_dir}/main_src_cxx.tmpl"
    main_outfilename = f"{config.outdir}/skel_{model_config['name']}.cxx"

    rank_template_filename = f"{template_dir}/rank_src_cxx.tmpl"

    create_synthetic_data_template_filename = f"{template_dir}/create_synthetic_data_cxx.tmpl"
    create_synthetic_data_outfilename = f"{config.outdir}/create_synthetic_data.cxx"
    #_template_filename = f"{template_dir}/"

    # Create a model from the given traces
    __util.trace_to_model(config.tracedir, dumped_model_filename)
    __util.filter("addcompute", dumped_model_filename, filtered_model_filename)


    args = None


    # Instantiate the various parts of the miniapp
    # First, the CMakeLists.txt file
    __util.instantiate(cmakelists_template_filename, modelmap, args, cmakelists_outfilename)

    # Next, the main c++ code
    __util.instantiate(main_template_filename, modelmap, args, main_outfilename)

    # A utility to create any needed synthetic data
    __util.instantiate(create_synthetic_data_template_filename, modelmap, args, create_synthetic_data_outfilename)

    # Now, the detailed code for each rank
    args = {}
    for i in range(4):
        rank_outfilename = f"{config.outdir}/rank{i:05}.cxx"
        args['rank'] = i
        __util.instantiate(rank_template_filename, modelmap, args, rank_outfilename)


    #__util.instantiate(template_filename, modelmap, args, outfilename)
    

def commandline (argv):
  parser = argparse.ArgumentParser(prog='skel-io')
  subparsers = parser.add_subparsers(help='sub help', dest="subcommand")

  _parser_template = subparsers.add_parser('replay', help="Generate an I/O mini app for the given traces")
  _parser_template.add_argument('--tracedir', dest="tracedir", required="true") #Maybe provide a default later...
  _parser_template.add_argument('--outdir', dest="outdir", required="true") #Maybe provide a default later...
  #_parser_template.add_argument('--config_file', dest="outdir", required="true") #Maybe provide a default later...

  return (parser.parse_args(argv[1:])) # Skip the program name, and pass the rest to the parser

def main(argv):
    config = commandline(argv)
    print (config)

    # Do the work...
    process(config)

    




