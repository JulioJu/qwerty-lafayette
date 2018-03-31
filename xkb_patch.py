#!/usr/bin/env python3
import os
import sys

NAME = sys.argv[1]
MARK = NAME.upper()
XKB_SYMBOLS = '/usr/share/X11/xkb/symbols'
SED = "sed -i '/" + MARK + "::BEGIN/,/" + MARK + "::END/d' $xkb_symbols/"

# xkb_path = os.path.join(os.path.dirname(__file__),
#                         'dist/xkb/' + NAME + '_install.sh')
xkb_path = 'dist/xkb/' + NAME + '_install.sh'
xkb_out = open(xkb_path, 'w')
xkb_out.write('#!/bin/sh')
xkb_out.write('\nxkb_symbols=' + XKB_SYMBOLS)

for locale in next(os.walk('dist/xkb'))[1]:
    xkb_out.write('\n')
    xkb_out.write('\n' + SED + locale)
    xkb_out.write("\ncat << '" + MARK + "::END' >> $xkb_symbols/" + locale)
    xkb_out.write('\n// ' + MARK + '::BEGIN')
    xkb_out.write('\n')
    locale_path = os.path.join('dist/xkb/', locale)
    for variant in next(os.walk(locale_path))[2]:
        xkb_out.write('\n')
        with open(os.path.join(locale_path, variant)) as infile:
            for line in infile:
                if not line.startswith('// vim:'):
                    xkb_out.write(line)
    xkb_out.write('\n// ' + MARK + '::END')

os.chmod(xkb_path, 0o755)
print('... ' + xkb_path)
