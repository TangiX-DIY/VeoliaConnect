#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 11:01:40 2015

@author: tangix
"""

import argparse

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    '-l', '--login',
    help='your login on VeoliaEau website'
)
parser.add_argument(
    '-p', '--password',
    help='your password on VeoliaEau website'
)
parser.add_argument(
    '-s', '--spreadsheet',
    type=argparse.FileType('r'),
    help='use this spreadsheet insted of website one')
parser.add_argument(
    '-o', '--output',
    help='store the spreadsheet'
)
parser.add_argument(
    '-f', '--format',
    default='text',
    choices=['text', 'json', 'xml', 'none'],
    help='change output format'
)
args = parser.parse_args()
args.web = args.login is not None and args.password is not None
if not args.web and args.spreadsheet is None:
    parser.error('No action requested, add credentials or spreadsheet')
    
# WebSite gathering
if args.web:
    #TODO
    print 'TODO'

# Get external spreadsheet content
if args.spreadsheet is not None:
    #TODO
    print 'TODO'
    
# Store spreadsheet content
if args.output is not None:
    #TODO
    print 'TODO'
    
# Parse spreadsheet contents
if args.format != 'none':
    #TODO
    print 'TODO'


