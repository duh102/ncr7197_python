__CLEAR_PRINTER__ = b'\x10'
__FULL_KNIFE_CUT__ = b'\x19'
__PARTIAL_KNIFE_CUT__ = b'\x1A'
__MAKE_BEEP__ = b'\x1B\x07'
__INITIALIZE__ = b'\x1B\x40'
__SELECT_CUT_MODE_AND_CUT_PREFIX__ = b'\x1D\x56'
__PRINT_TEST_FORM__ = b'\x1F\x74'
__PRINT_AND_NEWLINES_PREFIX__ = b'\x1B\x64'

# The maximum number of characters on a line in standard mode on 80mm paper
MAX_WIDTH = 44
# The minimum number of lines that are needed between the last printed line and
#   the cut command to ensure all of your text is actually on the cut part of
#   the paper
# This leaves at least ~ 6 dots of whitespace at the bottom of the receipt, you
#   may want some more
PRINT_CUT_OFFSET = 6


class NCR7197(object):
    def __init__(self, device):
        self.__device = device;

    def print_test_form(self):
        with open(self.__device, 'wb') as out:
            out.write(__PRINT_TEST_FORM__)

    def print(self, text, newlines=None):
        if newlines is None:
            newlines = 1
        lines = text.splitlines()
        with open(self.__device, 'wb') as out:
            for line in lines:
                out.write(bytes(line+'\n', 'ascii'))
            if newlines > 0:
                out.write(__PRINT_AND_NEWLINES_PREFIX__
                          + newlines.to_bytes(1,'big'))

    def cut(self):
        with open(self.__device, 'wb') as out:
            out.write(__PARTIAL_KNIFE_CUT__)
