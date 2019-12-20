from parser import parse as parse_src
from runtime import eval_sexpr, retornaHtml, createHtml

while True:
    src = input('hyperfython >')
    sexpr = parse_src(src)
    if eval_sexpr(sexpr) == 1:
      value = retornaHtml(sexpr)
      print(value)



