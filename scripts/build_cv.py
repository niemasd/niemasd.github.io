#! /usr/bin/env python3
'''
Build CV
'''

# imports
from pathlib import Path
from sys import argv
import argparse

# constants
pass # TODO

# parse user args
def parse_args():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input', required=False, type=str, default=Path(argv[0]).expanduser().parent.parent.resolve(), help="Root of GitHub Repository")
    parser.add_argument('-o', '--output', required=False, type=str, default='stdout', help="Output Markdown File")
    args = parser.parse_args()
    args.input = Path(args.input)
    if not args.input.is_dir():
        raise ValueError(f"Directory not found: {args.input}")
    if args.output not in {'stdout', 'stderr'}:
        args.output = Path(args.output)
        if args.output.exists():
            raise ValueError(f"Output exists: {args.output}")
    return args

# main logic
def main():
    args = parse_args()
    if isinstance(args.output, str):
        if args.output == 'stdout':
            from sys import stdout as out_f
        elif args.output == 'stderr':
            from sys import stderr as out_f
        else:
            raise ValueError(f"Invalid output: {args.output}")
    else:
        out_f = open(args.output, mode='wt')
    out_f.write("TODO\n") # TODO
    out_f.close()

# run script
if __name__ == '__main__':
    main()
