from lark import Lark, InlineTransformer
from pathlib import Path

class SExprTransformer(InlineTransformer):
    def funcao(self, *args):
      return ['funcao', *args]

    def lista(self, *args):
      return ['lista', *args]
    
    def tag(self,*args):
      return ['tag', *args]
    
    def atributo(self, *args):
      return ['atributo', *args]
    
    def nomedentro(self, x):
      return ['nomedentro' , str(x)]

    def nomefora(self, x):
      return ['nomefora' , str(x)]

def parse(src: str):
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
        grammar = Lark(fd, parser='lalr', transformer=SExprTransformer())
    return grammar

parser = _make_grammar()