#!/usr/bin/env python
import os
import shutil
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_directory(directory):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY,
                  directory), ignore_errors=True)


if __name__ == '__main__':

    remove_file('requirements.txt')
    remove_file('requirements-dev.txt')
    remove_directory('.venv/')
    subprocess.run(
        ['poetry', 'add', 'aws-cdk-lib'],
        capture_output=True,
        text=True,
        check=True
    )
