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

def subcommand_col(args):
    if args.extract:
        column_names = flatten(args.extract)
        df = pd.read_csv(args.input_file, sep='\t', index_col=0)
        print(tabutil.core.extract_columns(df, *column_names))

    elif args.delete:
        column_names = flatten(args.delete)
        df = pd.read_csv(args.input_file, sep='\t', index_col=0)
        print(tabutil.core.remove_columns(df, *column_names))

    elif args.rename:
        rename_pair = flatten(args.rename)
        rename_pair =  [(p.split(':')[0], p.split(':')[1]) for p in rename_pair]
        df = pd.read_csv(args.input_file, sep='\t', index_col=0)
        print(tabutil.core.replace_column_headers(df, *rename_pair))

def subcommand_row(args):
    if args.extract:
        column_value_pair = flatten(args.extract)
        column_value_pair =  [(p.split(':')[0], p.split(':')[1]) for p in column_value_pair]
        df = pd.read_csv(args.input_file, sep='\t', index_col=0)
        print(tabutil.core.extract_rows(df, column_value_pair[0][0], column_value_pair[0][1]))

    elif args.delete:
        row_ids = flatten(args.delete)
        df = pd.read_csv(args.input_file, sep='\t', index_col=0)
        print(tabutil.core.remove_rows(df, *row_ids))

    elif args.rename:
        rename_pair = flatten(args.rename)
        rename_pair =  [(p.split(':')[0], p.split(':')[1]) for p in rename_pair]
        df = pd.read_csv(args.input_file, sep='\t', index_col=0)
        print(tabutil.core.replace_row_ids(df, *rename_pair))

def main():

    parser = argparse.ArgumentParser('tabutil')

    subparsers = parser.add_subparsers(help='sub-command help')

    #-----------------------------------------------------------------------------------------

    col_parser = subparsers.add_parser('col', help='col --help')
    col_parser.set_defaults(func=subcommand_col)

    col_parser.add_argument('--extract', type=custom_parser_comma, action='append',
                            metavar='COLUMN_NAME[,COLUMN_NAME]', dest='extract')

    col_parser.add_argument('--delete', type=custom_parser_comma, action='append',
                            metavar='COLUMN_NAME[,COLUMN_NAME]', dest='delete')

    col_parser.add_argument('--rename', type=custom_parser_comma, action='append',
                            metavar='COLUMN_NAME[,COLUMN_NAME]', dest='rename')

    col_parser.add_argument('input_file')

    #-----------------------------------------------------------------------------------------

    row_parser = subparsers.add_parser('row', help='row --help')
    row_parser.set_defaults(func=subcommand_row)

    row_parser.add_argument('--extract', type=custom_parser_comma, action='append',
                            metavar='COLUMN_NAME:VALUE', dest='extract')

    row_parser.add_argument('--delete', type=custom_parser_comma, action='append',
                            metavar='ROW_ID[,ROW_ID]', dest='delete')

    row_parser.add_argument('--rename', type=custom_parser_comma, action='append',
                            metavar='ROW_ID:NEW_ID[,ROW_ID:NEW_ID]', dest='rename')

    row_parser.add_argument('input_file')

    #-----------------------------------------------------------------------------------------

    args = parser.parse_args(sys.argv[1:])

    args.func(args)

