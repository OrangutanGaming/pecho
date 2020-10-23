# MIT License
#
# Copyright (c) Nihaal Sangha
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

from typing import Any, Dict, List, Protocol, TypeVar, overload

__all__: List[str]

try:
    import importlib.metadata
except ImportError:
    __version__: None
else:
    __version__: str

_PrintFuncArg = TypeVar('_PrintFuncArg')
_PrintFuncReturn = TypeVar('_PrintFuncReturn')

class PrintFuncText(Protocol):
    def __call__(self, __text: _PrintFuncArg, *__args: Any, **__kwargs: Any) -> _PrintFuncReturn: ...

class PrintFuncObjects(Protocol):
    def __call__(self, *__objects: _PrintFuncArg, **__kwargs: Any) -> _PrintFuncReturn: ...

@overload
def echo(
    __text: _PrintFuncArg,
    newline: bool = ...,
    newline_char: str = ...,
    end: str = ...,
    print_func: PrintFuncText = ...,
    print_func_kwargs: Dict[str, Any] = ...,
) -> _PrintFuncReturn: ...
@overload
def echo(
    *objects: _PrintFuncArg,
    newline: bool = ...,
    newline_char: str = ...,
    end: str = ...,
    print_func_kwargs: Dict[str, Any] = ...,
) -> _PrintFuncReturn: ...
def echo(
    *objects: _PrintFuncArg,
    newline: bool = ...,
    newline_char: str = ...,
    end: str = ...,
    print_func: PrintFuncObjects = ...,
    print_func_kwargs: Dict[str, Any] = ...,
) -> _PrintFuncReturn: ...
