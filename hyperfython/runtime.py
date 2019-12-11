import math
import operator as op
from collections import ChainMap
from types import MappingProxyType

from .symbol import Symbol

HTMLTAGS = ['p', 'div', 'small', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span', 'head', 'footer', 'main', 'body']
CLOSEDHTMLTAGS = ['img', 'input', 'br']

def eval(htmlObj, env=None):

    if env is None:
        env = ChainMap({}, global_env)

    html = ""
    for initalTag in htmlObj:
        
        for tag, values in initalTag.items():

            # values is a dict
            parsed_attributes = ""
            parsed_content = ""
            try: 
                for attribute, attribute_value in values.items():

                    if attribute == 'content':
                        for obj in  attribute_value:
                            for inner_attr, innter_attr_value in obj.items():
                                if inner_attr == 'text':
                                    parsed_content += innter_attr_value
                                else:
                                    parsed_content += eval(
                                        [{inner_attr: innter_attr_value}, ]
                                    )
                    elif attribute == 'style':
                        classList = []
                        for classes, elements in attribute_value.items():
                            classList.append(f'{classes}:{elements};')
                        
                        parsed_attributes += f'{attribute}=" {" ".join(classList)} "'
                    else:
                        parsed_attributes += f' {attribute}="{attribute_value}" '
                
                if tag in HTMLTAGS:
                    html += f"<{tag} {parsed_attributes}>{parsed_content}</{tag}>"
                elif tag in CLOSEDHTMLTAGS:
                    html += f"<{tag} {parsed_attributes}>"
                else:
                    raise Exception(f"Syntax Error: tag {tag} not recognized")

            except AttributeError:
                raise AttributeError('Expected a dict, got a list')
    return html


#
# Cria ambiente de execução.
#
def env(*args, **kwargs):
    """
    Retorna um ambiente de execução que pode ser aproveitado pela função
    eval().

    Aceita um dicionário como argumento posicional opcional. Argumentos nomeados
    são salvos como atribuições de variáveis.

    Ambiente padrão
    >>> env()
    {...}
        
    Acrescenta algumas variáveis explicitamente
    >>> env(x=1, y=2)
    {x: 1, y: 2, ...}
        
    Passa um dicionário com variáveis adicionais
    >>> d = {Symbol('x'): 1, Symbol('y'): 2}
    >>> env(d)
    {x: 1, y: 2, ...}
    """

    kwargs = {Symbol(k): v for k, v in kwargs.items()}
    if len(args) > 1:
        raise TypeError('accepts zero or one positional arguments')
    elif len(args):
        if any(not isinstance(x, Symbol) for x in args[0]):
            raise ValueError('keys in a environment must be Symbols')
        args[0].update(kwargs)
        return ChainMap(args[0], global_env)
    return ChainMap(kwargs, global_env)


def _make_global_env():
    """
    Retorna dicionário fechado para escrita relacionando o nome das variáveis aos
    respectivos valores.
    """

    dic = {
        **vars(math), # sin, cos, sqrt, pi, ...
        '+':op.add, '-':op.sub, '*':op.mul, '/':op.truediv, 
        '>':op.gt, '<':op.lt, '>=':op.ge, '<=':op.le, '=':op.eq, 
        'abs':     abs,
        'append':  op.add,  
        'apply':   lambda proc, args: proc(*args),
        'begin':   lambda *x: x[-1],
        'car':     lambda x: head,
        'cdr':     lambda x: x[1:], 
        'cons':    lambda x,y: [x] + y,
        'eq?':     op.is_, 
        'expt':    pow,
        'equal?':  op.eq,
        'even?':   lambda x: x % 2 == 0,
        'length':  len, 
        'list':    lambda *x: list(x), 
        'list?':   lambda x: isinstance(x, list), 
        'map':     map,
        'max':     max,
        'min':     min,
        'not':     op.not_,
        'null?':   lambda x: x == [], 
        'number?': lambda x: isinstance(x, (float, int)),  
		'odd?':   lambda x: x % 2 == 1,
        'print':   print,
        'procedure?': callable,
        'quotient': op.floordiv,
        'round':   round,
        'symbol?': lambda x: isinstance(x, Symbol),
    }
    return MappingProxyType({Symbol(k): v for k, v in dic.items()})

global_env = _make_global_env() 

