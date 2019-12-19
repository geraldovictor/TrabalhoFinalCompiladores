from htmltags import HTMLTAGS, CLOSEDHTMLTAGS, ATRIBUTO


def isTag(tag):
    for i in HTMLTAGS:
        if tag == i:
           return 1
    for i in CLOSEDHTMLTAGS:
        if tag == i:
           return 1
    return 0

def isAtrib(atributo):
  for i in ATRIBUTO:
    if atributo == i:
      return 1
  return 0

def eval_sexpr(sexpr):
    
    # Finalmente, deve ser uma S-expression. Separamos o primeiro termo
    # dos argumentos e avaliamos o resultado condicionalmente
    for i in sexpr:
      # if i[0] == 'lista':
      
      if i[0] == 'tag':
        if (isTag(i[1][1]) == 0):
          print('Tag -> {} não encontrada'.format(i[1][1]))

      if i[0] == 'atributo':
        if (isAtrib(i[1][1]) == 0):
           print('Atributo -> {} nao encontrado'.format(i[1][1]))
      
      # elif head == 'funcao':
        # passe para a proxima lista
