#!/usr/bin/env python3.5

import argparse
import sys
import pandas as pd
import tabutil.core

#------------------------------------------------------------------------------------------------------
# Functions
#------------------------------------------------------------------------------------------------------
def flatten(alist):
    return [val for sublist in alist for val in sublist]

def custom_parser_comma(astring, separator=','):
    alist = astring.split(separator)
    alist = [a.strip() for a in alist if len(a)]
    return alist

def read_spec(filename):
    with open(filename) as f:
        return [str(line.rstrip()) for line in f]

def convert_separator(separator):
    if separator == '\\t':
        return '\t'
    elif separator == '\\n':
        return '\n'
    else:
        return separator

def csv_to_df(filename, sep='\t'):
    df = pd.read_csv(filename, sep=sep, dtype=str)
    df = df.set_index(df.columns[0])
    return df

def subcommand_col(args):
    input_separator = convert_separator(args.input_separator)
    output_separator = convert_separator(args.output_separator)
    df = csv_to_df(args.input_file, sep=input_separator)

    if args.append:
        df2 = csv_to_df(args.append, sep=input_separator)
        print(tabutil.core.column_append(df, df2, separator=output_separator))

    elif args.extract:
        if args.spec:
            column_names = read_spec(args.spec)
        else:
            column_names = flatten(args.extract)

        if args.with_index:
            print(tabutil.core.column_extract_with_index(df, column_names, separator=output_separator))
        else:
            print(tabutil.core.column_extract(df, column_names, separator=output_separator))

    elif args.drop:
        if args.spec:
            column_names = read_spec(args.spec)
        else:
            column_names = flatten(args.drop)

        print(tabutil.core.column_drop(df, column_names, separator=output_separator))

    elif args.rename:
        if args.spec:
            rename_pairs = read_spec(args.spec)
            arg_sep = '\t'
        else:
            rename_pairs = flatten(args.rename)
            arg_sep = ':'

        rename_pairs = [(p.split(arg_sep)[0], p.split(arg_sep)[1]) for p in rename_pairs]

        print(tabutil.core.column_rename(df, rename_pairs, separator=output_separator))

    elif args.sort:
        column_name = args.sort
        print(tabutil.core.column_sort(df, column_name, separator=output_separator))

    elif args.sort_numeric:
        column_name = args.sort_numeric
        print(tabutil.core.column_sort(df, column_name, numeric=True, separator=output_separator))

    elif args.set_intersect:
        df2 = csv_to_df(args.set_intersect, sep=input_separator)
        print('\n'.join(tabutil.core.set_intersect(df, df2, 'column')))

    elif args.set_union:
        df2 = csv_to_df(args.set_union, sep=input_separator)
        print('\n'.join(tabutil.core.set_union(df, df2, 'column')))

    elif args.set_diff:
        df2 = csv_to_df(args.set_diff, sep=input_separator)
        print('\n'.join(tabutil.core.set_diff(df, df2, 'column')))

    elif args.set_sym_diff:
        df2 = csv_to_df(args.set_sym_diff, sep=input_separator)
        print('\n'.join(tabutil.core.set_sym_diff(df, df2, 'column')))

def subcommand_row(args):
    input_separator = convert_separator(args.input_separator)
    output_separator = convert_separator(args.output_separator)
    df = csv_to_df(args.input_file, sep=input_separator)

    if args.extract:
        if args.spec:
            row_ids = read_spec(args.spec)
        else:
            row_ids = flatten(args.extract)

        print(tabutil.core.row_extract(df, row_ids, separator=output_separator))

    elif args.append:
        df2 = csv_to_df(args.append, sep=input_separator)
        print(tabutil.core.row_append(df, df2, separator=output_separator))

    elif args.extract_match:
        if args.spec:
            column_value_pair = read_spec(args.spec)
            arg_sep = '\t'
        else:
            column_value_pair = flatten(args.extract_match)
            arg_sep = ':'

        column_value_pair = [(p.split(arg_sep)[0], p.split(arg_sep)[1]) for p in column_value_pair]

        print(tabutil.core.row_extract_match(df, column_value_pair[0][0], column_value_pair[0][1], separator=output_separator))

    elif args.drop:
        if args.spec:
            row_ids = read_spec(args.spec)
        else:
            row_ids = flatten(args.drop)

        print(tabutil.core.row_drop(df, row_ids, separator=output_separator))

    elif args.drop_blank:
        print(tabutil.core.row_drop_blank(df, separator=output_separator))

    elif args.rename:
        if args.spec:
            rename_pairs = read_spec(args.spec)
            arg_sep = '\t'
        else:
            rename_pairs = flatten(args.rename)
            arg_sep = ':'

        rename_pairs = [(p.split(arg_sep)[0], p.split(arg_sep)[1]) for p in rename_pairs]

        print(tabutil.core.row_rename(df, rename_pairs, separator=output_separator))

    elif args.set_intersect:
        df2 = csv_to_df(args.set_intersect, sep=input_separator)
        print('\n'.join(tabutil.core.set_intersect(df, df2, 'row')))

    elif args.set_union:
        df2 = csv_to_df(args.set_union, sep=input_separator)
        print('\n'.join(tabutil.core.set_union(df, df2, 'row')))

    elif args.set_diff:
        df2 = csv_to_df(args.set_diff, sep=input_separator)
        print('\n'.join(tabutil.core.set_diff(df, df2, 'row')))

    elif args.set_sym_diff:
        df2 = csv_to_df(args.set_sym_diff, sep=input_separator)
        print('\n'.join(tabutil.core.set_sym_diff(df, df2, 'row')))

    elif args.sort:
        row_id = args.sort
        print(tabutil.core.row_sort(df, row_id, separator=output_separator))

    elif args.sort_numeric:
        row_id = args.sort_numeric
        print(tabutil.core.row_sort(df, row_id, numeric=True, separator=output_separator))

def subcommand_cell(args):
    input_separator = convert_separator(args.input_separator)
    output_separator = convert_separator(args.output_separator)
    df = csv_to_df(args.input_file, sep=input_separator)

    if args.replace:
        if args.spec:
            changesets = read_spec(args.spec)
            arg_sep = '\t'
        else:
            changesets = flatten(args.replace)
            arg_sep = ':'

        changesets = [(c.split(arg_sep)[0], c.split(arg_sep)[1]) for c in changesets]

        print(tabutil.core.cell_replace(df, changesets, separator=output_separator))

def main():
    parser = argparse.ArgumentParser('tabutil',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--input-separator', action='store', dest='input_separator', default='\t')
    parser.add_argument('--output-separator', action='store', dest='output_separator', default='\t')

    subparsers = parser.add_subparsers(help='sub-command help')
    subparsers.required = True

    #-----------------------------------------------------------------------------------------

    col = subparsers.add_parser('col', help='col --help')
    col.set_defaults(func=subcommand_col)

    col.add_argument('--append', action='store', metavar='FILE', dest='append')

    col.add_argument('--drop', type=custom_parser_comma, action='append',
                     metavar='COLUMN_NAME[,COLUMN_NAME...]', dest='drop', nargs='?', default=[])

    col.add_argument('--extract', type=custom_parser_comma, action='append',
                     metavar='COLUMN_NAME[,COLUMN_NAME]', dest='extract', nargs='?', default=[])

    col.add_argument('--rename', type=custom_parser_comma, action='append',
                     metavar='COLUMN_NAME[,COLUMN_NAME...]', dest='rename', nargs='?', default=[])

    col.add_argument('--set-intersect', action='store', metavar='FILE', dest='set_intersect')
    col.add_argument('--set-diff', action='store', metavar='FILE', dest='set_diff')
    col.add_argument('--set-sym-diff', action='store', metavar='FILE', dest='set_sym_diff')
    col.add_argument('--set-union', action='store', metavar='FILE', dest='set_union')

    col.add_argument('--sort', action='store', metavar='COLUMN_NAME', dest='sort')
    col.add_argument('--sort-numeric', action='store', metavar='COLUMN_NAME', dest='sort_numeric')

    col.add_argument('--spec', dest='spec')

    col.add_argument('--with-index', action='store_true', dest='with_index')

    col.add_argument('input_file')

    #-----------------------------------------------------------------------------------------

    row = subparsers.add_parser('row', help='row --help')
    row.set_defaults(func=subcommand_row)

    row.add_argument('--extract', type=custom_parser_comma, action='append',
                     metavar='ROW_ID[,ROW_ID...]', dest='extract', nargs='?', default=[])

    row.add_argument('--extract-match', type=custom_parser_comma, action='append',
                     metavar='COLUMN_NAME:VALUE[,COLUMN_NAME:VALUE...]', nargs='?', dest='extract_match', default=[])

    row.add_argument('--drop', type=custom_parser_comma, action='append',
                     metavar='ROW_ID[,ROW_ID...]', dest='drop', nargs='?', default=[])

    row.add_argument('--drop-blank', action='store_true', dest='drop_blank')

    row.add_argument('--rename', type=custom_parser_comma, action='append',
                     metavar='ROW_ID:NEW_ID[,ROW_ID:NEW_ID...]', dest='rename', nargs='?', default=[])

    row.add_argument('--append', action='store', metavar='FILE', dest='append')

    row.add_argument('--set-intersect', action='store', metavar='FILE', dest='set_intersect')
    row.add_argument('--set-diff', action='store', metavar='FILE', dest='set_diff')
    row.add_argument('--set-sym-diff', action='store', metavar='FILE', dest='set_sym_diff')
    row.add_argument('--set-union', action='store', metavar='FILE', dest='set_union')

    row.add_argument('--sort', action='store', metavar='ROW_ID', dest='sort')
    row.add_argument('--sort-numeric', action='store', metavar='ROW_ID', dest='sort_numeric')

    row.add_argument('--spec', dest='spec')

    row.add_argument('input_file')

    #-----------------------------------------------------------------------------------------

    cell = subparsers.add_parser('cell', help='cell --help')
    cell.set_defaults(func=subcommand_cell)

    cell.add_argument('--replace', type=custom_parser_comma, action='append',
                      metavar='OLD_VALUE:NEW_VALUE[,OLD_VALUE:NEW_VALUE...]', dest='replace', nargs='?', default=[])

    cell.add_argument('--spec', dest='spec')

    cell.add_argument('input_file')

    #-----------------------------------------------------------------------------------------

    if len(sys.argv) > 1:
        args = parser.parse_args(sys.argv[1:])
        args.func(args)
    else:
        parser.print_help()
        sys.exit(1)
