"""Pre-generation project hook."""

import subprocess
import sys

app_name = '{{cookiecutter.project_name}}'

try:
    subprocess.run(['cdk', 'init', '--language=python'], capture_output=True, text=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running 'cdk init': {e}")
    sys.exit(1)
