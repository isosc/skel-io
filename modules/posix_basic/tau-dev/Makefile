fetch:
	[ ! -f pooky2-with-posix-yaml.tgz ] || mv pooky2-with-posix-yaml.tgz pooky2-with-posix-yaml.tgz.old # Move to .old if exists
	wget http://www.nic.uoregon.edu/~khuck/pooky2-with-posix-yaml.tgz
	tar -xvzf pooky2-with-posix-yaml.tgz
	cp pooky2/rank000*.trace ../traces/grey-scott/
