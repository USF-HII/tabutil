# tabutil

## Synopsis

    tabutil col [OPTIONS] [--spec=spec_file] <file>

      OPTIONS:
        --append             <file>
        --drop               [column_name[,column_name...]]
        --extract            [column_name[,column_name...]]
        --rename             [column_name:new_name[,column_name:new_name...]]
        --show-duplicate     <file>
        --show-missing       <file>
        --show-unique        <file>

    tabutil row [OPTIONS] [--spec=spec_file] <file>

      OPTIONS:
        --append             <file>
        --drop               [row_id[,row_id...]]
        --extract            [row_id[,row_id...]]
        --extract-match      [column_name:value[,column_name:value...]]
        --rename             [row_id:new_id>[,<row_id:new_id>...]]
        --show-duplicate     <file>
        --show-missing       <file>
        --show-unique        <file>

    tabutil cell [OPTIONS] [--spec=spec_file] <input_file>

      OPTIONS:
        --replace            [value:new_value[,value:new_value...]]

## Specfile

For options specifying column names, row ids, matches, or replacement values a `spec_file` may be supplied with the `--spec` option
instead of providing arguments to the option, for example:

For `tabutil col --extract=foo,bar,baz`:

    foo
    bar
    baz

For `tabutil row --extract-match=apple:baker,charlie:delta,echo:foxtrot`:

    apple:baker
    charlie:delta
    echo:foxtrot

## Example Suite

```
--------------------------------------------------------------------------------
head tests/data/tabutil.tsv | expand -t10
ID        Teddy1    Teddy2    Teddy3
TXNIP     42        apple     29
GCL6      56        baker     99
GOS2      77        apple     100
INS       3         echo      54

head tests/data/tabutil-b.tsv | expand -t10
ID        Teddy4    Teddy5    Teddy6
TXNIP     70        grape     60
GCL6      30        orange    10
GOS2      50        zulu      90

head tests/data/tabutil-c.tsv | expand -t10
ID        Teddy4    Teddy5    Teddy6
XYZ       70        grape     60
ABC       30        orange    10
GEF       50        zulu      90

head tests/data/col-extract-spec.txt | expand -t10
Teddy1
Teddy2

--------------------------------------------------------------------------------
bin/venv tabutil col --extract --spec tests/data/col-extract-spec.txt tests/data/tabutil.tsv | expand -t10
ID        Teddy1    Teddy2
TXNIP     42        apple
GCL6      56        baker
GOS2      77        apple
INS       3         echo


--------------------------------------------------------------------------------
bin/venv tabutil col --extract=Teddy2,Teddy3 tests/data/tabutil.tsv | expand -t10
ID        Teddy2    Teddy3
TXNIP     apple     29
GCL6      baker     99
GOS2      apple     100
INS       echo      54


--------------------------------------------------------------------------------
bin/venv tabutil col --drop=Teddy2,Teddy3 tests/data/tabutil.tsv | expand -t10
ID        Teddy1
TXNIP     42
GCL6      56
GOS2      77
INS       3


--------------------------------------------------------------------------------
bin/venv tabutil col --rename=Teddy1:TeddyA,Teddy2:TeddyB --rename=Teddy3:TeddyC tests/data/tabutil.tsv | expand -t10
ID        Teddy1    Teddy2    Teddy3
TXNIP     42        apple     29
GCL6      56        baker     99
GOS2      77        apple     100
INS       3         echo      54


--------------------------------------------------------------------------------
bin/venv tabutil col --append=tests/data/tabutil-b.tsv tests/data/tabutil.tsv | expand -t10
ID        Teddy1    Teddy2    Teddy3    Teddy4    Teddy5    Teddy6
GCL6      56        baker     99        30        orange    10
GOS2      77        apple     100       50        zulu      90
INS       3         echo      54
TXNIP     42        apple     29        70        grape     60


--------------------------------------------------------------------------------
bin/venv tabutil row --extract=GCL6 tests/data/tabutil.tsv | expand -t10
ID        Teddy1    Teddy2    Teddy3
GCL6      56        baker     99


--------------------------------------------------------------------------------
bin/venv tabutil row --extract-match=Teddy2:apple tests/data/tabutil.tsv | expand -t10
ID        Teddy1    Teddy2    Teddy3
TXNIP     42        apple     29
GOS2      77        apple     100


--------------------------------------------------------------------------------
bin/venv tabutil row --drop=GCL6 tests/data/tabutil.tsv | expand -t10
ID        Teddy1    Teddy2    Teddy3
TXNIP     42        apple     29
GOS2      77        apple     100
INS       3         echo      54


--------------------------------------------------------------------------------
bin/venv tabutil row --rename=GCL6:FOO tests/data/tabutil.tsv | expand -t10
ID        Teddy1    Teddy2    Teddy3
TXNIP     42        apple     29
FOO       56        baker     99
GOS2      77        apple     100
INS       3         echo      54


--------------------------------------------------------------------------------
bin/venv tabutil row --append=tests/data/tabutil-c.tsv tests/data/tabutil.tsv | expand -t10
ID        Teddy1    Teddy2    Teddy3    Teddy4    Teddy5    Teddy6
ABC                                     30        orange    10
GCL6      56        baker     99
GEF                                     50        zulu      90
GOS2      77        apple     100
INS       3         echo      54
TXNIP     42        apple     29
XYZ                                     70        grape     60
```


