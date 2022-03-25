"""
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
from os import popen, path

root = '/home/egsagon/.config/luminosity/'

if not path.exists(f'{root}gamma.txt'): open(f'{root}gamma.txt', 'w').write('1')

def set_lumi(value: float) -> None:
    open(f'{root}gamma.txt', 'w').write(str(value))
    popen(f'xgamma -gamma {value}')

app = gtk.Window()
app.resize(300, 100)
app.move(1680/2 - 300/2, 50)
app.set_title('LuminosityModule')

lumi = gtk.Scale()
lumi.set_range(0.7, 2.0)
lumi.set_draw_value(False)
lumi.set_value(float(open(f'{root}gamma.txt', 'r').read()))
lumi.connect('value-changed', lambda s: set_lumi(s.get_value()))

app.add(lumi)
app.connect('destroy', gtk.main_quit)
app.show_all()
gtk.main()