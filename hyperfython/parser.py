from lark import Lark, InlineTransformer
from pathlib import Path

from .runtime import Symbol


class HTMLTransformer(InlineTransformer):
    
    def start(self, *args): 
        return [Symbol.BEGIN, *args] # begin == "fython"
    
    def block(self, *args):
        return list(args) # args -> array de dict

    def pair(self, key, value):
        return (key, value)

    def dictionary(self, *args):
        return dict(args)

    def atom(self, token):
        try:
            return str(token)
        except ValueError:
            try:
                if token.type == 'SYMBOL':
                    return 'SYMBOL'
            except ValueError:
                if token.type == 'STRING':
                    return str(token[1:-1])

    
def parse(src: str):

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