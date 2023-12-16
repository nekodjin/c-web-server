#!/bin/env python3

import sys
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
    write_setup_artifact()
    print('All set up!')


def verify_interpreter():
    print('Verifying the interpreter...')

    major, minor, *_ = sys.version_info

    if major < 3 or minor < 11:
        panic('Python 3.11.0 or higher is required')


def verify_toolchain():
    print('Verifying the toolchain...')

    tools = [
        'gprbuild',
        'gprconfig',
        'clang',
        'make',
    ]

    missing_tools = []

    for tool in tools:
        if not tool_exists(tool):
            missing_tools.append(tool)

    if 'clang' in missing_tools:
        missing_tools.remove('clang')
        print('WARNING: could not find Clang-C in PATH as `clang`')

    if len(missing_tools) != 0:
        panic(f'the required components {", ".join(missing_tools)} are missing')


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


def write_setup_artifact():
    with open('.setup_artifact', 'w') as artifact:
        # the artifact doesn't need to contain
        # anything, it just needs to exist.
        artifact.write('')


@alias_for(shutil.which)
def get_tool(): ...


def tool_exists(tool):
    return get_tool(tool) is not None


def panic(message):
    print(f'ERROR: {message}')
    exit(1)


if __name__ == '__main__': 
    main()
else:
    panic('setup is a script')
