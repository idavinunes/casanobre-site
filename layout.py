# -*- coding: utf-8 -*-
"""
Casca compartilhada de TODAS as paginas do site.

Cabecalho, menu, rodape e chat moram aqui e em nenhum outro lugar.
Mudou o menu? Muda so aqui e roda `gera_paginas.py` — todas as paginas
nascem de novo ja com a mudanca.
"""

# ---------------------------------------------------------------- menu
# (chave, rotulo, caminho a partir da raiz do site)
NAV = [
    ('modelos',       'Modelos',       'modelos/index.html'),
    ('como-funciona', 'Como funciona', 'como-funciona.html'),
    ('sobre',         'Sobre',         'sobre.html'),
    ('contato',       'Contato',       'contato.html'),
]

AVISO = ('⚠️ Modelo de apresentação — fotos, vídeo e números são <b>placeholder</b>. '
         'Logo reconstruído (falta o vetor original).')

# Uma familia so no site inteiro: Outfit no corpo E nos titulos (peso 200 nos
# titulos grandes). Fraunces saiu em 2026-09-16 por decisao do Davi.
FONTES = ('https://fonts.googleapis.com/css2?'
          'family=Outfit:wght@200;300;400;500;600;700;800&display=swap')

LOGO = '''<svg class="logo-neg" viewBox="0 0 320 80">
      <text x="0" y="46" font-family="Outfit,sans-serif" font-size="43" font-weight="800" fill="#fff" letter-spacing="-1">CASA</text>
      <text x="122" y="46" font-family="Outfit,sans-serif" font-size="43" font-weight="300" fill="#fff" letter-spacing="1">NOBRE</text>
      <path d="M10 52 q20 -12 40 0 t40 0" stroke="#6F96CE" stroke-width="5.5" fill="none" stroke-linecap="round"/>
      <text x="180" y="68" font-family="Outfit,sans-serif" font-size="13" font-weight="600" fill="rgba(255,255,255,.9)" letter-spacing="6">PISCINAS</text>
    </svg>
    <svg class="logo-cor" viewBox="0 0 320 80">
      <text x="0" y="46" font-family="Outfit,sans-serif" font-size="43" font-weight="800" fill="#212A53" letter-spacing="-1">CASA</text>
      <text x="122" y="46" font-family="Outfit,sans-serif" font-size="43" font-weight="300" fill="#33509E" letter-spacing="1">NOBRE</text>
      <path d="M10 52 q20 -12 40 0 t40 0" stroke="#6F96CE" stroke-width="5.5" fill="none" stroke-linecap="round"/>
      <text x="180" y="68" font-family="Outfit,sans-serif" font-size="13" font-weight="600" fill="#6F96CE" letter-spacing="6">PISCINAS</text>
    </svg>'''

ENDERECO = ('Av. Ayrton Senna da Silva, 3000<br>Jd. Busmayer — Campo Largo/PR<br>CEP 83606-390')
TELEFONE = '(41) 3393-2590'
TEL_LINK = '+554133932590'
EMAIL    = 'contato@casanobrestore.com.br'
INSTA    = 'casanobrestore'


def cabecalho(atual, p, solida):
    """p = prefixo ate a raiz ('' na raiz, '../' dentro de /modelos)."""
    itens = []
    for chave, rotulo, caminho in NAV:
        marca = ' class="atual"' if chave == atual else ''
        itens.append('<a href="%s%s"%s>%s</a>' % (p, caminho, marca, rotulo))
    itens.append('<a href="#" class="btn-zap" data-chat>💬 Orçamento</a>')

    classe = 'barra solida' if solida else 'barra'
    casa = '%sindex.html' % p
    return '''<header class="%s" id="barra">
  <a href="%s" class="logo-wrap" style="display:block">%s</a>
  <nav class="nav">
    %s
  </nav>
  <button class="menu-btn" id="menuBtn" aria-label="Menu" aria-expanded="false">
    <span></span><span></span><span></span>
  </button>
</header>''' % (classe, casa, LOGO, '\n    '.join(itens))


def rodape(p):
    navega = ''.join('<a href="%s%s">%s</a>' % (p, caminho, rotulo)
                     for _, rotulo, caminho in NAV)
    return '''<footer>
  <div class="fg">
    <div><h4>Casa Nobre Piscinas</h4>
      <p>Piscinas, spas e tudo que mantém a sua água em dia.<br>
      %s</p></div>
    <div><h4>Navegar</h4>
      %s</div>
    <div><h4>Contato</h4>
      <a href="#" data-chat>Chat no site</a>
      <a href="tel:%s">Telefone %s</a>
      <a href="mailto:%s">%s</a>
      <a href="https://instagram.com/%s">@%s</a></div>
  </div>
  <div class="fb2">Modelo de apresentação — Axisnetworks · conteúdo placeholder, não publicar</div>
</footer>''' % (ENDERECO, navega, TEL_LINK, TELEFONE, EMAIL, EMAIL, INSTA, INSTA)


CHAT = '''<div class="chat-jan" id="chatJan">
  <div class="chat-top">
    <div class="chat-av">💬</div>
    <div><h4>Atendimento Casa Nobre</h4><div class="on">Online agora</div></div>
    <button class="chat-x" id="chatX" aria-label="Fechar">×</button>
  </div>
  <div class="chat-corpo" id="chatCorpo"></div>
  <form class="chat-pe" id="chatForm">
    <input type="text" id="chatInput" placeholder="Escreva sua mensagem..." autocomplete="off">
    <button type="submit" class="chat-env" aria-label="Enviar">➤</button>
  </form>
</div>
<button class="chat-btn" id="chatBtn">
  <span class="bolha">💬</span><span class="txt">Fale com a gente</span><span class="pisca"></span>
</button>'''


def pagina(titulo, descricao, corpo, p='', atual='', solida=True, scripts=(), embutido=''):
    """Monta a pagina inteira. `corpo` e so o miolo — o resto vem daqui."""
    tags = ''.join('<script src="%sassets/%s"></script>\n' % (p, s) for s in scripts)
    extra = ('<script>\n%s\n</script>\n' % embutido) if embutido else ''
    return '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<!-- Modelo de apresentacao em ambiente de teste: nao pode ser indexado. -->
<meta name="robots" content="noindex,nofollow">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="%s" rel="stylesheet">
<link rel="stylesheet" href="%sassets/estilo.css">
</head>
<body>

<div class="aviso">%s</div>

%s

%s

%s

%s
<script src="%sassets/site.js"></script>
<script src="%sassets/chat.js"></script>
%s%s</body>
</html>
''' % (titulo, descricao, FONTES, p, AVISO,
       cabecalho(atual, p, solida), corpo, rodape(p), CHAT, p, p, tags, extra)
