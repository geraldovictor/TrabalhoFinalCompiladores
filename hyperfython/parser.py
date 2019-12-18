from lark import Lark, InlineTransformer
from pathlib import Path

class HTMLTransformer(InlineTransformer):

    def funcao(self, *args):
      return ['funcao', *args]

    def lista(self, *args):
      return ['lista', *args]
    
    # def lista2(self, *args):
    #   return ['lista2', *args]
    
    # def lista3(self, *args):
    #   return ['lista3', *args]
    
    def tag(self,*args):
      return ['tag', *args]
    
    def atributo(self, *args):
      return ['atributo', *args]
    
    def nome(self, x):
      return str(x)

    
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