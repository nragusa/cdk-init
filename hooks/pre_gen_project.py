import subprocess

app_name = '{{ cookiecutter.project_name}}'

subprocess.run(
    ['/home/ec2-user/.nvm/versions/node/v18.15.0/bin/cdk', 'init', '--language=python']
)
