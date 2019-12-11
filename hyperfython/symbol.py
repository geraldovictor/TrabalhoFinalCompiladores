class Symbol:
    """
    representação de simbolos html

    Diferentemente de strings, símbolos com o mesmo valor possuem a mesma identidade.
    """

    data : str
    CACHE = {}

    def __new__(cls, data):
        if isinstance(data, Symbol):
            return data
        try:
            return cls.CACHE[data]
        except KeyError:
            cls.CACHE[data] = new = super().__new__(cls)
            new._data = data
            return new

    def __str__(self):
        return self._data

    def __repr__(self):
        return self._data

    def __hash__(self):
        return id(self._data)

    def __eq__(self, other):
        if isinstance(other, Symbol):
            return self._data == other._data
        return NotImplemented


# Formas especiais
Symbol.QUOTE = Symbol('quote')
Symbol.BEGIN = Symbol('fython')

# Funções úteis
Symbol.LIST = Symbol('list')
# Symbol.COLON = Symbol(':')

class _Var:
    def __getattr__(self, attr):
        return Symbol(attr)

    def __repr__(self):
        return 'var'

var = _Var()