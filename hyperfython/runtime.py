from htmltags import HTMLTAGS, CLOSEDHTMLTAGS, ATRIBUTO

def eval_sexpr(sexpr):
    for i in sexpr:
      if i[0] == 'tag':
        if i[1][1] not in HTMLTAGS and i[1][1] not in CLOSEDHTMLTAGS:
          print('Tag "{}" não encontrada'.format(i[1][1]))
          return 0
      if i[0] == 'atributo':
        if i[1][1] not in ATRIBUTO:
          print('Atibuto "{}" não encontrado'.format(i[1][1]))
          return 0
      if i[0] == 'funcao':
        if eval_sexpr(i[1]) == 0:
          return 0 
    return 1



