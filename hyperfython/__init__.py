"""
Hyperfython é um interpretador de linguagem html a fim de poder renderizar expressões em html
"""

from .symbol import Symbol, var
from .parser import parse
from .runtime import eval, env, global_env

__version__ = '0.1.0'