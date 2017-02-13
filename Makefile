all: unit cli

install:
	bin/venv python setup.py install --force &>/dev/null

unit:
	bin/venv nosetests --verbose tests

cli: install
	@echo
	@echo "--------------------------------------------------------------------------------"
	head tests/data/tabutil.tsv | column -s '\t' -t
	@echo
	head tests/data/tabutil-b.tsv | column -s '\t' -t
	@echo
	head tests/data/tabutil-c.tsv | column -s '\t' -t
	@echo
	head tests/data/col-extract-spec.txt | column -s '\t' -t
	@echo
	@echo "--------------------------------------------------------------------------------"
	bin/venv tabutil col --extract --spec tests/data/col-extract-spec.txt tests/data/tabutil.tsv | column -s '\t' -t
	@echo
	@echo "--------------------------------------------------------------------------------"
	bin/venv tabutil col --extract=Teddy2,Teddy3 tests/data/tabutil.tsv | column -s '\t' -t
	@echo
	@echo "--------------------------------------------------------------------------------"
	bin/venv tabutil col --drop=Teddy2,Teddy3 tests/data/tabutil.tsv | column -s '\t' -t
	@echo
	@echo "--------------------------------------------------------------------------------"
	bin/venv tabutil col --rename=Teddy1:TeddyA,Teddy2:TeddyB --rename=Teddy3:TeddyC tests/data/tabutil.tsv | column -s '\t' -t
	@echo
	@echo "--------------------------------------------------------------------------------"
	bin/venv tabutil col --append=tests/data/tabutil-b.tsv tests/data/tabutil.tsv | column -s '\t' -t
	@echo
	@echo "--------------------------------------------------------------------------------"
	bin/venv tabutil row --extract=GCL6 tests/data/tabutil.tsv | column -s '\t' -t
	@echo
	@echo "--------------------------------------------------------------------------------"
	bin/venv tabutil row --extract-match=Teddy2:apple tests/data/tabutil.tsv | column -s '\t' -t
	@echo
	@echo "--------------------------------------------------------------------------------"
	bin/venv tabutil row --drop=GCL6 tests/data/tabutil.tsv | column -s '\t' -t
	@echo
	@echo "--------------------------------------------------------------------------------"
	bin/venv tabutil row --rename=GCL6:FOO tests/data/tabutil.tsv | column -s '\t' -t
	@echo
	@echo "--------------------------------------------------------------------------------"
	bin/venv tabutil row --append=tests/data/tabutil-c.tsv tests/data/tabutil.tsv | column -s '\t' -t
