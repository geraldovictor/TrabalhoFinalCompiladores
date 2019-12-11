from hyperfython import var, env, Symbol, parse, eval, global_env

run = lambda src, env=None: eval(parse(src), env)
x, y, a, b, c, f, g, h, op = map(Symbol, 'x y a b c f g h op'.split())


class testHTMLGrammar:
    def test_one_tag(self):
        assert parse([
            {
                'div':
                {
                    'class':'text', 
                    'id': 'div-pai', 
                    'style': 
                    {
                        'color': 'red',
                        'font-size': '12px'
                    },
                    'content':
                    [
                        {'text': 'conteudo interno da tag'},
                        {'p': 
                            {
                                'content': 
                                [
                                    {'text': 'texto de uma tag p'}
                                ]
                            }
                        },
                    ],   
                }
            }
        ])


    def test_multiple_tag(self):
        assert parse(
            [
                {
                    'div': 
                    {
                        'class': 'row',
                        'id': 'row',
                        'content': 
                        [
                            {
                                'div': 
                                {
                                    'class': 'col md-6 lg-6',
                                    'content': 
                                    [
                                        {
                                            'p': 
                                            {
                                                'content': 
                                                [
                                                    {'text': 'Coluna 1'} 
                                                ]
                                            }
                                        }
                                    ]
                                }
                            },
                            {
                                'div': 
                                {
                                    'class': 'col md-6 lg-6',
                                    'content': 
                                    [
                                        {
                                            'p': 
                                            {
                                                'content': 
                                                [
                                                    {'text': 'Coluna 2'} 
                                                ]
                                            }
                                        }
                                    ]
                                }
                            },
                        ]
                    }
                }
            ]
        )

    def empty_tags(self):
        assert parse(
            [
                {
                    'div':{
                        'content':[
                            {
                                'div':{
                                    'content':[
                                        {
                                            'div':{}
                                        }
                                    ]
                                }   
                            }
                        ]
                    }
                }
            ]
        )

    def close_tags(self):
        assert parse(
        [
            {
                'head': {
                    'content': [
                        {
                            'p':{
                                'content': [{
                                    'text': "TITLE"
                                }]
                            },
                        },
                        {
                            'br': {}
                        }
                    ],
                    
                }
            },
            {
                'body': {
                    
                    'content': [
                        {
                            'p':{
                                'content': [
                                    {'text': "LINE 1"}
                                ]
                            }
                        },
                        {'br': {}},
                        {
                            'p':{
                                'content': [
                                    {'text': "LINE 2"}
                                ]
                            }
                        },
                    ],
                }        
            },
        ]
    )


# def write_data(*args):
#     for test in testHTMLGrammar


# with open('text.html', 'w') as file:
#     file.write(html)
