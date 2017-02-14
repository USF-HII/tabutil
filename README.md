# tabutil

## Synopsis

    tabutil col [OPTIONS] [--spec=spec_file] <file>

      OPTIONS:
        --append             <file>
        --drop               [column_name[,column_name...]]
        --extract            [column_name[,column_name...]]
        --rename             [column_name:new_name[,column_name:new_name...]]
        --set-diff           <file>
        --set-intersect      <file>
        --set-sym-diff       <file>
        --set-union          <file>

    tabutil row [OPTIONS] [--spec=spec_file] <file>

      OPTIONS:
        --append             <file>
        --drop               [row_id[,row_id...]]
        --extract            [row_id[,row_id...]]
        --extract-match      [column_name:value[,column_name:value...]]
        --rename             [row_id:new_id>[,<row_id:new_id>...]]
        --set-diff           <file>
        --set-intersect      <file>
        --set-sym-diff       <file>
        --set-union          <file>

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

## CLI Examples

Run with `:.!bin/cli-examples`:

```
```
