from hyperfython import var, env, Symbol, parse, eval, global_env

run = lambda src, env=None: eval(parse(src), env)
x, y, a, b, c, f, g, h, op = map(Symbol, 'x y a b c f g h op'.split())


class testHTMLGrammar:
    def test_one_tag(self):
        assert parse('fython (div)') == "<div ></div>"
        assert parse('fython (h1)') == "<h1 ></h1>"
        assert parse('fython (br)') == "<br >"


class TestHTMLGrammarHard:
    def test_tag_inside_tag(self):
        assert parse('fython [{ div:{class:text, id: div-pai, style:{color: red, font-size: 12px}, content:[{text: conteudo interno da tag},{p:{content:[{text: texto de uma tag p}]}}]}}]') == "<div  class= 'text'  id='div-pai' style= 'color': 'red'; 'font-size': '12px'; >conteudo interno da tag<p >texto de uma tag p</p></div>"

    def test_multiple_tag_inside_tag(self):
        assert parse('fython [{ div :{ class :  row , id :  row , content :[{ div :{ class :  col md-6 lg-6 , content :[{ p :{ content :[{ text :  Coluna 1 }]}}]}},{ div :{ class :  col md-6 lg-6 , content :[{ p :{ content :[{ text :  Coluna 2 }]}}]}},]}}]') == "<div  class='row'  id='row' ><div  class='col md-6 lg-6' ><p >Coluna 1</p></div><div  class='col md-6 lg-6' ><p >Coluna 2</p></div></div>"

    def empty_tags_inside_tag(self):
        assert parse('fython [{ div :{ content :[{ div :{ content :[{ div :{}}]}}]}}]') == "<div ><div ><div ></div></div></div>"

    def close_tags_empty_tag_inside_tag(self):
        assert parse('fython [{ head : { content : [{ p :{ content : [{ text :  TITLE }]},},{ br : {}}],}},{ body : { content : [{ p :{ content : [{ text :  LINE 1 }]}},{ br : {}},{ p :{ content : [{ text :  LINE 2 }]}},],}},]') == "<head ><p >TITLE</p><br ></head><body ><p >LINE 1</p><br ><p >LINE 2</p></body>"
