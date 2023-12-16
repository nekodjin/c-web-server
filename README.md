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

To begin, you'll need to run the setup script, `setup.py`. This will verify the
toolchain components, and then automaticall register a toolchain configuration.
If you're missing any toolchain components, the script will notify you at this
step.

After setup, use `make` to build and start the server. To build the server
without running it, use `make build`. The server binary is called `server`.
