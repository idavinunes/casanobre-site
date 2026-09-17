# Etapa 1 — gera TODAS as páginas a partir de layout.py + conteudo/ + assets/modelos.js
# (o gerador só usa stdlib; o Pillow do .venv é das ferramentas de foto, não dele)
FROM python:3.12-alpine AS build
WORKDIR /app
COPY layout.py gera_paginas.py ./
COPY conteudo/ ./conteudo/
COPY assets/ ./assets/
RUN python3 gera_paginas.py

# Etapa 2 — nginx servindo o site estático
FROM nginx:1.27-alpine

COPY --from=build /app/index.html /app/como-funciona.html /app/sobre.html /app/contato.html /usr/share/nginx/html/
COPY --from=build /app/modelos/ /usr/share/nginx/html/modelos/
COPY --from=build /app/assets/ /usr/share/nginx/html/assets/
COPY midia/ /usr/share/nginx/html/midia/

# Healthcheck com carência: sem --start-period o contêiner nasce reprovado
HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
  CMD wget -qO- http://127.0.0.1/ >/dev/null 2>&1 || exit 1

EXPOSE 80
