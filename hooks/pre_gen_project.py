import subprocess

app_name = '{{ cookiecutter.project_name}}'

subprocess.run(
    ['/home/ec2-user/.npm-packages/bin/cdk', 'init', '--language=python']
)
