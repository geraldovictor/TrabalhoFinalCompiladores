from collections import OrderedDict

HTMLTAGS = ['p', 'div', 'small', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span', 'head', 'footer', 'main', 'body']
CLOSEDHTMLTAGS = ['img', 'input', 'br']


def eval(htmlObj):

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


## 1 - Aceitar mais de uma tag inicial
## 2 - Permitir que o content aceite mais de uma entrada para a mesma tag (fazer uma lista de objetos) 

# <div  class="text"  id="div-pai" style=" color:red; font-size:12px; ">conteudo interno da tag<p >texto de uma tag p</p></div>
# <div  class="row"  id="row" ><div  class="col md-6 lg-6" ><p >Coluna 1</p></div><div  class="col md-6 lg-6" ><p >Coluna 2</p></div></div>
# <div ><div ><div ></div></div></div>
# <head ><p >TITLE</p><br ></head><body ><p >LINE 1</p><br ><p >LINE 2</p></body>
# Traceback (most recent call last):
#   File "render.py", line 214, in <module>
#     {'text': 'abcd'}]
#   File "render.py", line 57, in new_eval
#     for attribute, attribute_value in values.items():
# AttributeError: 'list' object has no attribute 'items'
# <p >abcd</p>



