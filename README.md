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

Use `make` (or `make run`) to build and run the server. To build the server
without running it, use `make build`. The server executable is called `server`.

The first time you build the server, a setup script will run. This script
verifies that the requried toolchain components are installed, and then
generates and stores a toolchain configuration.

To remove old build artifacts in preparation for building from scratch, use
`make clean`. This will also remove the stored toolchain configuration. You
should run `make clean` whenever you update or modify a toolchain component,
such as your Clang-C installation.
