# tabutil

## Synopsis

    tabutil col --extract=column_name[,column_name]|--extract-spec=<spec_file> <input_file>

    tabutil col --delete=column_name[,column_name...]|--delete-spec=<spec_file> <input_file>

    tabutil col --rename=<column_name:new_name>[,column_name:new_name]|--rename-spec=<spec_file> <input_file>

    tabutil row --extract=column_name:value[,column_name:value]|--extract-spec=<spec_file> <input_file>

    tabutil row --delete=row_id[,row_id]|--delete-spec=<spec_file> <input_file>

    tabutil row --rename=<row_id:new_id>[,<row_id:new_id>]|--rename-spec=<spec_file> <input_file>

## Specfile

For operations with many column names, row ids, rename pairs, or column/value extraction pairs a `spec_file` may be specified instead of an option.

For `tabutil col --extract=foo,baz`:

    foo
    baz

For `tabutil row --extract=apple:baker,charlie:delta`:

    apple:baker
    charlie:delta

## Example Suite


```
--------------------------------------------------------------------------------
head tests/data/tabutil.tsv
ID	Teddy1	Teddy2	Teddy3
TXNIP	42	apple	29
GCL6	56	baker	99
GOS2	77	apple	100
INS	3	echo	54
head tests/data/tabutil-b.tsv
ID	Teddy4	Teddy5	Teddy6
TXNIP	70	grape	60
GCL6	30	orange	10
GOS2	50	zulu	90
head tests/data/col-extract-spec.txt
Teddy1
Teddy2

--------------------------------------------------------------------------------
bin/venv tabutil col --extract=Teddy2,Teddy3 tests/data/tabutil.tsv
ID	Teddy2	Teddy3
TXNIP	apple	29
GCL6	baker	99
GOS2	apple	100
INS	echo	54


--------------------------------------------------------------------------------
bin/venv tabutil col --extract --spec tests/data/col-extract-spec.txt tests/data/tabutil.tsv
ID	Teddy1	Teddy2
TXNIP	42	apple
GCL6	56	baker
GOS2	77	apple
INS	3	echo


--------------------------------------------------------------------------------
bin/venv tabutil col --drop=Teddy2,Teddy3 tests/data/tabutil.tsv
ID	Teddy1
TXNIP	42
GCL6	56
GOS2	77
INS	3


--------------------------------------------------------------------------------
bin/venv tabutil col --rename=Teddy1:TeddyA,Teddy2:TeddyB --rename=Teddy3:TeddyC tests/data/tabutil.tsv
ID	Teddy1	Teddy2	Teddy3
TXNIP	42	apple	29
GCL6	56	baker	99
GOS2	77	apple	100
INS	3	echo	54


--------------------------------------------------------------------------------
bin/venv tabutil col --append=tests/data/tabutil-b.tsv tests/data/tabutil.tsv
ID	Teddy1	Teddy2	Teddy3	Teddy4	Teddy5	Teddy6
GCL6	56	baker	99	30	orange	10
GOS2	77	apple	100	50	zulu	90
INS	3	echo	54
TXNIP	42	apple	29	70	grape	60


--------------------------------------------------------------------------------
bin/venv tabutil row --extract=GCL6 tests/data/tabutil.tsv
ID	Teddy1	Teddy2	Teddy3
GCL6	56	baker	99


--------------------------------------------------------------------------------
bin/venv tabutil row --extract-match=Teddy2:apple tests/data/tabutil.tsv
ID	Teddy1	Teddy2	Teddy3
TXNIP	42	apple	29
GOS2	77	apple	100


--------------------------------------------------------------------------------
bin/venv tabutil row --drop=GCL6 tests/data/tabutil.tsv
ID	Teddy1	Teddy2	Teddy3
TXNIP	42	apple	29
GOS2	77	apple	100
INS	3	echo	54


--------------------------------------------------------------------------------
bin/venv tabutil row --rename=GCL6:FOO tests/data/tabutil.tsv
ID	Teddy1	Teddy2	Teddy3
TXNIP	42	apple	29
FOO	56	baker	99
GOS2	77	apple	100
INS	3	echo	54

```
bin/venv nosetests --verbose tests
bin/venv python setup.py install --force &>/dev/null

--------------------------------------------------------------------------------
head tests/data/tabutil.tsv
ID	Teddy1	Teddy2	Teddy3
TXNIP	42	apple	29
GCL6	56	baker	99
GOS2	77	apple	100
INS	3	echo	54
head tests/data/tabutil-b.tsv
ID	Teddy4	Teddy5	Teddy6
TXNIP	70	grape	60
GCL6	30	orange	10
GOS2	50	zulu	90
head tests/data/col-extract-spec.txt
Teddy1
Teddy2

--------------------------------------------------------------------------------
bin/venv tabutil col --extract --spec tests/data/col-extract-spec.txt tests/data/tabutil.tsv
ID	Teddy1	Teddy2
TXNIP	42	apple
GCL6	56	baker
GOS2	77	apple
INS	3	echo


--------------------------------------------------------------------------------
bin/venv tabutil col --extract=Teddy2,Teddy3 tests/data/tabutil.tsv
ID	Teddy2	Teddy3
TXNIP	apple	29
GCL6	baker	99
GOS2	apple	100
INS	echo	54


--------------------------------------------------------------------------------
bin/venv tabutil col --drop=Teddy2,Teddy3 tests/data/tabutil.tsv
ID	Teddy1
TXNIP	42
GCL6	56
GOS2	77
INS	3


--------------------------------------------------------------------------------
bin/venv tabutil col --rename=Teddy1:TeddyA,Teddy2:TeddyB --rename=Teddy3:TeddyC tests/data/tabutil.tsv
ID	Teddy1	Teddy2	Teddy3
TXNIP	42	apple	29
GCL6	56	baker	99
GOS2	77	apple	100
INS	3	echo	54


--------------------------------------------------------------------------------
bin/venv tabutil col --append=tests/data/tabutil-b.tsv tests/data/tabutil.tsv
ID	Teddy1	Teddy2	Teddy3	Teddy4	Teddy5	Teddy6
GCL6	56	baker	99	30	orange	10
GOS2	77	apple	100	50	zulu	90
INS	3	echo	54			
TXNIP	42	apple	29	70	grape	60


--------------------------------------------------------------------------------
bin/venv tabutil row --extract=GCL6 tests/data/tabutil.tsv
ID	Teddy1	Teddy2	Teddy3
GCL6	56	baker	99


--------------------------------------------------------------------------------
bin/venv tabutil row --extract-match=Teddy2:apple tests/data/tabutil.tsv
ID	Teddy1	Teddy2	Teddy3
TXNIP	42	apple	29
GOS2	77	apple	100


--------------------------------------------------------------------------------
bin/venv tabutil row --drop=GCL6 tests/data/tabutil.tsv
ID	Teddy1	Teddy2	Teddy3
TXNIP	42	apple	29
GOS2	77	apple	100
INS	3	echo	54


--------------------------------------------------------------------------------
bin/venv tabutil row --rename=GCL6:FOO tests/data/tabutil.tsv
ID	Teddy1	Teddy2	Teddy3
TXNIP	42	apple	29
FOO	56	baker	99
GOS2	77	apple	100
INS	3	echo	54


--------------------------------------------------------------------------------
bin/venv tabutil row --append=tests/data/tabutil-c.tsv tests/data/tabutil.tsv
ID	Teddy1	Teddy2	Teddy3	Teddy4	Teddy5	Teddy6
ABC				30	orange	10
GCL6	56	baker	99			
GEF				50	zulu	90
GOS2	77	apple	100			
INS	3	echo	54			
TXNIP	42	apple	29			
XYZ				70	grape	60

