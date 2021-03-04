# skel-io
I/O related models and templates for skel

## Dependencies
Requires skel, which is available [here](https://github.com/isosc/skel-core).

The posix module uses tau to acquire application traces that feed io model creation. This was installed with spack using 
spack install tau@develop +adios2 +mpi +io +pthreads ~otf2 ~pdt ^hwloc@1.11.11
