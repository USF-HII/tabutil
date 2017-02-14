all: unit cli

install:
	bin/venv python setup.py install --force &>/dev/null

unit:
	bin/venv nosetests --verbose tests

cli: install
	bin/cli-examples
