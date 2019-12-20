from lark import Lark, InlineTransformer, Tree, Token

grammar = Lark(r"""

?start : expr

?expr  : list

?list  : "f" "(" ( (namefora "," tag|tag|namefora) ("," atribute)* ("," func)? ) ")" -> lista


?atribute :  ( "$" namedentro ":" namedentro )  -> atributo

?func  : "{" list+ "}" -> funcao

?tag   :  "*" namedentro  -> tag

?namedentro  : STRINGDENTRO -> nomedentro

?namefora  : STRINGFORA -> nomefora
      
// Terminais
SYMBOL  : /[-!$%^&*()_+|~=`{}\[\]:";'<>?,.\/ ]/
STRINGDENTRO    : /[a-zA-Z0-9]+/
STRINGFORA    : /[a-zA-Z0-9 ]+/

%ignore /\s+/
%ignore /;[^\n]*/
""")

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

HTMLTAGS = ['p', 'pre','section','div', 'head','title',
            'html','article','aside','details','span',
            'small','footer', 'header','main', 'figure',
            'figcaption', 'h1', 'h2', 'iframe','style',
            'button','fieldset', 'label', 'legend',
            'h3', 'h4', 'h5', 'h6', 'span', 'applet',
            'big', 'center', 'dir',
            'head', 'footer', 'body', 'body','progress',
            'samp','summary','time','var',
            'abbr', 'blockquote', 'code', 
            'b', 'em', 'del', 'i', 'ins', 'mark',
            'p', 'sub', 'sup', 'u', 'textarea', 'canvas',
            'a', 'bdo', 'address', 'dialog']

CLOSEDHTMLTAGS = ['img', 'input', 'br', 'hr',
                  'wbr','meta','link', 'embed','basefont']

ATRIBUTO = [ 'accept', 'accept-charset', 'accesskey',
             'action', 'align', 'alt', 'async',
             'autocomplete', 'autofocus', 'autoplay',
             'bgcolor', 'border', 'buffered', 'challenge',
             'charset', 'checked', 'cite', 'class', 'code',
             'codebase', 'color', 'cols', 'colspan', 'content',
             'contenteditable', 'contextmenu', 'controls',
             'coords', 'data', 'datetime', 'default', 'defer',
             'dir', 'dirname', 'disabled', 'draggable', 'dropzone',
             'enctype', 'for', 'form', 'headers', 'height', 'hidden',
             'high', 'href', 'hreflang', 'http-equiv', 'icon', 'id', 
             'ismap', 'itemprop', 'keytype', 'kind', 'label', 'lang',
             'language', 'list', 'loop', 'low', 'manifest', 'max',
             'maxlength', 'media', 'method', 'min', 'multiple', 'name',
             'novalidate', 'open', 'optimum', 'pattern', 'ping',
             'placeholder', 'poster', 'preload', 'pubdate', 'radiogroup',
             'readonly', 'rel', 'required', 'reversed', 'rows', 'rowspan',
             'sandbox', 'spellcheck', 'scope', 'scoped', 'seamless',
             'selected', 'shape', 'size', 'sizes', 'span', 'src', 'srcdoc',
             'srclang', 'start', 'step', 'style', 'summary', 'target',
             'title', 'type', 'usemap', 'value', 'width', 'wrap']

def eval_sexpr(sexpr):
    for i in sexpr:
      if i[0] == 'tag':
        if i[1][1] not in HTMLTAGS and i[1][1] not in CLOSEDHTMLTAGS:
          print('Tag "{}" não encontrada'.format(i[1][1]))
          return 0
      if i[0] == 'atributo':
        if i[1][1] not in ATRIBUTO:
          print('Atributo "{}" não encontrado'.format(i[1][1]))
          return 0
      if i[0] == 'funcao':
        if eval_sexpr(i[1]) == 0:
          return 0 
    return 1

def eval_sexpr(sexpr):
    for i in sexpr:
      if i[0] == 'tag':
        if i[1][1] not in HTMLTAGS and i[1][1] not in CLOSEDHTMLTAGS:
          print('Tag "{}" não encontrada'.format(i[1][1]))
          return 0
      if i[0] == 'atributo':
        if i[1][1] not in ATRIBUTO:
          print('Atributo "{}" não encontrado'.format(i[1][1]))
          return 0
      if i[0] == 'funcao':
        if eval_sexpr(i[1]) == 0:
          return 0 
    return 1

# Manipulação de HTML
def createHtml(lista,fila,pilha):
    for i in lista:
      if i[0] == 'nomefora':
        fila.append('{} '.format(i[1]))
      if i[0] == 'tag':
        if i[1][1] in HTMLTAGS:
          fila.append('<{} '.format(i[1][1]))
          pilha.insert(0,'</{}>'.format(i[1][1]))
        elif i[1][1] in CLOSEDHTMLTAGS:
          fila.append('<{}'.format(i[1][1]))
      if i[0] == 'atributo':
        if i[1][1] in ATRIBUTO:
          fila.append('{}="{}" '.format(i[1][1], i[2][1]))
      if i == lista[-1] and lista[-1][0] != 'nomefora':
        fila.append('>')
      if i[0] == 'funcao':   
        createHtml(i[1],fila, pilha)

def retornaHtml(sexpr):
  fila = []
  pilha = []
  createHtml(sexpr,fila,pilha)
  resultado = ''.join(map(str,fila)) + ''.join(map(str,pilha))
  return resultado

########################################### Testes ############################################################

def test_one_tag():
  tree = grammar.parse('f(*div)')
  sexpr = SExprTransformer().transform(tree)
  assert retornaHtml(sexpr) == '<div ></div>'

  tree = grammar.parse('f(string fora, *div)')
  sexpr = SExprTransformer().transform(tree)
  assert retornaHtml(sexpr) == 'string fora <div ></div>'
  
  tree = grammar.parse('f(*p)')
  sexpr = SExprTransformer().transform(tree)
  assert retornaHtml(sexpr) == '<p ></p>'

  tree = grammar.parse('f(string fora, *span)')
  sexpr = SExprTransformer().transform(tree)
  assert retornaHtml(sexpr) == 'string fora <span ></span>'

  tree = grammar.parse('f(*img)')
  sexpr = SExprTransformer().transform(tree)
  assert retornaHtml(sexpr) == '<img>'

def test_inside_tag():

    tree = grammar.parse('f(*div, $class : teste ,{f(texto dentro da tag)})')
    sexpr = SExprTransformer().transform(tree)
    assert retornaHtml(sexpr) == '<div class="teste" >texto dentro da tag </div>'

    tree = grammar.parse('f(*span, $class : teste ,{f(texto dentro da tag)})')
    sexpr = SExprTransformer().transform(tree)
    assert retornaHtml(sexpr) == '<span class="teste" >texto dentro da tag </span>'

    tree = grammar.parse('f(*p, $class : paragraph ,{f(texto dentro da tag)})')
    sexpr = SExprTransformer().transform(tree)
    assert retornaHtml(sexpr) == '<p class="paragraph" >texto dentro da tag </p>'

    tree = grammar.parse('f(*div, $class : teste ,{f(texto dentro da tag)})')
    sexpr = SExprTransformer().transform(tree)
    assert retornaHtml(sexpr) == '<div class="teste" >texto dentro da tag </div>'

def test_multiple_tag_inside_tag():
    
    tree = grammar.parse('f(*div, $class : teste,{f(asdad,*p, $id: njsahd , {f(*div)})})')
    sexpr = SExprTransformer().transform(tree)
    assert retornaHtml(sexpr) == '<div class="teste" >asdad <p id="njsahd" ><div ></div></p></div>'

    tree = grammar.parse('f(string, *div, $class : nome, {f(string2, *h1, $color : blue)})')
    sexpr = SExprTransformer().transform(tree)
    assert retornaHtml(sexpr) == 'string <div class="nome" >string2 <h1 color="blue" ></h1></div>'

    tree = grammar.parse('f(string, *span, $class : nome, $id : number, {f(string2, *h1, $color : blue)})')
    sexpr = SExprTransformer().transform(tree)
    assert retornaHtml(sexpr) == 'string <span class="nome" id="number" >string2 <h1 color="blue" ></h1></span>'

    tree = grammar.parse('f(string, *div, $class : nome, {f(string2, *h1, $color : blue,{f(Texto dentro do h1)})})')
    sexpr = SExprTransformer().transform(tree)
    assert retornaHtml(sexpr) == 'string <div class="nome" >string2 <h1 color="blue" >Texto dentro do h1 </h1></div>'