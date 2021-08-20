
test:
	PYTHONPATH=${PYTHONPATH}:../../.. ../../../scripts/skel-io replay --tracedir=trace --outdir=out

build:
	mkdir -p out/build
	cd out/build && cmake .. && make && cd -

run:
	mpirun -np 4 --oversubscribe ./out/build/skel_lammps


