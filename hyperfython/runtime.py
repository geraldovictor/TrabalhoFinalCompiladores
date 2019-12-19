from htmltags import HTMLTAGS, CLOSEDHTMLTAGS, ATRIBUTO

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
          out.append('<{}>'.format(i[1][1]))
      if i[0] == 'atributo':
        if i[1][1] in ATRIBUTO:
          fila.append('{}="{}" '.format(i[1][1], i[2][1]))
      if i[0] == 'funcao':
        fila.append('>')
        createHtml(i[1],fila, pilha)

def retornaHtml(sexpr):
  fila = []
  pilha = []
  createHtml(sexpr,fila,pilha)
  fila.append('>')
  return fila + pilha

