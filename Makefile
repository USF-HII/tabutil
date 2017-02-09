all:
	bin/venv nosetests --verbose tests

#	bin/tabutil col --extract=Teddy2,Teddy3 data/tabutil.tsv
#	bin/tabutil col --delete=Teddy2,Teddy3 data/tabutil.tsv
#	bin/tabutil col --rename=Teddy1:TeddyA,Teddy2:TeddyB --rename=Teddy3:TeddyC data/tabutil.tsv
#	bin/tabutil row --extract=Teddy2:apple data/tabutil.tsv
#	bin/tabutil row --delete=Teddy2,Teddy3 data/tabutil.tsv
#	bin/tabutil row --rename=GC06:FOO data/tabutil.tsv
