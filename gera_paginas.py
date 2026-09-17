#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera TODAS as paginas do site.

    .venv/bin/python gera_paginas.py

De onde vem cada coisa:
  layout.py            cabecalho, menu, rodape e chat  (fonte unica)
  conteudo/*.html      o miolo de cada pagina fixa
  assets/modelos.js    os dados dos modelos            (fonte unica)

Nenhum HTML da raiz ou de /modelos se edita a mao — tudo aqui e sobrescrito.
"""
import json, re, os, sys
import layout

RAIZ = os.path.dirname(os.path.abspath(__file__))
CONT = os.path.join(RAIZ, 'conteudo')
DEST = os.path.join(RAIZ, 'modelos')


def miolo(nome):
    with open(os.path.join(CONT, nome), encoding='utf-8') as f:
        return f.read()


def escreve(caminho_rel, html):
    destino = os.path.join(RAIZ, caminho_rel)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, 'w', encoding='utf-8') as f:
        f.write(html)
    print('  gerado  %s' % caminho_rel)


# ------------------------------------------------------------ paginas fixas
# (arquivo, chave-no-menu, titulo, descricao, scripts extras, barra solida?)
FIXAS = [
    ('index.html', '', 'home',
     'Casa Nobre Piscinas — piscinas de fibra e alvenaria em Campo Largo',
     'Piscina de fibra e de alvenaria com projeto, instalação e entrega completa. '
     'Campo Largo, Curitiba e região.',
     ['home.js'], False),

    ('como-funciona.html', 'como-funciona', 'como-funciona',
     'Como funciona — Casa Nobre Piscinas',
     'Da visita técnica à entrega com a piscina cheia: as seis etapas da instalação, '
     'com escopo fechado e prazo definido.',
     [], True),

    ('sobre.html', 'sobre', 'sobre',
     'Sobre a Casa Nobre — Casa Nobre Piscinas',
     'Loja, projeto e obra no mesmo lugar. Representante autorizado GM Fibras, '
     'equipe própria de instalação em Campo Largo/PR.',
     [], True),

    ('contato.html', 'contato', 'contato',
     'Contato — Casa Nobre Piscinas',
     'Chat no site, telefone, e-mail e a loja física em Campo Largo/PR. '
     'Atendemos Curitiba e região metropolitana.',
     [], True),
]


def gera_fixas():
    for arquivo, atual, fonte, titulo, desc, scripts, solida in FIXAS:
        escreve(arquivo, layout.pagina(
            titulo, desc, miolo(fonte + '.html'),
            p='', atual=atual, solida=solida, scripts=scripts))


# ------------------------------------------------------------ lista de modelos
def gera_lista():
    escreve('modelos/index.html', layout.pagina(
        'Modelos de piscina — Casa Nobre Piscinas',
        'Modelos de piscina de fibra, alvenaria e spa. Medidas, prazo de instalação '
        'e detalhes técnicos de cada modelo.',
        miolo('modelos.html'),
        p='../', atual='modelos', solida=True,
        scripts=['modelos.js', 'lista.js']))


# ------------------------------------------------------------ detalhe do modelo
def le_modelos():
    bruto = open(os.path.join(RAIZ, 'assets', 'modelos.js'), encoding='utf-8').read()
    m = re.search(r'window\.MODELOS\s*=\s*(\[.*?\]);', bruto, re.S)
    if not m:
        sys.exit('ERRO: nao achei window.MODELOS em assets/modelos.js')
    corpo = m.group(1)
    corpo = re.sub(r'//.*', '', corpo)                      # tira comentarios
    corpo = re.sub(r'/\*.*?\*/', '', corpo, flags=re.S)
    corpo = re.sub(r'(\w+)\s*:', r'"\1":', corpo)           # chaves sem aspas
    corpo = corpo.replace('"', '"').replace("'", '"')
    corpo = re.sub(r',(\s*[}\]])', r'\1', corpo)            # virgula sobrando
    return json.loads(corpo)


def corpo_detalhe(mod, todos):
    galeria = mod.get('galeria') or [mod['foto']]
    minis = ''.join(
        '<div class="gmini%s" data-src="%s"><img loading="lazy" src="%s" alt=""></div>'
        % (' on' if i == 0 else '', u, u)
        for i, u in enumerate(galeria[:4]))
    opcs = ''.join('<span class="opc">%s</span>' % o for o in mod.get('opcionais', []))

    linhas = [
        ('Comprimento', mod['comprimento']), ('Largura', mod['largura']),
        ('Profundidade', mod['profundidade']), ('Área', mod['area']),
        ('Volume de água', mod['volume']), ('Borda', mod.get('borda', '—')),
    ]
    tec = ''.join('<div class="tlinha"><dt>%s</dt><dd>%s</dd></div>' % kv for kv in linhas)
    tec += ('<div class="tlinha destaque"><dt>Prazo de instalação</dt><dd>%s</dd></div>'
            '<div class="tlinha destaque"><dt>Garantia</dt><dd>%s</dd></div>'
            % (mod['prazo'], mod['garantia']))

    outros = [x for x in todos if x['slug'] != mod['slug']][:3]
    relac = ''.join('''
      <a class="mcard" href="%s.html">
        <div class="capa"><span class="etq">%s</span><img loading="lazy" src="%s" alt="%s"></div>
        <div class="corpo"><h3>%s</h3><div class="med">%s × %s</div></div>
      </a>''' % (o['slug'], o['etiqueta'], o['foto'], o['nome'],
                 o['nome'], o['comprimento'], o['largura']) for o in outros)

    return '''<section class="topo-pag" style="padding-bottom:34px">
  <div class="topo-in">
    <div class="migalha"><a href="../index.html">Início</a> › <a href="index.html">Modelos</a> › %s</div>
  </div>
</section>

<section class="det">
  <div class="galeria">
    <div class="gprinc"><img id="gfoto" src="%s" alt="%s"></div>
    <div class="gminis" id="gminis">%s</div>
  </div>

  <div class="ficha">
    <span class="etq-cat">%s</span>
    <h1>%s</h1>
    <p class="desc">%s</p>

    <div class="tec">
      <h4>Ficha técnica</h4>
      <dl>%s</dl>
    </div>

    <h4 class="rot-opc">Opcionais</h4>
    <div class="opcs">%s</div>

    <div class="cta-box">
      <h4>Quer esse modelo na sua casa?</h4>
      <p>Manda a medida do seu espaço que a gente confirma se cabe e passa o valor.</p>
      <a href="#" class="cta" data-chat>💬 Pedir orçamento</a>
    </div>
  </div>
</section>

<section class="relac">
  <div class="tit"><span class="cap">Veja também</span><h2>Outros <em>modelos</em></h2></div>
  <div class="grade" style="max-width:1240px">%s</div>
</section>''' % (mod['nome'], galeria[0], mod['nome'], minis, mod['etiqueta'],
                 mod['nome'], mod['resumo'], tec, opcs, relac)


def gera_detalhes(modelos):
    for mod in modelos:
        escreve('modelos/%s.html' % mod['slug'], layout.pagina(
            '%s — Casa Nobre Piscinas' % mod['nome'],
            mod['resumo'][:150],
            corpo_detalhe(mod, modelos),
            p='../', atual='modelos', solida=True,
            scripts=['detalhe.js']))


if __name__ == '__main__':
    os.makedirs(DEST, exist_ok=True)
    modelos = le_modelos()
    gera_fixas()
    gera_lista()
    gera_detalhes(modelos)
    print('\n%d páginas fixas + lista + %d modelos = %d páginas geradas.'
          % (len(FIXAS), len(modelos), len(FIXAS) + 1 + len(modelos)))
