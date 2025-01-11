#!/usr/bin/env python3
import ncr7197, argparse, textwrap, sys
from ncr7197 import AnnotatedText


if __name__ != '__main__':
    raise Exception('Must run as executable')

def print_stdin(printer):
    txt = sys.stdin.read()
    if txt is None:
        print('Didn\'t read anything')
    else:
        for line in txt.splitlines():
            if len(line.strip()) == 0:
                printer.print('')
            else:
                for subline in textwrap.wrap(line, width=ncr7197.MAX_WIDTH):
                    printer.print(subline, newlines=0)
        printer.cut()

def demo(printer):
    printer.print('Here\'s some text', 2)
    printer.print(AnnotatedText('Have some text effects!\nSome ') + AnnotatedText('bolded', bold=True) + AnnotatedText(' text, some ') + AnnotatedText('italics', italics=True) + AnnotatedText('\nAnd now various text sizes:\n'))
    printer.print(AnnotatedText('2X Size', size=ncr7197.SIZE_DOUBLED))
    printer.print(AnnotatedText('3X Size', size=ncr7197.SIZE_TRIPLED))
    printer.print(AnnotatedText('4X Size', size=ncr7197.SIZE_QUADRUPLED))
    printer.cut()

parser = argparse.ArgumentParser(description='Without input, prints a demo receipt showing the capabilities of the library; if given stdin, will print the given text, wrapping to the width of the receipt')
parser.add_argument('device', help='The device mountpoint of the printer; usually /dev/ttyUSB*')

args = parser.parse_args()

printer = ncr7197.NCR7197(args.device)

# stdin has stuff
if not sys.stdin.isatty():
    print_stdin(printer)
else:
    demo(printer)
