# tabutil

## Synopsis

    tabutil [--input-separator=<separator>]
            [--output-separator=<separator>]
            <col|row|cell> [options]

---

    tabutil col [options] [--spec=<spec_file>] <file>

      OPTIONS:
        --append             <file>
        --drop               [<column_name>[,<column_name>...]]
        --extract            [<column_name>[,<column_name>...]]
        --rename             [<column_name>:<new_name>[,<column_name>:<new_name>...]]
        --set-diff           <file>
        --set-intersect      <file>
        --set-sym-diff       <file>
        --set-union          <file>
        --sort               <column_name>
        --sort-numeric       <column_name>
        --with-index         (Changes --extract option to include row index)
---

    tabutil row [options] [--spec=<spec_file>] <file>

      OPTIONS:
        --append             <file>
        --drop               [<row_id>[,<row_id>...]]
        --drop-blank
        --extract            [<row_id>[,<row_id>...]]
        --extract-match      [<column_name>:<value>[,<column_name>:<value>...]]
        --rename             [row_id:new_id>[,<row_id:new_id>...]]
        --set-diff           <file>
        --set-intersect      <file>
        --set-sym-diff       <file>
        --set-union          <file>
        --sort               <row_id>
        --sort-numeric       <row_id>

---

    tabutil cell [options] [--spec=<spec_file>] <file>

      OPTIONS:
        --replace            [<value>:<new_value>[,<value>:<new_value>...]]

## Option Explanations

tabutil col:

    - `--extract [<column_name[,<column_name>...]]` - Extracts columns only. To print row index add `--with-index` option.

tabutil row:

    - `--drop-blank` - drop any row with a blank value in any of its columns

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

## CLI Examples

Run with `:.!bin/cli-examples` from vim:


    --------------------------------------------------------------------------------
    head tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    ID      Teddy1      Teddy2      Teddy3
    TXNIP   42          apple       29
    GCL6    56          baker       99
    GOS2    77          apple       100
    INS     3           echo        54

    --------------------------------------------------------------------------------
    head tests/data/tabutil-b.tsv
    --------------------------------------------------------------------------------
    ID      Teddy4      Teddy5      Teddy6
    TXNIP   70          grape       60
    GCL6    30          orange      10
    GOS2    50          zulu        90

    --------------------------------------------------------------------------------
    head tests/data/tabutil-c.tsv
    --------------------------------------------------------------------------------
    ID      Teddy4      Teddy5      Teddy6
    XYZ     70          grape       60
    ABC     30          orange      10
    GEF     50          zulu        90

    --------------------------------------------------------------------------------
    head tests/data/col-extract-spec.txt
    --------------------------------------------------------------------------------
    Teddy1
    Teddy2

    ================================================================================


    --------------------------------------------------------------------------------
    bin/venv tabutil col --append=tests/data/tabutil-b.tsv tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    ID      Teddy1      Teddy2      Teddy3      Teddy4      Teddy5      Teddy6
    GCL6    56          baker       99          30          orange      10
    GOS2    77          apple       100         50          zulu        90
    INS     3           echo        54
    TXNIP   42          apple       29          70          grape       60


    --------------------------------------------------------------------------------
    bin/venv tabutil col --drop=Teddy2,Teddy3 tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    ID      Teddy1
    TXNIP   42
    GCL6    56
    GOS2    77
    INS     3


    --------------------------------------------------------------------------------
    bin/venv tabutil col --drop --spec=/dev/fd/63 tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    ID      Teddy1
    TXNIP   42
    GCL6    56
    GOS2    77
    INS     3


    --------------------------------------------------------------------------------
    bin/venv tabutil col --extract=Teddy2,Teddy3 tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    Teddy2  Teddy3
    apple   29
    baker   99
    apple   100
    echo    54


    --------------------------------------------------------------------------------
    bin/venv tabutil col --extract --spec=/dev/fd/63 tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    Teddy2  Teddy3
    apple   29
    baker   99
    apple   100
    echo    54


    --------------------------------------------------------------------------------
    bin/venv tabutil col --extract=Teddy2,Teddy3 --with-index tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    ID      Teddy2      Teddy3
    TXNIP   apple       29
    GCL6    baker       99
    GOS2    apple       100
    INS     echo        54


    --------------------------------------------------------------------------------
    bin/venv tabutil col --rename=Teddy1:TeddyA,Teddy2:TeddyB --rename=Teddy3:TeddyC tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    ID      TeddyA      TeddyB      TeddyC
    TXNIP   42          apple       29
    GCL6    56          baker       99
    GOS2    77          apple       100
    INS     3           echo        54


    --------------------------------------------------------------------------------
    bin/venv tabutil col --rename --spec=/dev/fd/63 tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    ID      TeddyA      TeddyB      TeddyC
    TXNIP   42          apple       29
    GCL6    56          baker       99
    GOS2    77          apple       100
    INS     3           echo        54


    --------------------------------------------------------------------------------
    bin/venv tabutil col --set-diff=tests/data/tabutil-b.tsv tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    Teddy1
    Teddy2
    Teddy3

    --------------------------------------------------------------------------------
    bin/venv tabutil col --set-intersect=tests/data/tabutil-b.tsv tests/data/tabutil.tsv
    --------------------------------------------------------------------------------


    --------------------------------------------------------------------------------
    bin/venv tabutil col --set-sym-diff=tests/data/tabutil-b.tsv tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    Teddy1
    Teddy2
    Teddy3
    Teddy4
    Teddy5
    Teddy6

    --------------------------------------------------------------------------------
    bin/venv tabutil col --set-union=tests/data/tabutil-b.tsv tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    Teddy1
    Teddy2
    Teddy3
    Teddy4
    Teddy5
    Teddy6

    --------------------------------------------------------------------------------
    bin/venv tabutil col --sort=Teddy2 tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    ID      Teddy1      Teddy2      Teddy3
    TXNIP   42          apple       29
    GOS2    77          apple       100
    GCL6    56          baker       99
    INS     3           echo        54


    --------------------------------------------------------------------------------
    bin/venv tabutil col --sort-numeric=Teddy3 tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    ID      Teddy1      Teddy2      Teddy3
    TXNIP   42          apple       29
    INS     3           echo        54
    GCL6    56          baker       99
    GOS2    77          apple       100


    --------------------------------------------------------------------------------
    bin/venv tabutil row --append=tests/data/tabutil-c.tsv tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    ID      Teddy1      Teddy2      Teddy3      Teddy4      Teddy5      Teddy6
    ABC                                         30          orange      10
    GCL6    56          baker       99
    GEF                                         50          zulu        90
    GOS2    77          apple       100
    INS     3           echo        54
    TXNIP   42          apple       29
    XYZ                                         70          grape       60


    --------------------------------------------------------------------------------
    bin/venv tabutil row --drop=GCL6 tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    ID      Teddy1      Teddy2      Teddy3
    TXNIP   42          apple       29
    GOS2    77          apple       100
    INS     3           echo        54


    --------------------------------------------------------------------------------
    bin/venv tabutil row --drop --spec=/dev/fd/63 tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    ID      Teddy1      Teddy2      Teddy3
    TXNIP   42          apple       29
    GOS2    77          apple       100
    INS     3           echo        54


    --------------------------------------------------------------------------------
    bin/venv tabutil row --drop-blank tests/data/tabutil-d.tsv
    --------------------------------------------------------------------------------
    ID      Teddy1      Teddy2      Teddy3
    GCL6    56          baker       99
    INS     3           echo        54


    --------------------------------------------------------------------------------
    bin/venv tabutil row --extract-match=Teddy2:apple tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    ID      Teddy1      Teddy2      Teddy3
    TXNIP   42          apple       29
    GOS2    77          apple       100


    --------------------------------------------------------------------------------
    bin/venv tabutil row --extract-match --spec=/dev/fd/63 tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    ID      Teddy1      Teddy2      Teddy3
    TXNIP   42          apple       29
    GOS2    77          apple       100


    --------------------------------------------------------------------------------
    bin/venv tabutil row --extract=GCL6 tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    ID      Teddy1      Teddy2      Teddy3
    GCL6    56          baker       99


    --------------------------------------------------------------------------------
    bin/venv tabutil row --extract --spec=/dev/fd/63 tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    ID      Teddy1      Teddy2      Teddy3
    GCL6    56          baker       99


    --------------------------------------------------------------------------------
    bin/venv tabutil row --rename=GCL6:FOO tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    ID      Teddy1      Teddy2      Teddy3
    TXNIP   42          apple       29
    FOO     56          baker       99
    GOS2    77          apple       100
    INS     3           echo        54


    --------------------------------------------------------------------------------
    bin/venv tabutil row --rename --spec=/dev/fd/63 tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    ID      Teddy1      Teddy2      Teddy3
    TXNIP   42          apple       29
    FOO     56          baker       99
    GOS2    77          apple       100
    INS     3           echo        54


    --------------------------------------------------------------------------------
    bin/venv tabutil row --sort=TXNIP tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    ID      Teddy3      Teddy1      Teddy2
    TXNIP   29          42          apple
    GCL6    99          56          baker
    GOS2    100         77          apple
    INS     54          3           echo


    --------------------------------------------------------------------------------
    bin/venv tabutil row --sort-numeric=TXNIP tests/data/tabutil-e.tsv
    --------------------------------------------------------------------------------
    ID      Teddy2      Teddy3      Teddy1
    TXNIP   9           97          100
    INS     echo        54          3


    --------------------------------------------------------------------------------
    bin/venv tabutil row --set-diff=tests/data/tabutil-b.tsv tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    INS

    --------------------------------------------------------------------------------
    bin/venv tabutil row --set-intersect=tests/data/tabutil-b.tsv tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    GCL6
    GOS2
    TXNIP

    --------------------------------------------------------------------------------
    bin/venv tabutil row --set-sym-diff=tests/data/tabutil-b.tsv tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    INS

    --------------------------------------------------------------------------------
    bin/venv tabutil row --set-union=tests/data/tabutil-b.tsv tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    GCL6
    GOS2
    INS
    TXNIP

    --------------------------------------------------------------------------------
    bin/venv tabutil cell --replace=42:2000,apple:egglplant tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    ID      Teddy1      Teddy2      Teddy3
    TXNIP   2000        egglplant   29
    GCL6    56          baker       99
    GOS2    77          egglplant   100
    INS     3           echo        54


    --------------------------------------------------------------------------------
    bin/venv tabutil cell --replace --spec=/dev/fd/63 tests/data/tabutil.tsv
    --------------------------------------------------------------------------------
    ID      Teddy1      Teddy2      Teddy3
    TXNIP   2000        egglplant   29
    GCL6    56          baker       99
    GOS2    77          egglplant   100
    INS     3           echo        54

