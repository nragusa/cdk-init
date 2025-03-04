# Overview

A very basic [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) template to initialize an AWS CDK application using ~~`pipenv`~~ ~~`poetry`~~ `uv` instead of `virtualenv`.

This assumes a function stored in `~/.zshrc` with something like the following:

```zsh
venv() {
    local venv_name="."

    # Check if .envrc already exists
    if [ -f .envrc ]; then
        echo "Error: .envrc already exists" >&2
        return 1
    fi

    # Initialize the virtual environment
    if ! uv init --python 3.13 --bare "$venv_name"; then
        echo "Error: Failed to initialize venv" >&2
        return 1
    fi
    # Create the virtual environment
    if ! uv venv --python 3.13; then
        echo "Error: Failed to create venv" >&2
        return 1
    fi

    # Create .envrc
    echo "layout python" > .envrc

    # Allow direnv to immediately activate the virtual environment
    direnv allow
}
```
