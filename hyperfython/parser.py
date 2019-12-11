from lark import Lark, InlineTransformer
from pathlib import Path

from .runtime import Symbol


class HTMLTransformer(InlineTransformer):
    
    def start(self, *args): 
        return [Symbol.BEGIN, *args]

    
def parse(src: int):
    """
    Compila string de entrada e retorna a S-expression equivalente.
    """
    return parser.parse(src)


def _make_grammar():
    """
    Retorna uma gramática do Lark inicializada.
    """

    path = Path(__file__).parent / 'grammar.lark'
    with open(path) as fd:
        grammar = Lark(fd, parser='lalr', transformer=HTMLTransformer())
    return grammar

parser = _make_grammar()