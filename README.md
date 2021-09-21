# skel-io
Skel I/O is a generative tool for creating I/O mini applications. Skel I/O is driven by application traces produced by Tau, generating mini-apps that exhibit the traced behavior (I/O and communication).

## Dependencies
Requires skel, which is available [here](https://github.com/isosc/skel-core). (Dependency removed August '21)

The posix functionality uses tau directly to acquire application traces that feed io model creation. This was installed with spack using 
spack install tau@develop +adios2 +mpi +io +pthreads ~otf2 ~pdt ^hwloc@1.11.11

The ADIOS2.x functionality requires building an ADIOS wrapper that works with the tau tracing  in order to collect the ADIOS events. 

## Using Skel-IO

Detailed instructions coming soon...
