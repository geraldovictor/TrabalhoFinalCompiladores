"""
Hyperfython é um interpretador de linguagem html a fim de poder renderizar expressões em html
"""

from .parser import parse
from .runtime import eval_sexpr, env, global_env
from .htmltags import HTMLTAGS, CLOSEDHTMLTAGS , ATRIBUTO

__version__ = '0.1.0'