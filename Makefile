all: unit cli

unit:
	bin/venv nosetests --verbose tests

cli:
	bin/venv python setup.py install --force &>/dev/null
	bin/venv tabutil col --extract=Teddy2,Teddy3 tests/data/tabutil.tsv
	bin/venv tabutil col --drop=Teddy2,Teddy3 tests/data/tabutil.tsv
	bin/venv tabutil col --rename=Teddy1:TeddyA,Teddy2:TeddyB --rename=Teddy3:TeddyC tests/data/tabutil.tsv
	bin/venv tabutil row --extract=GCL6 tests/data/tabutil.tsv
	bin/venv tabutil row --extract-match=Teddy2:apple tests/data/tabutil.tsv
	bin/venv tabutil row --drop=GCL6 tests/data/tabutil.tsv
	bin/venv tabutil row --rename=GLC6:FOO tests/data/tabutil.tsv

#	bin/venv tabutil row --delete=GCL6 tests/data/tabutil.tsv
#	bin/venv tabutil col --extract=Teddy2,Teddy3 tests/data/tabutil.tsv
