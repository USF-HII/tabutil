#!/usr/bin/env python27

import argparse
import os
import sys
import pprint as pp
import pandas as pd

import tabutil.core

#------------------------------------------------------------------------------------------------------
# Functions
#------------------------------------------------------------------------------------------------------
def flatten(alist):
    return([val for sublist in alist for val in sublist])

def custom_parser_comma(astring, separator=','):
    alist = astring.split(separator)
    alist = [a.strip() for a in alist if len(a)]
    return(alist)

def read_spec(filename):
    with open(filename) as f:
        return([line.rstrip() for line in f])

def subcommand_col(args):
    separator = '\t'
    df = pd.read_csv(args.input_file, sep=separator, index_col=0, dtype=str)

    if args.append:
        df2 = pd.read_csv(args.append, sep=separator, index_col=0, dtype=str)
        print(tabutil.core.column_append(df, df2))

    elif args.extract:
        if args.spec:
            column_names = read_spec(args.spec)
        else:
            column_names = flatten(args.extract)

        print(tabutil.core.column_extract(df, *column_names))

    elif args.drop:
        if args.spec:
            column_names = read_spec(args.spec)
        else:
            column_names = flatten(args.drop)

        print(tabutil.core.column_drop(df, *column_names))

    elif args.rename:
        if args.spec:
            rename_pairs = read_spec(args.spec)
        else:
            rename_pairs = flatten(args.rename)

        rename_pairs = [(p.split(':')[0], p.split(':')[1]) for p in rename_pairs]

        print(tabutil.core.column_rename(df, rename_pairs))

def subcommand_row(args):
    df = pd.read_csv(args.input_file, sep='\t', index_col=0, dtype=str)

    if args.extract:
        if args.spec:
            row_ids = read_spec(args.spec)
        else:
            row_ids = flatten(args.extract)

        print(tabutil.core.row_extract(df, *row_ids))

    elif args.append:
        df2 = pd.read_csv(args.append, sep='\t', index_col=0, dtype=str)
        print(tabutil.core.row_append(df, df2))

    elif args.extract_match:
        if args.spec:
            column_value_pair = read_spec(args.spec)
        else:
            column_value_pair = flatten(args.extract_match)

        column_value_pair =  [(p.split(':')[0], p.split(':')[1]) for p in column_value_pair]

        print(tabutil.core.row_extract_match(df, column_value_pair[0][0], column_value_pair[0][1]))

    elif args.drop:
        if args.spec:
            row_ids = read_spec(args.spec)
        else:
            row_ids = flatten(args.drop)

        print(tabutil.core.row_drop(df, *row_ids))

    elif args.rename:
        if args.spec:
            rename_pairs = read_spec(args.spec)
        else:
            rename_pairs = flatten(args.rename)

        rename_pairs = [(p.split(':')[0], p.split(':')[1]) for p in rename_pairs]
        print(tabutil.core.row_rename(df, rename_pairs))

    elif args.show_duplicate:
        df2 = pd.read_csv(args.show_duplicate, sep='\t', index_col=0, dtype=str)
        print(tabutil.core.show_duplicate(df, df2, 'row'))

    elif args.show_missing:
        df2 = pd.read_csv(args.show_missing, sep='\t', index_col=0, dtype=str)
        print(tabutil.core.show_missing(df, df2, 'row')

    elif args.show_unique:
        df2 = pd.read_csv(args.show_unique, sep='\t', index_col=0, dtype=str)
        print(tabutil.core.show_unique(df, df2, 'row'))

def subcommand_cell(args):
    df = pd.read_csv(args.input_file, sep='\t', index_col=0, dtype=str)

    if args.replace:
        if args.spec:
            changesets = read_spec(args.spec)
        else:
            changesets = flatten(args.replace)

        changesets = [(c.split(':')[0], c.split(':')[1]) for c in changesets]
        print(tabutil.core.cell_replace(df, changesets))


def main():

    parser = argparse.ArgumentParser('tabutil',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

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

    col.add_argument('--show-duplicate', action='store', metavar='FILE', dest='show_duplicate')
    col.add_argument('--show-missing', action='store', metavar='FILE', dest='show_missing')
    col.add_argument('--show-unique', action='store', metavar='FILE', dest='show_unique')

    col.add_argument('--spec', dest='spec')

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

    row.add_argument('--rename', type=custom_parser_comma, action='append',
                                 metavar='ROW_ID:NEW_ID[,ROW_ID:NEW_ID...]', dest='rename', nargs='?', default=[])

    row.add_argument('--append', action='store', metavar='FILE', dest='append')

    row.add_argument('--show-duplicate', action='store', metavar='FILE', dest='show_duplicate')
    row.add_argument('--show-missing', action='store', metavar='FILE', dest='show_missing')
    row.add_argument('--show-unique', action='store', metavar='FILE', dest='show_unique')

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

