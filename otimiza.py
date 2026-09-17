from PIL import Image
import os, glob

D = os.path.expanduser('~/dev/casanobre-site/midia')
total_antes = total_depois = 0

for f in sorted(glob.glob(os.path.join(D, '*.jpg'))):
    antes = os.path.getsize(f)
    total_antes += antes
    im = Image.open(f)
    im = im.convert('RGB')
    w, h = im.size
    # largura maxima 1600px, mantendo proporcao
    if w > 1600:
        nh = int(h * 1600 / w)
        im = im.resize((1600, nh), Image.LANCZOS)
    im.save(f, 'JPEG', quality=82, optimize=True, progressive=True)
    depois = os.path.getsize(f)
    total_depois += depois
    print(f"  {os.path.basename(f):26} {w}x{h} -> {im.size[0]}x{im.size[1]}  "
          f"{antes//1024}KB -> {depois//1024}KB")

print(f"\nTOTAL: {total_antes//1024}KB -> {total_depois//1024}KB "
      f"({100 - total_depois*100//total_antes}% menor)")
