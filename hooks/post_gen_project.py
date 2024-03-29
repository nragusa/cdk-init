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
        ['/home/ec2-user/.pyenv/shims/pipenv', '--python', '3.12']
    )
    subprocess.run(
        ['/home/ec2-user/.pyenv/shims/pipenv', 'install', 'aws-cdk-lib']
    )
