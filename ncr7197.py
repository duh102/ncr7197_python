__CLEAR_PRINTER__ = b'\x10'
__FULL_KNIFE_CUT__ = b'\x19'
__PARTIAL_KNIFE_CUT__ = b'\x1A'
__BOLD_PREFIX__ = b'\x1b\x45\x01'
__BOLD_POSTFIX__ = b'\x1b\x45\x00'
__ITALIC_PREFIX__ = b'\x1b\x49\x01'
__ITALIC_POSTFIX__ = b'\x1b\x49\x00'
__SIZE_PREFIX__ = b'\x1d\x21'
__SIZES__ = [b'\x11', b'\x22', b'\x33']
__SIZE_POSTFIX__ = b'\x1d\x21\x00'
__MAKE_BEEP__ = b'\x1B\x07'
__INITIALIZE__ = b'\x1B\x40'
__SELECT_CUT_MODE_AND_CUT_PREFIX__ = b'\x1D\x56'
__PRINT_EVERYTHING_AND_PARTIAL_CUT__ = b'\x1d\x56\x41\x06'
__PRINT_TEST_FORM__ = b'\x1F\x74'
__PRINT_AND_NEWLINES_PREFIX__ = b'\x1B\x64'


# Available character heights
SIZE_DOUBLED = __SIZES__[0]
SIZE_TRIPLED = __SIZES__[1]
SIZE_QUADRUPLED = __SIZES__[2]

# The maximum number of characters on a line in standard mode on 80mm paper
MAX_WIDTH = 44
# The minimum number of lines that are needed between the last printed line and
#   the cut command to ensure all of your text is actually on the cut part of
#   the paper
# This leaves at least ~ 6 dots of whitespace at the bottom of the receipt, you
#   may want some more
PRINT_CUT_OFFSET = 6

class AnnotatedText(object):
    def __init__(self, text, bold=None, italics=None, size=None):
        prefix = bytes()
        postfix = bytes()
        if bold is None:
            bold = False
        if italics is None:
            italics = False
        if bold:
            prefix = __BOLD_PREFIX__
            postfix = __BOLD_POSTFIX__
        if italics:
            prefix += __ITALIC_PREFIX__
            postfix = __ITALIC_POSTFIX__ + postfix
        if size is not None:
            if size not in __SIZES__:
                raise Exception('Must use one of SIZE_DOUBLED, -TRIPLED, -QUADRUPLED')
            prefix += __SIZE_PREFIX__ + size
            postfix = __SIZE_POSTFIX__ + postfix

        self._text = prefix + bytes(text, 'ibm437') + postfix

    def __add__(self, other):
        self._text += other.get_text()
        return self

    def get_text(self):
        return self._text


class NCR7197(object):
    def __init__(self, device):
        self.__device = device;

    def print_test_form(self):
        with open(self.__device, 'wb') as out:
            out.write(__PRINT_TEST_FORM__)

    def print(self, text, newlines=None):
        if newlines is None:
            newlines = 1
        try:
            text = text.get_text()
            with open(self.__device, 'wb') as out:
                out.write(text + __PRINT_AND_NEWLINES_PREFIX__
                              + newlines.to_bytes(1,'big') )
        except AttributeError:
            lines = text.splitlines()
            with open(self.__device, 'wb') as out:
                for line in lines:
                    out.write(bytes(line+'\n', 'ibm437'))
                if newlines > 0:
                    out.write(__PRINT_AND_NEWLINES_PREFIX__
                              + newlines.to_bytes(1,'big'))

    def cut(self):
        with open(self.__device, 'wb') as out:
            out.write(__PRINT_EVERYTHING_AND_PARTIAL_CUT__)
