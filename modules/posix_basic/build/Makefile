all:
	../bin/trace2model.py 
	skel template ../tmpl/makefile.tmpl --model ../model/grey-scott.json:posix_model --outfile ../repos/grey-scott/Makefile
	skel template ../tmpl/main_src_cxx.tmpl --model ../model/grey-scott.json:posix_model --outfile ../repos/grey-scott/main.cxx
	skel template ../tmpl/rank_src_cxx.tmpl --model ../model/grey-scott.json:posix_model --outfile ../repos/grey-scott/rank00000.cxx
	cd ../repos/grey-scott && make && cd -



