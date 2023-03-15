import subprocess

app_name = '{{ cookiecutter.project_name}}'

subprocess.run(
    ['/home/ec2-user/.nvm/versions/node/v16.4.1/bin/cdk', 'init', '--language=python']
)