import requests
from functools import singledispatch
import numbers
from collections import abc

@singledispatch
def search_book(text):
    print('Buscando livro com [str]')
    return 'str'

@search_book.register(numbers.Integral)
def _(n):
    print('Buscando livro com [números]')
    return 'number'


def _(seq):
    print('Buscando livro com [sequência]')
    return 'sequence'
    
search_book.register(abc.MutableSequence)(_)


