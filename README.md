# Casa Nobre Piscinas — modelo de site

**Status:** modelo de apresentação. **Não publicar.**
Fonte de verdade do cliente: `~/dev/aiox-vault/06-Empresas/casa-nobre-store.md`

## Rodar

Abra `index.html` no navegador. Não precisa de servidor.
(Para ver com os caminhos certos: `python3 -m http.server 8787` na raiz.)

## ⚠️ Nenhum HTML se edita à mão

**Todas** as páginas são geradas. Editou qualquer coisa e quer ver no site:

```bash
.venv/bin/python gera_paginas.py
```

O que você edita:

| Quero mudar… | Edite |
|---|---|
| menu, logo, rodapé, chat | `layout.py` |
| texto/blocos de uma página | `conteudo/<pagina>.html` |
| os modelos de piscina | `assets/modelos.js` |
| aparência | `assets/estilo.css` |
| a fonte dos títulos | `--fonte-tit` no `estilo.css` + `FONTES` no `layout.py` |
| comportamento | `assets/*.js` |

Adicionar uma página nova: crie `conteudo/nova.html`, adicione uma linha na lista
`FIXAS` do `gera_paginas.py` e (se ela entra no menu) uma linha em `NAV` no `layout.py`.

## Estrutura

```
teste-fontes.html       comparação das 8 fontes (ferramenta, não é página do site)
layout.py               cabeçalho, menu, rodapé e chat  ← FONTE ÚNICA
gera_paginas.py         gera TODAS as páginas
conteudo/*.html         o miolo de cada página fixa

index.html              home / vitrine          ← GERADO
como-funciona.html      processo em 6 etapas    ← GERADO
sobre.html              a empresa + marcas      ← GERADO
contato.html            canais + mapa           ← GERADO
modelos/index.html      lista com filtros       ← GERADO
modelos/<slug>.html     detalhe + ficha técnica ← GERADO

assets/estilo.css       CSS de todas as páginas
assets/modelos.js       DADOS dos modelos (fonte única)
assets/site.js          barra, reveal e menu do celular (todas as páginas)
assets/home.js          hero + carrossel (só a home)
assets/lista.js         filtros da lista de modelos
assets/detalhe.js       galeria da página de modelo
assets/chat.js          web chat (demo de fluxo)
midia/                  fotos
otimiza.py              redimensiona fotos para 1600px
```

## Navegação

O menu leva a **páginas separadas** — não é mais rolagem por âncora numa página só.
A home ficou como vitrine curta (hero · pilares · carrossel · CTA) e manda para
`como-funciona`, `modelos` e `contato`. Os números ("00 anos de mercado") saíram da
home e estão em `sobre.html`.

## Ligar o vídeo de fundo do hero

Em `conteudo/home.html`, ponha o ID do vídeo do YouTube e rode o gerador:

```html
<div class="bg-video" id="bgVideo" data-video="ID_DO_VIDEO"
     data-inicio="73" data-fim="130">
```

`data-inicio` e `data-fim` (em segundos) cortam um trecho do vídeo — opcionais.

> ⚠️ **Hoje está com o vídeo do CONCORRENTE** (Cristal Pool, `L-Q0qFJsB_w`,
> trecho 73→130s) só para demonstrar o efeito. **Trocar pelo vídeo da Casa Nobre**
> antes de mostrar como se fosse dela.

O fundo vira vídeo e as fotos somem sozinhas. Técnica copiada da Cristal Pool
(iframe maior que a tela, `pointer-events:none`, controles ocultos).
Sem ID, as 3 fotos do hero giram com fade de 1,6s.

## Decisões já tomadas (não refazer sem falar com o Davi)

- **Páginas separadas** no lugar de rolagem em página única — decisão do Davi.
- **Web chat** no lugar do WhatsApp — decisão do cliente.
- **Logo:** negativo branco (onda em `#6F96CE`) sobre o hero; colorido na barra branca ao rolar.
- **Fonte:** **Outfit em tudo** — corpo e títulos (peso 200 nos títulos grandes).
  **Fraunces saiu** (2026-09-16): o Davi não gostou do desenho serifado.
  Inter continua vetada por ser genérica.
  ⚠️ **Outfit não tem itálico.** O destaque dos títulos (`<em>`) é feito por
  **peso + cor**, nunca por `font-style:italic` — senão o navegador inclina na
  força e fica torto. Se um dia voltar uma serifada com itálico de verdade,
  é devolver `font-style:italic` nas regras `em`.
  Comparação das 8 opções avaliadas: `teste-fontes.html`.
- **Cores:** `#212A53` marinho · `#33509E` royal · `#6F96CE` claro — medidas por
  contagem de pixel nas pranchetas da identidade nova.

## ⚠️ O que falta (bloqueios reais)

- 🔴 **Foto real de obra entregue.** As atuais são banco livre (CC-BY, piscina de
  resort) — servem para apresentar o layout, **não para publicar**. Créditos em
  `midia/CREDITOS.json`. Todo concorrente do segmento vive de foto de obra.
- 🔴 **Vetor do logo (SVG/AI).** O logo do site foi *reconstruído* com a fonte
  Outfit — é aproximação. Para produção, pedir o original ao designer.
- 🔴 **Dados técnicos reais** dos modelos (hoje tudo `0,00`).
- 🔴 **Horário de atendimento** em `contato.html` está `00h às 00h`.
- 🔴 **Confirmar com o cliente:** os "12 anos" são de mercado/instalação — a Casa
  Nobre **não fabrica**, revende fibra (GM Fibras) e constrói alvenaria.
- 🟡 **Vídeos** `midia/hero.mp4`, `obra-01.mp4` e `spa-02.mp4` não existem — os
  blocos caem no placeholder sozinhos, sem quebrar.

## Nota sobre o chat

É **demonstração de fluxo**: roteiro fixo com chips de resposta rápida, para
mostrar ao cliente como a conversa se comporta. Não há atendente nem IA atrás.
Ligar em gente real ou IA é etapa futura — candidatos no vault: atende-ai/zpro + n8n.
