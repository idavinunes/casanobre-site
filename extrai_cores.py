from PIL import Image
import collections, glob, os, json

base = "/Users/davinunes/Library/Application Support/Hermes/composer-images/"
arquivos = sorted(glob.glob(base + "Prancheta_*.png"))

todas = collections.Counter()
for f in arquivos:
    im = Image.open(f).convert("RGB")
    im.thumbnail((900, 900))
    c = collections.Counter(im.getdata())
    nome = os.path.basename(f)
    print(f"\n=== {nome} ===")
    for (r, g, b), n in c.most_common(400):
        # ignora branco/quase branco e cinza neutro
        if r > 238 and g > 238 and b > 238:
            continue
        mx, mn = max(r, g, b), min(r, g, b)
        if mx - mn < 18:          # neutro (antialias cinza)
            continue
        if b <= max(r, g):        # queremos azuis: B dominante
            continue
        todas[(r, g, b)] += n
        if n > 90:
            print(f"  #{r:02X}{g:02X}{b:02X}  rgb({r},{g},{b})  px={n}")

print("\n\n=========== AZUIS DOMINANTES (todas as pranchetas) ===========")
for (r, g, b), n in todas.most_common(14):
    print(f"  #{r:02X}{g:02X}{b:02X}  rgb({r:3d},{g:3d},{b:3d})  px={n}")
