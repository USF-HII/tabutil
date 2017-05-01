all: unit install cli

install:
	bin/venv -- python setup.py install &>/dev/null

unit:
	bin/venv -- nosetests --verbose tests

cli: install
	bin/cli-examples

lint:
	bin/venv -- pylint --rcfile=.pylintrc --reports=no --output-format=parseable tabutil/*.py

