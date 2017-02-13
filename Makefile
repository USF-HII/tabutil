all: unit cli

install:
	bin/venv python setup.py install --force &>/dev/null

unit:
	bin/venv nosetests --verbose tests

cli: install
	@echo
	@echo "--------------------------------------------------------------------------------"
	head tests/data/tabutil.tsv | expand -t10
	@echo
	head tests/data/tabutil-b.tsv | expand -t10
	@echo
	head tests/data/tabutil-c.tsv | expand -t10
	@echo
	head tests/data/col-extract-spec.txt | expand -t10
	@echo
	@echo "--------------------------------------------------------------------------------"
	bin/venv tabutil col --extract --spec tests/data/col-extract-spec.txt tests/data/tabutil.tsv | expand -t10
	@echo
	@echo "--------------------------------------------------------------------------------"
	bin/venv tabutil col --extract=Teddy2,Teddy3 tests/data/tabutil.tsv | expand -t10
	@echo
	@echo "--------------------------------------------------------------------------------"
	bin/venv tabutil col --drop=Teddy2,Teddy3 tests/data/tabutil.tsv | expand -t10
	@echo
	@echo "--------------------------------------------------------------------------------"
	bin/venv tabutil col --rename=Teddy1:TeddyA,Teddy2:TeddyB --rename=Teddy3:TeddyC tests/data/tabutil.tsv | expand -t10
	@echo
	@echo "--------------------------------------------------------------------------------"
	bin/venv tabutil col --append=tests/data/tabutil-b.tsv tests/data/tabutil.tsv | expand -t10
	@echo
	@echo "--------------------------------------------------------------------------------"
	bin/venv tabutil row --extract=GCL6 tests/data/tabutil.tsv | expand -t10
	@echo
	@echo "--------------------------------------------------------------------------------"
	bin/venv tabutil row --extract-match=Teddy2:apple tests/data/tabutil.tsv | expand -t10
	@echo
	@echo "--------------------------------------------------------------------------------"
	bin/venv tabutil row --drop=GCL6 tests/data/tabutil.tsv | expand -t10
	@echo
	@echo "--------------------------------------------------------------------------------"
	bin/venv tabutil row --rename=GCL6:FOO tests/data/tabutil.tsv | expand -t10
	@echo
	@echo "--------------------------------------------------------------------------------"
	bin/venv tabutil row --append=tests/data/tabutil-c.tsv tests/data/tabutil.tsv | expand -t10
	@echo
	@echo "--------------------------------------------------------------------------------"
	bin/venv tabutil cell --replace=42:2000,apple:egglplant tests/data/tabutil.tsv | expand -t10
