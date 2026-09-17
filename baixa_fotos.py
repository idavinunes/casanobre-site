import urllib.request, json, ssl, os, time
ctx = ssl.create_default_context()
UA = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/122 Safari/537.36'}
DEST = os.path.expanduser('~/dev/casanobre-site/midia')
os.makedirs(DEST, exist_ok=True)

def get(url, timeout=30):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
        return r.read()

buscas = [
    ("hero",   "luxury swimming pool villa"),
    ("pool",   "backyard swimming pool"),
    ("pool2",  "modern swimming pool house"),
    ("spa",    "outdoor hot tub spa"),
    ("noite",  "swimming pool night lights"),
    ("lazer",  "family swimming pool summer"),
]

# ND = no derivatives -> nao serve (nao podemos recortar/sobrepor texto)
LIC_OK = {'by', 'by-sa', 'cc0', 'pdm'}

catalogo = []
usados = set()

for slug, termo in buscas:
    q = urllib.parse.quote(termo)
    url = (f"https://api.openverse.org/v1/images/?q={q}&page_size=40"
           f"&license_type=commercial&aspect_ratio=wide")
    try:
        d = json.loads(get(url).decode())
    except Exception as e:
        print(f"[{slug}] erro busca: {str(e)[:90]}")
        continue

    achou = False
    for item in d.get('results', []):
        lic = (item.get('license') or '').lower()
        u   = item.get('url') or ''
        ident = item.get('id')
        if lic not in LIC_OK or not u or ident in usados:
            continue
        try:
            dados = get(u, timeout=35)
        except Exception:
            continue
        if len(dados) < 45000:      # muito pequena = thumb
            continue
        nome = f"{slug}.jpg"
        with open(os.path.join(DEST, nome), 'wb') as f:
            f.write(dados)
        usados.add(ident)
        catalogo.append({
            'arquivo': nome, 'busca': termo,
            'titulo': (item.get('title') or '')[:70],
            'autor': (item.get('creator') or 'desconhecido')[:50],
            'licenca': lic.upper(),
            'fonte': item.get('foreign_landing_url') or u,
            'kb': len(dados)//1024,
        })
        print(f"[{slug}] OK {len(dados)//1024}KB  {lic.upper():6} {(item.get('title') or '')[:40]}")
        achou = True
        break
    if not achou:
        print(f"[{slug}] nada utilizavel")

with open(os.path.join(DEST, 'CREDITOS.json'), 'w') as f:
    json.dump(catalogo, f, indent=2, ensure_ascii=False)

print(f"\nbaixadas: {len(catalogo)}")
