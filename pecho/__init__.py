# MIT License
#
# Copyright (c) 2019-2020 Nihaal Sangha
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from importlib.metadata import version as _version

import colorama

colorama.init()

__all__ = ['echo']
__version__ = _version('pecho')


def echo(*objects, newline=False, end='', pass_end=False, str_convert_func=str, print_func=print, **print_kwargs):
    if objects:
        objects = ('\r' + str_convert_func(objects[0]),) + objects[1:]
    else:
        objects = ('\r',)

    end += '\033[K'

    if newline:
        end += '\n'

    force_pass_end = print_func == print

    if pass_end is False or force_pass_end is True:
        objects = objects[:-1] + (str_convert_func(objects[-1]) + end,)
        end = ''  # Sets end for print()
    if pass_end is True or force_pass_end is True:
        print_kwargs['end'] = end

    return print_func(*objects, **print_kwargs)
