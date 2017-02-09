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

## Examples

All examples use the following tab-separated input file `test.tsv`:

    ID       Teddy1    Teddy2    Teddy3
    TXNIP    42        apple     29
    GCL6     56        baker     99
    GOS2     77        apple     100
    INS      3         echo      54

For the `col --append` option a second file `test-b.tsv` is:

    ID       Teddy4    Teddy5    Teddy6
    TXNIP    70        grape     60
    GCL6     30        orange    10
    GOS2     50        zulu      90

For the `row --append` option a second file `test-c.tsv` is:

    ID       Teddy4    Teddy5    Teddy6
    XYZ      70        grape     60
    ABC      30        orange    10
    GEF      50        zulu      90

### extract Columns

    tabutil col --extract=Teddy1,Teddy3 test.tsv

    ID        Teddy1   Teddy3
    TXNIP     42       29
    GCL6      56       99
    GOS2      77       100
    INS       3        54

### Remove Columns

    tabutil col --remove=Teddy1,Teddy3 test.tsv

    ID       Teddy2
    TXNIP    apple
    GCL6     baker
    GOS2     apple
    INS      echo

### Rename Column Headers

    tabutil col --rename=Teddy1:TeddyA,Teddy2:TeddyB test.tsv

    ID       TeddyA    TeddyB    Teddy3
    TXNIP    42        apple     29
    GCL6     56        baker     99
    GOS2     77        apple     100
    INS      3         echo      54


### extract Rows with Column Value

    tabutil row --extract=Teddy2:apple test.tsv

    ID       Teddy1    Teddy2    Teddy3
    TXNIP    42        apple     29
    GOS2     77        apple     100

### Remove Rows

    tabutil row --remove=GCL6,TXNIP test.tsv

    ID       Teddy1    Teddy2    Teddy3
    GOS2     77        apple     100
    INS      3         echo      54

### Rename Rows

    tabutil row --rename=TXNIP:FOO,GCL6:BOO test.tsv

    ID       Teddy1    Teddy2    Teddy3
    FOO      42        apple     29
    BOO      56        baker     99
    GOS2     77        apple     100
    INS      3         echo      54

### Append Columns

*Note: All column names in each file must be unique.*

    tabutil col --append=test-b.tsv test.tsv

    All examples use the following tab-separated input file `test.tsv`:

        ID       Teddy1    Teddy2    Teddy3  Teddy4    Teddy5    Teddy6
        TXNIP    42        apple     29      70        grape     60
        GCL6     56        baker     99      30        orange    10
        GOS2     77        apple     100     50        zulu      90
        INS      3         echo      54

### Append Rows

*Note: All row ids in each file must be unique.*

    tabutil row --append=test-c.tsv test.tsv

    ID       Teddy1    Teddy2    Teddy3   Teddy4    Teddy5    Teddy6
    TXNIP    42        apple     29
    GCL6     56        baker     99
    GOS2     77        apple     100
    INS      3         echo      54
    XYZ                                   70        grape     60
    ABC                                   30        orange    10
    GEF                                   50        zulu      90

