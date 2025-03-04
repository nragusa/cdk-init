import os
import shutil
import subprocess
import sys

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
    try:
        subprocess.run(
            ['zsh', '-i', '-c', 'venv'],
            capture_output=True,
            text=True,
            check=True
        )
        subprocess.run(
            ['uv', 'add', 'aws-cdk-lib'],
            capture_output=True,
            text=True,
            check=True
        )
        with open('.envrc', 'a') as f:
            f.write('export AWS_PROFILE=sso\n')
            f.write('export AWS_REGION=us-east-2\n')
        subprocess.run(
            ['direnv', 'allow'],
            capture_output=True,
            text=True,
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error running 'venv': {e}")
        sys.exit(1)
