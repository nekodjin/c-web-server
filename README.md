# C Web Server

This is an educational project. The goal is for me to learn the low-level
details of web servers, by writing one from scratch in C.

The project should compile and run on any Unix-like operating system. It has
been tested on Linux.

## Building and Running

This project requires the following toolchain components to be accessible in
PATH:
- Python 3.11 or higher (as `python3`)
- GPRBuild (as `gprbuild`)
- GPRConfig (as `gprconfig`)
- Clang-C
- Makefile
Toolchain components must be accessible through the listed binary name, if there
is one.

Use `make` (or `make run`) to build and run the server. To build the server
without running it, use `make build`. The server executable is called `server`.

The first time you build the server, a setup script will run. This script
verifies that the requried toolchain components are installed, and then
generates and stores a toolchain configuration.

To remove old build artifacts in preparation for building from scratch, use
`make clean`. This will also remove the stored toolchain configuration. You
should run `make clean` whenever you update or modify a toolchain component,
such as your Clang-C installation.

## Troubleshooting

In some cases, GPRConfig may fail to detect your installation of Clang-C. If
this happens, you will need to perform manual setup. To do this, run the command
`gprconfig` with no arguments. GPRConfig will show you a list of detected
compilers - select any compiler labelled 'for C', and enter the associated
number. Press enter, followed by 's', followed by enter. GPRConfig will generate
a `default.cgpr` file storing your configuration. To change the configuration,
repeat this process.

Note that the server's build configuration makes certain assumptions about the
command-line API that the compiler will expose - namely, that the compiler
supports all of the Clang-C arguments. If you manually chose a compiler that
does not support these arguments, you may get some build errors. Either select
a more appropriate compiler, or edit the switches passed to the C compiler in
`server.gpr`.

After manually configuring your toolchain, you will need to create a setup
artifact to inform Makefile that setup is already complete. Just run the command
`touch .setup_artifact`.
