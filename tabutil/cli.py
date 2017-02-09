#!/usr/bin/env python27

import argparse
import os
import sys
import pprint as pp
import pandas as pd

import tabutil


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
        print('extract: {}'.format(column_names))
        df = pd.read_csv(args.input_file, sep='\t', index_col=0)

    elif args.delete:
        column_names = flatten(args.delete)
        print('delete: {}'.format(column_names))

    elif args.rename:
        rename_pair = flatten(args.rename)
        print('rename: {}'.format(rename_pair))

def subcommand_row(args):
    if args.extract:
        column_value_pair = flatten(args.extract)
        print('extract: {}'.format(column_value_pair))

    elif args.delete:
        column_names = flatten(args.delete)
        print('delete: {}'.format(column_names))

    elif args.rename:
        rename_pair = flatten(args.rename)
        print('rename: {}'.format(rename_pair))

#------------------------------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------------------------------

parser = argparse.ArgumentParser('tabutil')

subparsers = parser.add_subparsers(help='sub-command help')

#------------------------------------------------------------------------------------------------------

col_parser = subparsers.add_parser('col', help='col -h')
col_parser.set_defaults(func=subcommand_col)

col_parser.add_argument('-e', '--extract', type=custom_parser_comma, action='append',
                        metavar='COLUMN_NAME[,COLUMN_NAME]', dest='extract')

col_parser.add_argument('-d', '--delete', type=custom_parser_comma, action='append',
                        metavar='COLUMN_NAME[,COLUMN_NAME]', dest='delete')

col_parser.add_argument('-r', '--rename', type=custom_parser_comma, action='append',
                        metavar='COLUMN_NAME[,COLUMN_NAME]', dest='rename')

col_parser.add_argument('input_file')

#------------------------------------------------------------------------------------------------------

row_parser = subparsers.add_parser('row', help='row -h')
row_parser.set_defaults(func=subcommand_row)

row_parser.add_argument('-e', '--extract', type=custom_parser_comma, action='append',
                        metavar='COLUMN_NAME:VALUE', dest='extract')

row_parser.add_argument('-d', '--delete', type=custom_parser_comma, action='append',
                        metavar='ROW_ID[,ROW_ID]', dest='delete')

row_parser.add_argument('-r', '--rename', type=custom_parser_comma, action='append',
                        metavar='ROW_ID:NEW_ID[,ROW_ID:NEW_ID]', dest='rename')

row_parser.add_argument('input_file')

#------------------------------------------------------------------------------------------------------

args = parser.parse_args(sys.argv[1:])

args.func(args)

