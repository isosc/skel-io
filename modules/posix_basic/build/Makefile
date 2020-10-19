mpi-test:
	mkdir -p ../repos/mpi-test
	../bin/trace2model.py ../traces/mpi-test ../model/mpi-test.json
	../bin/filter addcompute ../model/mpi-test.json --outfile ../model/mpi-test-compute.json
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/CMakeLists_txt.tmpl --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/CMakeLists.txt
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/main_src_cxx.tmpl --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/skel_grey_scott_posix_compute.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/create_synthetic_data_cxx.tmpl --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/create_synthetic_data.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:0 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00000.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:1 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00001.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:2 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00002.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:3 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00003.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:4 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00004.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:5 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00005.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:6 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00006.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:7 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00007.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:8 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00008.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:9 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00009.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:10 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00010.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:11 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00011.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:12 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00012.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:13 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00013.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:14 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00014.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:15 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00015.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:16 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00016.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:17 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00017.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:18 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00018.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:19 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00019.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:20 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00020.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:21 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00021.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:22 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00022.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:23 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00023.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:24 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00024.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:25 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00025.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:26 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00026.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:27 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00027.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:28 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00028.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:29 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00029.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:30 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00030.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:31 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00031.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:32 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00032.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:33 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00033.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:34 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00034.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:35 --model ../model/mpi-test-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/mpi-test/rank00035.cxx
	mkdir -p ../repos/mpi-test/build
	cd ../repos/mpi-test/build && cmake .. && make && cd -


grey-scott:
	../bin/trace2model.py ../traces/grey-scott ../model/grey-scott.json
	#../bin/filter posixonly ../model/grey-scott.json --outfile ../model/grey-scott-posix-only.json
	../bin/filter addcompute ../model/grey-scott.json --outfile ../model/grey-scott-compute.json
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/CMakeLists_txt.tmpl --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/CMakeLists.txt
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/main_src_cxx.tmpl --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/skel_grey_scott_posix_compute.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/create_synthetic_data_cxx.tmpl --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/create_synthetic_data.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:0 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00000.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:1 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00001.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:2 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00002.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:3 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00003.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:4 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00004.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:5 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00005.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:6 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00006.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:7 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00007.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:8 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00008.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:9 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00009.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:10 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00010.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:11 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00011.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:12 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00012.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:13 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00013.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:14 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00014.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:15 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00015.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:16 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00016.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:17 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00017.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:18 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00018.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:19 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00019.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:20 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00020.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:21 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00021.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:22 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00022.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:23 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00023.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:24 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00024.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:25 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00025.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:26 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00026.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:27 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00027.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:28 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00028.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:29 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00029.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:30 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00030.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:31 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00031.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:32 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00032.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:33 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00033.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:34 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00034.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:35 --model ../model/grey-scott-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00035.cxx
	mkdir -p ../repos/grey-scott/build
	cd ../repos/grey-scott/build && cmake .. && make && cd -

grey-scott-posix-only:
	../bin/trace2model.py 
	../bin/filter posixonly ../model/grey-scott.json --outfile ../model/grey-scott-posix-only.json
	../bin/filter addcompute ../model/grey-scott-posix-only.json --outfile ../model/grey-scott-posix-compute.json
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/CMakeLists_txt.tmpl --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/CMakeLists.txt
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/main_src_cxx.tmpl --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/skel_grey_scott_posix_compute.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/create_synthetic_data_cxx.tmpl --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/create_synthetic_data.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:0 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00000.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:1 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00001.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:2 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00002.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:3 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00003.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:4 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00004.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:5 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00005.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:6 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00006.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:7 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00007.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:8 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00008.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:9 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00009.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:10 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00010.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:11 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00011.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:12 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00012.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:13 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00013.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:14 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00014.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:15 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00015.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:16 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00016.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:17 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00017.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:18 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00018.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:19 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00019.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:20 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00020.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:21 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00021.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:22 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00022.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:23 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00023.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:24 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00024.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:25 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00025.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:26 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00026.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:27 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00027.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:28 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00028.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:29 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00029.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:30 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00030.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:31 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00031.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:32 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00032.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:33 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00033.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:34 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00034.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:35 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00035.cxx
	mkdir -p ../repos/grey-scott/build
	cd ../repos/grey-scott/build && cmake .. && make && cd -

#Need to add command line args to filters to make this work
grey-scott-skel:
	../bin/trace2model.py 
	../bin/filterposixonly.py
	../bin/filteraddcomputeevents.py
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/CMakeLists_txt.tmpl --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/CMakeLists.txt
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/main_src_cxx.tmpl --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/skel_grey_scott_posix_compute.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/create_synthetic_data_cxx.tmpl --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/create_synthetic_data.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:0 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00000.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:1 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00001.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:2 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00002.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:3 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00003.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:4 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00004.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:5 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00005.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:6 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00006.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:7 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00007.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:8 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00008.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:9 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00009.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:10 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00010.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:11 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00011.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:12 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00012.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:13 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00013.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:14 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00014.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:15 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00015.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:16 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00016.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:17 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00017.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:18 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00018.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:19 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00019.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:20 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00020.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:21 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00021.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:22 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00022.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:23 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00023.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:24 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00024.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:25 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00025.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:26 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00026.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:27 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00027.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:28 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00028.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:29 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00029.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:30 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00030.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:31 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00031.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:32 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00032.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:33 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00033.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:34 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00034.cxx
	PYTHONPATH=${PWD}/../tmpl:${PYTHONPATH} skel template ../tmpl/rank_src_cxx.tmpl --arg rank:35 --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile ../repos/grey-scott/rank00035.cxx
	mkdir -p ../repos/grey-scott/build
	cd ../repos/grey-scott/build && cmake .. && make && cd -

refresh:
	skel template ../tmpl/Makefile.tmpl --model ../model/grey-scott-posix-compute.json:posix-model,../model/tweak.json:tweak --outfile Makefile



create_synthetic:
	cd ../repos/grey-scott/build && ./create_synthetic_data && cd -

run:
	cd ../repos/grey-scott/build && mpirun -np 36 -oversubscribe ./skel_grey_scott_posix_compute && cd -
	cd ../repos/grey-scott/build && ~/sw/skel-io/bin/skel-io-merge && cd -

run-tau:
	cd ../repos/grey-scott/build && mpirun -np 36 -oversubscribe tau_exec -T mpi,pthread -io -skel ./skel_grey_scott_posix_compute && cd -

plot:
	cd ../repos/grey-scott/build && ~/sw/skel-io/bin/skel-io-plot && cd -
	

.PHONY: refresh create_synthetic run run-tau plot


