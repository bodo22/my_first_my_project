# Test files

- general stuff: `python hello.py`
- module stuff: `python module_example.py`
- File IO stuff: `python file_io.py`
- print current ip: `python myip.py`

# Virtual ENV (works on ubuntu 16 & with [my .zshrc](https://gist.github.com/bodo22/3dc5a08a5a9a5c259f93fb5e8ae5ed48))

based on [a very basic guide](https://medium.com/@rahul3012_37725/a-very-basic-guide-to-python-virtual-environments-a53d1e191490) and [the right way (allegedly)](https://medium.com/@rahul3012_37725/a-very-basic-guide-to-python-virtual-environments-a53d1e191490)

```
# install virtualenv, coz venv didnt work, maybe due to ubuntu16
pip install virtualenv

# create project folder
mkdir my_first_py_project && cd my_first_py_project

# create virtual env
python -m virtualenv venv

git init
echo 'venv' > .gitignore

# to activate
source venv/bin/activate
# -> venv name should be at start of prompt
# -> all installed packages will be installed in venv, e.g.
pip install camelcase

# confirm installation in venv
pip freeze
# should only show camelcase with version

# Move venv packages into requirements.txt (similar to package.json in node)
pip freeze > requirements.txt

# For fresh install other machine or other venv
pip install -r requirements.txt

# To include package in zip created, e.g. when executing on aws lamda
pip install -t . camelcase
# folder camelcase should exist now

# to deactivate venv
deactivate

```
