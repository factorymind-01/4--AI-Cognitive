#!/usr/bin/env python3
# Rênitton Scremin (UPinC)
# Abril de 2023
# Arquivo auxiliar: definição das perguntas inicializadas no soar.
# Arquivo auxiliar: definição dos trechos de inicialização do agente soar.

def trechos():

    initialize_intelligence_jug = """

    sp {intelligence-jug*apply*initialize-intelligence-jug
        (state <s> ^operator <o>)
        (<o> ^name initialize-intelligence-jug)
    -->
        (<s> ^name intelligence-jug ^jug <j1>
            ^jug <j2>) 
        (<j1> ^name intelligence-1
            ^volume 20
            ^contents 0
            ^question qual-é-a-sua-habilidade-de-escrita
            ^question você-gosta-de-ler
            ^question você-se-sente-confortável-falando-em-público
            ^question qual-a-sua-habilidade-de-criar-rimas-e-poemas
            ^question você-tem-facilidade-para-encontrar-palavras-e-expressões-adequadas-em-diferentes-situações
            ^question você-gosta-de-ler-livros,-artigos-e-jornais-regularmente
            ^question você-gosta-de-escrever-histórias-ensaios-ou-crônicas
            ^question com-que-frequência-você-usa-palavras-difícies-e-expressões-sofisticadas-em-suas-conversas
            ^question você-consegue-se-comunicar-bem-com-pessoas-de-culturas-e-línguas-diferentes
            ^question você-é-capaz-de-entender-e-usar-metáforas,-símbolos-e-outros-recursos-linguísticos-para-transmitir-ideias-e-emoções
            ) 
        (<j2> ^name intelligence-2
            ^volume 20
            ^contents 0
            ^question qual-é-a-sua-habilidade-em-resolução-de-problemas-matemáticos
            ^question você-gosta-de-jogos-de-lógica-e-raciocínio
            ^question você-se-sente-confortável-com-números-e-cálculos
            ^question você-gosta-de-resolver-problemas-matemáticos-e-lógicos
            ^question com-que-frequência-você-usa-a-lógica-e-o-raciocínio-para-solucionar-problemas-no-dia-a-dia
            ^question você-consegue-entender-rapidamente-relações-e-padrões-matemáticos-e-lógicos
            ^question você-gosta-de-jogos-de-estratégia-e-inteligência,-como-xadrez-e-sudoku
            ^question você-tem-facilidade-para-aprender-e-aplicar-conceitos-matemáticos
            ^question você-consegue-identificar-rapidamente-errors-em-cálculos-matemáticos-e-lógicos
            ^question você-gosta-de-experimentar-e-descobrir-novas-formas-de-resolver-problemas-matemáticos-e-lógicos
            )}
    """

    propose_initialize_intelligence_jug = """

    sp {intelligence-jug*propose*initialize-intelligence-jug
        (state <s> ^superstate nil)
    -(<s> ^name)
    -->
        (<s> ^operator <o> +)
        (<o> ^name initialize-intelligence-jug)}
    """

    propose_fill_intelligence_jug = """

    sp {intelligence-jug*propose*fill-intelligence-jug
        (state <s> ^name intelligence-jug
                ^jug <j>) 
        (<j> ^question <q>)
    -->
        (<s> ^operator <o> +) 
        (<o> ^name fill
            ^fill-jug <j>)}
    """

    apply_fill = """

    sp {intelligence-jug*apply*fill 
        (state <s> ^name intelligence-jug
                ^operator <o> ^jug <j>)
        (<o> ^name fill ^fill-jug <j>)
        (<j> ^volume <volume> ^contents <contents>)
    -->
        (<j> ^contents (+ <contents> <novo>))
        (<j> ^contents <contents> -)}
    """

    monitor_jugs = """

    sp {intelligence-jug*monitor*jugs 
        (state <s> ^name intelligence-jug
                ^jug <i> <j>)
        (<i> ^contents <icon>)
        (<j> ^contents <jcon>)
    -->
        (write (crlf) | j1:| <icon> | j2:| <jcon>)}
    """

    agent_raw = f"""
    # Initialization
    {initialize_intelligence_jug} # operador de init
    # Proposals
    {propose_initialize_intelligence_jug} # condição de init
    {propose_fill_intelligence_jug} # condição de preenchimento
    # Application
    {apply_fill} # preenchimento
    # Monitor
    {monitor_jugs}
    """

    return agent_raw


def li_perguntas():
    
    li_perguntas = [
        # Inteligência 1.
        {
            'pergunta':'qual-é-a-sua-habilidade-de-escrita',
            'resposta_a':'Excelente',
            'resposta_b':'Média',
            'resposta_c':'Fraca'
        },
        {'pergunta':'você-gosta-de-ler','resposta_a':'Sim','resposta_b':'Às vezes','resposta_c':'Não'},
        {'pergunta':'você-se-sente-confortável-falando-em-público','resposta_a':'Sim','resposta_b':'Às vezes','resposta_c':'Não'},
        {'pergunta':'qual-a-sua-habilidade-de-criar-rimas-e-poemas','resposta_a':'Excelente','resposta_b':'Média','resposta_c':'Fraca'},
        {'pergunta':'você-tem-facilidade-para-encontrar-palavras-e-expressões-adequadas-em-diferentes-situações','resposta_a':'Sim','resposta_b':'Às vezes','resposta_c':'Não'},
        {'pergunta':'você-gosta-de-ler-livros,-artigos-e-jornais-regularmente','resposta_a':'Sim','resposta_b':'Às vezes','resposta_c':'Não'},
        {'pergunta':'você-gosta-de-escrever-histórias-ensaios-ou-crônicas','resposta_a':'Sim','resposta_b':'Às vezes','resposta_c':'Não'},
        {'pergunta':'com-que-frequência-você-usa-palavras-difícies-e-expressões-sofisticadas-em-suas-conversas','resposta_a':'Com frequência','resposta_b':'Ocasionalmente','resposta_c':'Raramente'},
        {'pergunta':'você-consegue-se-comunicar-bem-com-pessoas-de-culturas-e-línguas-diferentes','resposta_a':'Sim','resposta_b':'Às vezes','resposta_c':'Não'},
        {'pergunta':'você-é-capaz-de-entender-e-usar-metáforas,-símbolos-e-outros-recursos-linguísticos-para-transmitir-ideias-e-emoções','resposta_a':'Sim','resposta_b':'Às vezes','resposta_c':'Não'},

        # Inteligência 2.
        {'pergunta':'qual-é-a-sua-habilidade-em-resolução-de-problemas-matemáticos','resposta_a':'Excelente','resposta_b':'Média','resposta_c':'Fraca'},
        {'pergunta':'você-gosta-de-jogos-de-lógica-e-raciocínio','resposta_a':'Sim','resposta_b':'Às vezes','resposta_c':'Não'},
        {'pergunta':'você-se-sente-confortável-com-números-e-cálculos','resposta_a':'Sim','resposta_b':'Às vezes','resposta_c':'Não'},
        {'pergunta':'você-gosta-de-resolver-problemas-matemáticos-e-lógicos','resposta_a':'Sim','resposta_b':'Às vezes','resposta_c':'Não'},
        {'pergunta':'com-que-frequência-você-usa-a-lógica-e-o-raciocínio-para-solucionar-problemas-no-dia-a-dia','resposta_a':'Com frequência','resposta_b':'Ocasionalmente','resposta_c':'Raramente'},
        {'pergunta':'você-consegue-entender-rapidamente-relações-e-padrões-matemáticos-e-lógicos','resposta_a':'Sim','resposta_b':'Às vezes','resposta_c':'Não'},
        {'pergunta':'você-gosta-de-jogos-de-estratégia-e-inteligência,-como-xadrez-e-sudoku','resposta_a':'Sim','resposta_b':'Às vezes','resposta_c':'Não'},
        {'pergunta':'você-tem-facilidade-para-aprender-e-aplicar-conceitos-matemáticos','resposta_a':'Sim','resposta_b':'Às vezes','resposta_c':'Não'},
        {'pergunta':'você-consegue-identificar-rapidamente-errors-em-cálculos-matemáticos-e-lógicos','resposta_a':'Sim','resposta_b':'Às vezes','resposta_c':'Não'},
        {'pergunta':'você-gosta-de-experimentar-e-descobrir-novas-formas-de-resolver-problemas-matemáticos-e-lógicos','resposta_a':'Sim','resposta_b':'Às vezes','resposta_c':'Não'},
    ]

    return li_perguntas
