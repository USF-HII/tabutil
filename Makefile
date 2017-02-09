all:
	bin/venv nosetests --verbose tests

install:
	bin/venv python setup.py build &>/dev/null
	bin/venv python setup.py install &>/dev/null

cli: install
	bin/venv tabutil row --rename=GCL6:FOO tests/data/tabutil.tsv

cli2: install
	bin/venv tabutil row --extract=Teddy2:apple tests/data/tabutil.tsv
	bin/venv tabutil col --delete=Teddy2,Teddy3 tests/data/tabutil.tsv
	bin/venv tabutil row --delete=GCL6 tests/data/tabutil.tsv
	bin/venv tabutil col --rename=Teddy1:TeddyA,Teddy2:TeddyB --rename=Teddy3:TeddyC tests/data/tabutil.tsv
	bin/venv tabutil col --extract=Teddy2,Teddy3 tests/data/tabutil.tsv
