import argparse
import sys

from fireshare.receiver import recvfile
from fireshare.sender import send

__version__ = '0.0.1'
parser = argparse.ArgumentParser(description="It is a file transfer app which uses ssh to transfer files")

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-r', '--receive', action='store_true')
group.add_argument('-s', '--send', action='store_true')
parser.add_argument('-f', '--file', type=str, help="Path of file to be sent", metavar="FILEPATH")

args = parser.parse_args()


def main():
    if args.receive:
        recvfile()
        sys.exit(0)

    elif args.send:
        if args.file is None:
            print("File path needed when using send")
            parser.print_help()
            sys.exit(0)
        send(args.file)