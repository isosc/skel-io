
import os
import subprocess

def try_cmd (cmd):
    cp = subprocess.run(cmd.split(' '))
    exit_status = cp.returncode
    assert exit_status == 0


def test_gtc_cycle():

    module_root = '{}/..'.format(os.path.dirname(os.path.abspath(__file__)))

    # Can we run skel at all?
    cmd = 'skel -h'
    try_cmd (cmd)

    # Try a loop with simple decomposition - generate CMakeLists.txt 
    jsonfile = '{}/model/gtc_small.json'.format(module_root)
    outfile = '{}/test/test_repo/CMakeLists.txt'.format(module_root) #need to make sure directory exists...
    tmplfile = '{}/tmpl/CMakeLists_txt.tmpl'.format(module_root)
    cmd = 'skel template --model {}:io-model --outfile {} {}'.format(jsonfile, outfile, tmplfile)
    try_cmd (cmd)

    # Try a loop with simple decomposition - generate the skeletal application 
    jsonfile = '{}/model/gtc_small.json'.format(module_root)
    outfile = '{}/test/test_repo/skel_gtc.cxx'.format(module_root)
    tmplfile = '{}/tmpl/skeletal_cxx.tmpl'.format(module_root)
    cmd = 'skel template --model {}:io-model --outfile {} {}'.format(jsonfile, outfile, tmplfile)
    try_cmd (cmd)

    # make sure build dir exists and is empty
    cmd = 'rm -rf {}/test/test_repo/build'.format(module_root)
    try_cmd (cmd)
    cmd = 'mkdir {}/test/test_repo/build'.format(module_root)
    try_cmd (cmd)

    # Run cmake from the build directory
    cmd = 'cmake ..'
    cwd = '{}/test/test_repo/build'.format(module_root)
    cp = subprocess.run(cmd.split(' '), cwd=cwd)
    exit_status = cp.returncode
    assert exit_status == 0

    # build the skeletal
    cmd = 'make'
    cwd = '{}/test/test_repo/build'.format(module_root)
    cp = subprocess.run(cmd.split(' '), cwd=cwd)
    exit_status = cp.returncode
    assert exit_status == 0

    # ...and run it
    cmd = 'mpirun -np 4 --oversubscribe {}/test/test_repo/build/skel_gtc'.format(module_root)
    try_cmd (cmd)

    # Now extract a model from the output
    cmd = '/home/logan/sw/spack/opt/spack/linux-ubuntu18.04-sandybridge/gcc-7.5.0/python-3.7.6-yaoqr5r7uwjfgu5gn6velor3b7qelxvj/bin/python3 {}/bin/bp-extract.py -b gtc_restart.bp -o gtc_final.json -n gtc'.format(module_root)
    try_cmd (cmd)

    cmd = 'diff model/gtc_small.json gtc_final.json'
    try_cmd (cmd)

    #assert (False)
