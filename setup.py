#!/bin/env python3

import sys
import os
import shutil
import subprocess


def alias_for(func):
    def decorator(_):
        return func

    return decorator


def main():
    verify_interpreter()
    verify_toolchain()
    configure_toolchain()
    print('All set up!')


def verify_interpreter():
    print('Verifying the interpreter...')

    major, minor, *_ = sys.version_info

    if major < 3 or minor < 11:
        panic('Python 3.11.0 or higher is required')


def verify_toolchain():
    print('Verifying the toolchain...')

    tools = [
        "gprbuild",
        "gprconfig",
        "clang",
        "make",
    ]

    for tool in tools:
        if not tool_exists(tool):
            panic(f'required toolchain component {tool} not found')


def configure_toolchain():
    print('Configuring the toolchain...')

    gprconfig = get_tool('gprconfig')
    compiler_listing = (subprocess
        .run(
            [gprconfig, '--mi-show-compilers'],
            stdout=subprocess.PIPE,
            text=True
        )
        .stdout
    )

    if 'name:CLANG-C\n' not in compiler_listing:
        panic('gprconfig could not find Clang-C in your PATH')

    gprconfig_invocation = subprocess.run([
        gprconfig,
        '--batch',
        '--config=C,,,,CLANG-C',
    ])

    if gprconfig_invocation.returncode != 0:
        panic('gprconfig failed')


@alias_for(shutil.which)
def get_tool(): ...


def tool_exists(tool):
    return get_tool(tool) != None


def panic(message):
    print(f'ERROR: {message}')
    exit(1)


if __name__ == '__main__': 
    main()
else:
    panic('setup is a script')
