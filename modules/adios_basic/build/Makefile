

gtc:
	mkdir -p ../repos/gtc
	skel template --model ../model/gtc_decomp.json:io-model --outfile ../repos/gtc/CMakeLists.txt ../tmpl/CMakeLists_txt.tmpl
	skel template  --model ../model/gtc_decomp.json:io-model --outfile ../repos/gtc/skel_gtc.cxx ../tmpl/skeletal_cxx.tmpl
	mkdir -p ../repos/gtc/build
	cd ../repos/gtc/build && cmake .. && make && cd -


run-gtc:
	../repos/gtc/build/skel_gtc



