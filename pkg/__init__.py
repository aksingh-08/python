print(f'Invoking __init__.py for {__name__}')

A = ['quux', 'corge', 'grault']

# import pkg.mod1, pkg.mod2
from pkg.sub_pkg1 import *
from pkg.sub_pkg2 import *

__all__ = [
    'mod1',
    'mod2',
    'mod3',
    'mod4'
]