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
    df = pd.read_csv(args.input_file, sep=separator, index_col=0)
    df.applymap(str)

    if args.extract:
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
            rename_pair = read_spec(args.spec)
        else:
            rename_pair = flatten(args.rename)

        rename_pair = [(p.split(':')[0], p.split(':')[1]) for p in rename_pair]

        print(tabutil.core.column_rename(df, *rename_pair))

def subcommand_row(args):
    df = pd.read_csv(args.input_file, sep='\t', index_col=0)
    df.applymap(str)

    if args.extract:
        if args.spec:
            row_ids = read_spec(args.spec)
        else:
            row_ids = flatten(args.extract)

        print(tabutil.core.row_extract(df, *row_ids))

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
            rename_pair = read_spec(args.spec)
        else:
            rename_pair = flatten(args.rename)

        rename_pair =  [(p.split(':')[0], p.split(':')[1]) for p in rename_pair]
        print(tabutil.core.row_rename(df, *rename_pair))

def main():

    parser = argparse.ArgumentParser('tabutil',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    subparsers = parser.add_subparsers(help='sub-command help')

    #-----------------------------------------------------------------------------------------

    col = subparsers.add_parser('col', help='col --help')
    col.set_defaults(func=subcommand_col)

    col.add_argument('--extract', type=custom_parser_comma, action='append',
                                  metavar='COLUMN_NAME[,COLUMN_NAME]', dest='extract')

    col.add_argument('--drop', type=custom_parser_comma, action='append',
                               metavar='COLUMN_NAME[,COLUMN_NAME...]', dest='drop')

    col.add_argument('--rename', type=custom_parser_comma, action='append',
                                 metavar='COLUMN_NAME[,COLUMN_NAME...]', dest='rename')

    col.add_argument('--spec', dest='spec')

    col.add_argument('input_file')

    #-----------------------------------------------------------------------------------------

    row = subparsers.add_parser('row', help='row --help')
    row.set_defaults(func=subcommand_row)

    row.add_argument('--extract', type=custom_parser_comma, action='append',
                                  metavar='ROW_ID[,ROW_ID...]', dest='extract')

    row.add_argument('--extract-match', type=custom_parser_comma, action='append',
                                        metavar='COLUMN_NAME:VALUE[,COLUMN_NAME:VALUE...]', dest='extract_match')

    row.add_argument('--drop', type=custom_parser_comma, action='append',
                               metavar='ROW_ID[,ROW_ID...]', dest='drop')

    row.add_argument('--rename', type=custom_parser_comma, action='append',
                                 metavar='ROW_ID:NEW_ID[,ROW_ID:NEW_ID...]', dest='rename')

    row.add_argument('--spec', dest='spec')

    row.add_argument('input_file')

    #-----------------------------------------------------------------------------------------

    args = parser.parse_args(sys.argv[1:])

    args.func(args)

