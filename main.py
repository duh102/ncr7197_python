#!/usr/bin/env python3
import ncr7197, argparse


if __name__ != '__main__':
    raise Exception('Must run as executable')

parser = argparse.ArgumentParser()
parser.add_argument('device', help='The device mountpoint of the printer; usually /dev/ttyUSB*')

args = parser.parse_args()

printer = ncr7197.NCR7197(args.device)
printer.print('Here\'s some text', 2)
printer.cut()
